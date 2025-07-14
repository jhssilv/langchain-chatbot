from langchain.tools import tool

@tool
def get_store_conversion_rate(store_name: str) -> str:
    """
    Use esta ferramenta para obter a taxa de conversão de uma loja específica.
    A ferramenta espera o nome exato da loja como entrada.
    """
    print(f"🔎 Executando a ferramenta 'get_store_conversion_rate' para a loja: {store_name}")
    # Lógica real de busca no banco de dados iria aqui
    if "loja a" in store_name.lower():
        return "A taxa de conversão da Loja A é de 5.2%."
    elif "loja b" in store_name.lower():
        return "A taxa de conversão da Loja B é de 4.1%."
    else:
        return f"Não encontrei dados para a loja '{store_name}'. As opções são: Loja A, Loja B."

@tool
def get_top_seller_last_month() -> str:
    """
    Use esta ferramenta para descobrir qual vendedor teve o melhor desempenho no mês passado.
    Esta ferramenta não precisa de nenhum parâmetro de entrada.
    """
    print("🔎 Executando a ferramenta 'get_top_seller_last_month'")
    # Lógica real de busca no banco de dados iria aqui
    return "O vendedor com melhor desempenho no mês passado foi 'Carlos Silva' com R$ 25.430,00 em vendas."