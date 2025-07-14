from langchain.tools import tool
import datetime
from typing import Literal, Optional

@tool
def send_report(
    store_name: str, 
    report_type: Literal['simple', 'conversion', 'flow'] = 'simple', 
    dates: Optional[str] = None
) -> str:
    """Gera e envia um relatório de performance para uma loja específica. 

    Args:
        store_name: O nome exato da loja para a qual o relatório deve ser gerado.
        report_type: Define o formato do relatório. Os valores válidos são 'simple', 'conversion' ou 'flow'.
        date: A data do relatório no formato AAAA-MM-DD ou como período [AAAA-MM-DD, AAAA-MM-DD]. Se não for fornecida, a data de hoje será usada.
    """
    if dates is None:
        # Usamos a data atual formatada corretamente
        dates = datetime.date.today().isoformat()

    print(f"🔎 Executando a ferramenta 'send_report' para a loja: '{store_name}', com os parâmetros report_type='{report_type}' e date='{dates}'")
    # Lógica real de busca no banco de dados iria aqui
    return f"Relatório do tipo '{report_type}' para a loja '{store_name}' referente às datas {dates} foi enviado com sucesso!"