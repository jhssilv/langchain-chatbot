from langchain.tools import tool

@tool
def open_support_ticket(description: str) -> str:
    """
    Use esta ferramenta criar um ticket de suporte para o usuário.
    Insira uma descrição da solicitação do usuário em description.
    """
    print(f"🔎 Executando a ferramenta 'open_support_ticket' com a descrição:\n\n{description}\n\n")
    # Lógica real de busca no banco de dados iria aqui
    return "Ticket criado com sucesso. Número do ticket: 1234"
