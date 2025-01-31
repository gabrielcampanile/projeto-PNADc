import streamlit as st

st.set_page_config(page_title="Apresentação ODS", page_icon="📢")

st.title("📢 Apresentação ODS - Erradicação da Pobreza")
st.write("Aqui você pode visualizar a apresentação diretamente ou baixá-lo como PDF.")

# Link da apresentação
apresentacao_link = "https://drive.google.com/file/d/1LFPZSX2velhiRDs5hcShscMTRdfb59_w/view?usp=sharing"

# # Link para visualização externa
# st.markdown(f"[📑 Acesse a apresentação aqui](https://projeto-pnadc.my.canva.site/)", unsafe_allow_html=True)

# Exibir iframe
pdf_embed_link = apresentacao_link.replace("/view", "/preview")
st.markdown(
    f"""
    <iframe id="presentationFrame" src="{pdf_embed_link}" 
            width="800" height="500" style="border: none;">
    </iframe>
    """,
    unsafe_allow_html=True,
)

# Caminho do arquivo PDF
pdf_path = "data/ODS1_ErradicarPobreza.pdf"

# Ler o arquivo PDF
with open(pdf_path, "rb") as pdf_file:
    pdf_bytes = pdf_file.read()

# Botão de download
st.download_button(
    label="📥 Download Apresentação",
    data=pdf_bytes,
    file_name="ODS1_ErradicarPobreza.pdf",
    mime="application/pdf"
)