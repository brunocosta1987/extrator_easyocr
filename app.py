
import streamlit as st
from PIL import Image
import easyocr
import pandas as pd
from io import BytesIO
from utils import extrair_dados_formatados

st.title("Extração de Dados de Imagens PNG para Excel (sem Tesseract)")

uploaded_files = st.file_uploader("Faça upload de até 50 imagens PNG", type=["png"], accept_multiple_files=True)

if uploaded_files:
    reader = easyocr.Reader(['pt'], gpu=False)
    todos_dados = []
    alertas = []

    for img_file in uploaded_files:
        imagem = Image.open(img_file)
        result = reader.readtext(np.array(imagem), detail=0, paragraph=True)
        texto = "\n".join(result)
        dados_formatados, faltando = extrair_dados_formatados(texto)
        dados_formatados['Arquivo'] = img_file.name
        todos_dados.append(dados_formatados)

        if faltando:
            alertas.append(f"⚠️ {img_file.name}: Campos não extraídos -> {', '.join(faltando)}")

    df_final = pd.DataFrame(todos_dados)
    st.write("Pré-visualização dos dados extraídos:")
    st.dataframe(df_final)

    for alerta in alertas:
        st.warning(alerta)

    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df_final.to_excel(writer, index=False, sheet_name='Dados')
        writer.save()
        st.download_button(
            label="📥 Baixar Excel",
            data=output.getvalue(),
            file_name="dados_extraidos.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
