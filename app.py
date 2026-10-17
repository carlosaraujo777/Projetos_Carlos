import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Portfólio de Dados — Carlos Araújo",
    page_icon="⚡",
    layout="wide"
)

# --- FUNÇÕES DE FORMATAÇÃO (Padrão BR: 1.000,00) ---
def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def formatar_numero(valor):
    return f"{valor:,.0f}".replace(",", ".")

# --- BASE DE DADOS TRATADA DE TECNOLOGIA ---
np.random.seed(42)
n_linhas = 300

produtos = ['Licença Cloud Enterprise', 'Notebook Pro 15', 'Servidor Rack 2U', 'Sistema ERP SaaS']
categorias = {'Licença Cloud Enterprise': 'SaaS', 'Notebook Pro 15': 'Hardware', 'Servidor Rack 2U': 'Hardware', 'Sistema ERP SaaS': 'SaaS'}
precos = {'Licença Cloud Enterprise': 1200, 'Notebook Pro 15': 8500, 'Servidor Rack 2U': 25000, 'Sistema ERP SaaS': 3500}
regioes = ['Sudeste', 'Sul', 'Nordeste', 'Centro-Oeste', 'Norte']

prods = np.random.choice(produtos, n_linhas)
qtds = np.random.randint(1, 8, n_linhas)

df = pd.DataFrame({
    'Produto': prods,
    'Categoria': [categorias[p] for p in prods],
    'Regiao': np.random.choice(regioes, n_linhas),
    'Quantidade': qtds,
    'Preco_Unitario': [precos[p] for p in prods]
})
df['Faturamento'] = df['Quantidade'] * df['Preco_Unitario']

# --- BARRA LATERAL (FILTROS) ---
st.sidebar.title("🔍 Filtros do Painel")

filtro_regiao = st.sidebar.multiselect(
    "Selecione a Região:",
    options=list(df['Regiao'].unique()),
    default=list(df['Regiao'].unique())
)

filtro_categoria = st.sidebar.multiselect(
    "Selecione a Categoria:",
    options=list(df['Categoria'].unique()),
    default=list(df['Categoria'].unique())
)

# Aplicando Filtros
df_filtrado = df[
    (df['Regiao'].isin(filtro_regiao)) & 
    (df['Categoria'].isin(filtro_categoria))
]

# --- CABEÇALHO ---
st.title("⚡ Tech Analytics — Dashboard de Vendas B2B")
st.markdown("Portal interativo de análise de faturamento em tecnologia e SaaS.")
st.write("---")

# --- KPIs PRINCIPAIS ---
faturamento_total = df_filtrado['Faturamento'].sum()
qtd_total = df_filtrado['Quantidade'].sum()
ticket_medio = faturamento_total / max(len(df_filtrado), 1)

col1, col2, col3 = st.columns(3)
col1.metric("💰 Faturamento Total", formatar_moeda(faturamento_total))
col2.metric("📦 Unidades Vendidas", formatar_numero(qtd_total))
col3.metric("📈 Ticket Médio por Venda", formatar_moeda(ticket_medio))

st.write("---")

# --- GRÁFICO PERSONALIZADO E TABELA ---
col_grafico, col_tabela = st.columns([1.6, 1.4])

with col_grafico:
    st.subheader("📊 Faturamento por Região")
    df_regiao = df_filtrado.groupby('Regiao', as_index=False)['Faturamento'].sum().sort_values('Faturamento', ascending=False)
    
    fig = px.bar(
        df_regiao,
        x='Regiao',
        y='Faturamento',
        text_auto=True,
        color='Faturamento',
        color_continuous_scale='Blues',
        labels={'Regiao': 'Região', 'Faturamento': 'Faturamento (R$)'}
    )
    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        coloraxis_showscale=False
    )
    fig.update_traces(texttemplate='R$ %{y:,.0f}', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

with col_tabela:
    st.subheader("📋 Resumo dos Dados Tratados")
    
    # Criando tabela formatada com ponto de milhar
    df_exibicao = df_filtrado.groupby(['Regiao', 'Categoria'], as_index=False).agg({
        'Quantidade': 'sum',
        'Faturamento': 'sum'
    })
    
    df_exibicao['Faturamento'] = df_exibicao['Faturamento'].apply(formatar_moeda)
    df_exibicao['Quantidade'] = df_exibicao['Quantidade'].apply(formatar_numero)
    
    st.dataframe(df_exibicao, use_container_width=True, hide_index=True)