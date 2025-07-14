import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from tools import all_tools 

load_dotenv()

# --- Memória ---
# TODO: Implementar memória em MySql
chat_histories = {}

def get_agent_executor():
    # --- Configuração do LLM ---
    llm_provider = os.getenv("LLM_PROVIDER", "GOOGLE").upper()
    llm = None

    print(f"LLM Provider Selected: {llm_provider}")

    if llm_provider == "OPENAI":
        llm = ChatOpenAI(
            model=os.getenv("LLM_MODEL_NAME_OPENAI", "gpt-4o"),
            temperature=float(os.getenv("LLM_TEMPERATURE", 0.0))
        )
    elif llm_provider == "GOOGLE":
        llm = ChatGoogleGenerativeAI(
            model=os.getenv("LLM_MODEL_NAME_GEMINI", "gemini-1.5-flash"),
            temperature=float(os.getenv("LLM_TEMPERATURE", 0.0))
        )
    else:
        raise ValueError(f"Error. LLM_PROVIDER must be GOOGLE or OPENAI.")

    tools = all_tools

    # --- Configuração do Prompt ---
    prompt = ChatPromptTemplate.from_messages([
        ("system", """
        INSTRUÇÕES DE SISTEMA:
        - Você é A.R.I.A (Assistente de Relatórios e Insights Analíticos), uma assistente de IA sênior.
        - Sua especialidade é analisar dados de performance de lojas para gerentes.
        - Responda sempre em português do Brasil.
        
        REGRAS DE FORMATAÇÃO DA RESPOSTA FINAL:
        1. Ao formular sua RESPOSTA FINAL para o usuário, você DEVE incluir não apenas a conclusão, mas também um resumo dos dados ou passos que usou para chegar a ela.
        2. Se a sua análise envolveu múltiplas informações (ex: vendas de várias lojas), apresente os dados de forma clara na resposta final antes de dar o total ou a conclusão.
        3. NÃO resuma demais sua resposta final. O usuário precisa ver os dados que suportam sua conclusão. A sua resposta final deve ser completa e auto-contida.
        4. A resposta final NUNCA deve conter as palavras 'Pensamento', 'Ação', ou 'Observação'.
        5. Você está trabalhando pelo Whatsapp, então pode usar regras simples de formatação que o chat disponibiliza.
        
        REGRAS DE EXECUÇÃO:
        - Para obter dados, use as ferramentas disponíveis. Não invente respostas.
        - Use o histórico da conversa para entender perguntas de acompanhamento.
        """),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    # --- Criação do Agente e Executor ---
    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    print("✅ Agent Executor created")
    return agent_executor

# Cria uma instância única do executor que será usada pela API.
agent_executor_instance = get_agent_executor()