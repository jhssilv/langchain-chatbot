from langchain.tools import tool

@tool
def get_store_info(store_name: str) -> str:
    """
    Use esta ferramenta para obter as informações sobre a loja.
    Returns: Nome, Setor, Local
    """
    print(f"🔎 Executando a ferramenta 'get_store_info' para a loja: {store_name}")
    if store_name.lower() == 'loja a':
        return "Nome: Loja A, Setor: Calçados, Local: Porto Alegre"
    elif store_name.lower() == 'loja b':
        return "Nome: Loja B, Setor Alimentos, Local: São Paulo"
    else:
        return "Nenhuma loja encontrada com esse nome"