import streamlit as st
import base64

st.set_page_config(page_title="Relatório ODS", page_icon="📄")

st.title("📄 Relatório ODS - Erradicação da Pobreza")
st.write("Aqui você pode visualizar o relatório diretamente ou baixá-lo como PDF.")

# Caminho do arquivo PDF
pdf_path = "data/relatorio.pdf"

# Ler e converter PDF para base64
with open(pdf_path, "rb") as pdf_file:
    pdf_bytes = pdf_file.read()
    base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')

# Exibir PDF usando HTML
pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
st.markdown(pdf_display, unsafe_allow_html=True)

# Adicionar botão de download
st.download_button(
    label="📥 Download PDF",
    data=pdf_bytes,
    file_name="relatorio_ods.pdf",
    mime="application/pdf"
)