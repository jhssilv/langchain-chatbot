from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

# Importa a instância do executor e o dicionário de históricos
from agent import agent_executor_instance, chat_histories
from langchain_core.messages import HumanMessage, AIMessage

# Configuração básica de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Inicialização da API ---
app = FastAPI(
    title="A.R.I.A. - Assistente de IA (Memória Local)",
    description="API para interagir com a assistente A.R.I.A. usando memória volátil em dicionário.",
    version="1.0.0-local",
)

# --- Modelos de Dados (Request/Response) ---
class ChatRequest(BaseModel):
    user_id: str
    input: str

class ChatResponse(BaseModel):
    user_id: str
    output: str

# --- Endpoints da API ---
@app.get("/", summary="Verifica o status da API")
def read_root():
    """Endpoint raiz para verificar se a API está online."""
    return {"status": "A.R.I.A. is online."}

@app.post("/invoke", response_model=ChatResponse, summary="Envia uma mensagem para o agente")
async def invoke_agent(request: ChatRequest):
    """
    Processa a mensagem de um usuário e retorna a resposta do agente.
    O histórico da conversa é mantido em um dicionário em memória no servidor.
    """
    if not request.user_id or not request.input:
        raise HTTPException(status_code=400, detail="Os campos 'user_id' e 'input' são obrigatórios.")

    logger.info(f"Recebida requisição do user_id: {request.user_id}")

    try:
        # 1. Recupera o histórico da conversa para este usuário
        current_history = chat_histories.get(request.user_id, [])
        
        # 2. Invoca o agente, passando o input e o histórico específico
        response = await agent_executor_instance.ainvoke({
            "input": request.input,
            "chat_history": current_history
        })
        
        # 3. Atualiza o histórico na memória local
        updated_history = current_history + [
            HumanMessage(content=request.input),
            AIMessage(content=response["output"])
        ]
        chat_histories[request.user_id] = updated_history
        
        logger.info(f"Resposta gerada e histórico atualizado para o user_id: {request.user_id}")
        
        return ChatResponse(user_id=request.user_id, output=response.get("output", ""))

    except Exception as e:
        logger.error(f"Erro ao processar a requisição para {request.user_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Ocorreu um erro interno: {e}")
