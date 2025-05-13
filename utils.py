
import re

CAMPOS = {
    'Solicitação': r'Solicitação[:\-]?\s*(.+)',
    'Telefone': r'Telefone[:\-]?\s*([\d\s]+)',
    'Passageiro': r'Passageiro[:\-]?\s*(.+)',
    'Origem': r'Origem[:\-]?\s*(.+)',
    'Destino': r'Destino[:\-]?\s*(.+)',
    'Data': r'Data[:\-]?\s*(\d{2}/\d{2}/\d{4})',
    'Início': r'Início[:\-]?\s*(\d{2}:\d{2}:\d{2})',
    'Fim': r'Fim[:\-]?\s*(\d{2}:\d{2}:\d{2})',
    'Nº Serviço': r'No\.?.? Serviço[:\-]?\s*(\d+)',
    'Preferências': r'Preferências[:\-]?\s*(.*)',

    'Contrato': r'CONTRATO[:\-]?\s*(.+)',
    'Nome do Passageiro': r'Nome do Passageiro[:\-]?\s*(.+)',
    'Nível D': r'Nível D[:\-]?\s*(.+)',
    'Nível E': r'Nível E[:\-]?\s*(.+)',
    'Nível F': r'Nível F[:\-]?\s*(.+)',
    'Protocolo MPRJ': r'Protocolo MPRJ[:\-]?\s*(\d+)',
    'Autorizador': r'Autorizador[:\-]?\s*(.+)',

    'KM': r'KM[:\-]?\s*([\d.,]+)',
    'Valor do Serviço': r'Valor do Serviço R\$[:\-]?\s*([\d.,]+)',
    'Taxa Fixa': r'Taxa Fixa[:\-]?\s*R?\$?\s*([\d.,]+)',
    'Taxa %': r'Taxa %[:\-]?\s*([\d.,]+)',
    'Valor Taxa R\$': r'Valor Taxa R\$[:\-]?\s*([\d.,]+)',
    'Tempo Parado': r'Tempo Parado[:\-]?\s*R?\$?\s*([\d.,]+)',
    'Tempo parado\(embarque aguardando\)': r'Tempo parado\(embarque aguardando\)[:\-]?\s*([\d.,]+)',
    'Desc. Tempo Parado': r'Desc\. Tempo Parado[:\-]?\s*R?\$?\s*([\d.,]+)',
    'Distância HP': r'Distância HP[:\-]?\s*([\d.,]+)',
    'Hora Parada R\$': r'Hora Parada R\$[:\-]?\s*([\d.,]+)',
    'Hora R\$': r'Hora R\$[:\-]?\s*([\d.,]+)',
    'Pedágio R\$': r'Pedágio R\$[:\-]?\s*([\d.,]+)',
    'Recebido por R\$': r'Recebido por R\$[:\-]?\s*([\d.,]+)',
    'Valor Repasse Motorista': r'Valor Repasse Motorista[:\-]?\s*([\d.,]+)',
    'Total/Devido R\$': r'Total/Devido R\$[:\-]?\s*([\d.,]+)',
    'KM Final': r'KM Final[:\-]?\s*([\d.,]+)',
}

def extrair_dados_formatados(texto):
    dados = {}
    faltando = []
    for campo, padrao in CAMPOS.items():
        match = re.search(padrao, texto, re.IGNORECASE)
        valor = match.group(1).strip() if match else ""
        dados[campo] = valor
        if not valor:
            faltando.append(campo)
    return dados, faltando
