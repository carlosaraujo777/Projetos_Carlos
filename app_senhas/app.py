import streamlit as st
import random
import string

st.set_page_config(page_title="Gerador de Senhas", page_icon="🔐")

st.title("🔐 Gerador de Senhas Seguras pra uso pessoal ou corporativo")
st.markdown("Crie senhas fortes e personalizadas com um clique.")

# Controles na barra lateral
st.sidebar.header("Configurações")
tamanho = st.sidebar.slider("Tamanho da senha", min_value=4, max_value=50, value=12)

usar_numeros = st.sidebar.checkbox("Incluir números", value=True)
usar_simbolos = st.sidebar.checkbox("Incluir símbolos", value=True)

# Monta o "pool" de caracteres
caracteres = string.ascii_letters
if usar_numeros:
    caracteres += string.digits
if usar_simbolos:
    caracteres += string.punctuation

# Botão para gerar
if st.button("Gerar Senha"):
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    
    # Mostra a senha em destaque
    st.success("Senha gerada com sucesso!")
    st.code(senha, language=None)
    
    # Opção de copiar (o Streamlit já tem o botão de copiar no canto do código)

st.markdown("---")
st.caption("Desenvolvido por Carlos Alexandre Araújo | Python + Streamlit")