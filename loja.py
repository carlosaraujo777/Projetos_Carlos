import streamlit as st
import pandas as pd
from datetime import datetime # <--- Adicione essa linha
st.set_page_config(page_title="Loja do Carlos", page_icon="🛒")

# 1. Inicializa o "carrinho" na memória do app
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []
if 'tela' not in st.session_state:
    st.session_state.tela = "loja"

# Produtos disponíveis (poderia vir de um banco de dados, mas aqui é fixo)
produtos = {
    "Teclado Mecânico": 150.00,
    "Mouse Gamer": 80.00,
    "Monitor 144Hz": 900.00,
    "Headset": 200.00,
    "Cadeira Gamer": 450.00,
    "Mousepad Gamer": 50.00,
    "Webcam HD": 120.00,
    "Microfone Condesador com rgb": 300.00,
    "PS5": 4000.00
    
}

# ----- TELA 1: LOJA -----
if st.session_state.tela == "loja":
    st.title("🛒 Loja do Carlos")
    st.subheader("Produtos disponíveis:")
    
    for nome, preco in produtos.items():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{nome}** - R$ {preco:.2f}")
        with col2:
            if st.button(f"Adicionar", key=nome):
                st.session_state.carrinho.append({"nome": nome, "preco": preco})
                st.toast(f"{nome} adicionado!")

    st.divider()
    qtd_carrinho = len(st.session_state.carrinho)
    
    if st.button(f"🛍️ Ver Carrinho ({qtd_carrinho} itens)"):
        st.session_state.tela = "carrinho"
        st.rerun()

# ----- TELA 2: CARRINHO -----
elif st.session_state.tela == "carrinho":
    st.title("🛍️ Seu Carrinho")
    
    if not st.session_state.carrinho:
        st.warning("Seu carrinho está vazio!")
    else:
        total = 0
        for item in st.session_state.carrinho:
            st.write(f"- {item['nome']}: R$ {item['preco']:.2f}")
            total += item['preco']
        
        st.divider()
        st.subheader(f"Total: R$ {total:.2f}")
        
        st.write("Escolha o método de pagamento:")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Pagar com Pix"):
                st.session_state.tela = "finalizado"
                st.rerun()
        with col2:
            if st.button("Pagar com Cartão"):
                st.session_state.tela = "finalizado"
                st.rerun()
                
    if st.button("⬅️ Voltar para a loja"):
        st.session_state.tela = "loja"
        st.rerun()

# ----- TELA 3: SUCESSO -----
# ----- TELA 3: SUCESSO -----
elif st.session_state.tela == "finalizado":
    st.balloons()
    st.success("🎉 Sua compra foi concluída com sucesso!")
    
    # --- A MÁGICA ACONTECE AQUI ---
    # 1. Monta os dados da compra
    total = sum(item['preco'] for item in st.session_state.carrinho)
    itens_comprados = ", ".join([item['nome'] for item in st.session_state.carrinho])
    
    # 2. Cria a linha que vai pro arquivo
    nova_compra = {
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "itens": itens_comprados,
        "total": total,
        "pagamento": "Pix ou Cartão" # Você pode guardar a escolha exata depois
    }
    
    # 3. Salva no arquivo CSV
    # (Se o arquivo não existir, ele cria. Se existir, ele adiciona no final)
    try:
        df_existente = pd.read_csv("vendas.csv")
        df_novo = pd.DataFrame([nova_compra])
        df_final = pd.concat([df_existente, df_novo], ignore_index=True)
        df_final.to_csv("vendas.csv", index=False)
    except FileNotFoundError:
        df_novo = pd.DataFrame([nova_compra])
        df_novo.to_csv("vendas.csv", index=False)
        
    st.write("Obrigado por comprar na Loja do Carlos! Seus dados foram salvos.")
    
    if st.button("Fazer uma nova compra"):
        st.session_state.carrinho = [] 
        st.session_state.tela = "loja"
        st.rerun()