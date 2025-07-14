from langchain.tools import tool
import datetime

@tool
def get_current_date() -> str:
    "Retorna a data atual em formato AAAA-MM-DD"
    print(f"🔎 Executando a ferramenta 'get_current_date'")
    return f"{datetime.date.today().isoformat()}"