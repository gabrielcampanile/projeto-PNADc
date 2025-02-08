import streamlit as st

st.set_page_config(page_title="Relatório ODS", page_icon="📄")

st.title("📄 Relatório ODS - Erradicação da Pobreza")
st.write("Aqui você pode visualizar o relatório diretamente ou baixá-lo como PDF.")

# Link do relatório no Google Drive
relatorio_link = "https://drive.google.com/file/d/1WdMvK1Td-fdF-nwHHrRNbtfl2AeA_QbQ/view?usp=sharing"

# Exibir iframe
pdf_embed_link = relatorio_link.replace("/view", "/preview")
st.markdown(
    f"""
    <iframe id="reportFrame" src="{pdf_embed_link}" 
            width="800" height="1120" style="border: none;">
    </iframe>
    """,
    unsafe_allow_html=True,
)

# Caminho do arquivo PDF local
pdf_path = "data/Erradicação_da_Extrema_Pobreza.pdf"

# Ler arquivo PDF
with open(pdf_path, "rb") as pdf_file:
    pdf_bytes = pdf_file.read()

# Botão de download
st.download_button(
    label="📥 Download Relatório",
    data=pdf_bytes,
    file_name="Erradicação_da_Extrema_Pobreza.pdf",
    mime="application/pdf"
)