import streamlit as st
import plotly.express as px

from src.dados import gerar_dados
from src.logica import calcular_kpis, faturamento_por_regiao, resumo_por_regiao_categoria
from src.formatacao import formatar_moeda, formatar_numero

st.set_page_config(
    page_title="Portfólio de Dados — Carlos Araújo",
    page_icon="⚡",
    layout="wide"
)

df = gerar_dados()

st.sidebar.title("🔍 Filtros do Painel")
filtro_regiao = st.sidebar.multiselect("Selecione a Região:", options=list(df['Regiao'].unique()), default=list(df['Regiao'].unique()))
filtro_categoria = st.sidebar.multiselect("Selecione a Categoria:", options=list(df['Categoria'].unique()), default=list(df['Categoria'].unique()))

df_filtrado = df[
    (df['Regiao'].isin(filtro_regiao)) &
    (df['Categoria'].isin(filtro_categoria))
]

st.title("⚡ Tech Analytics — Dashboard de Vendas B2B")
st.markdown("Portal interativo de análise de faturamento em tecnologia e SaaS.")
st.write("---")

kpis = calcular_kpis(df_filtrado)
col1, col2, col3 = st.columns(3)
col1.metric("💰 Faturamento Total", formatar_moeda(kpis['faturamento_total']))
col2.metric("📦 Unidades Vendidas", formatar_numero(kpis['qtd_total']))
col3.metric("📈 Ticket Médio por Venda", formatar_moeda(kpis['ticket_medio']))

st.write("---")

col_grafico, col_tabela = st.columns([1.6, 1.4])

with col_grafico:
    st.subheader("📊 Faturamento por Região")
    df_regiao = faturamento_por_regiao(df_filtrado)
    fig = px.bar(df_regiao, x='Regiao', y='Faturamento', text_auto=True,
                 color='Faturamento', color_continuous_scale='Blues',
                 labels={'Regiao': 'Região', 'Faturamento': 'Faturamento (R$)'})
    fig.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)",
                      paper_bgcolor="rgba(0,0,0,0)", coloraxis_showscale=False)
    fig.update_traces(texttemplate='R$ %{y:,.0f}', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

with col_tabela:
    st.subheader("📋 Resumo dos Dados Tratados")
    df_exibicao = resumo_por_regiao_categoria(df_filtrado)
    df_exibicao['Faturamento'] = df_exibicao['Faturamento'].apply(formatar_moeda)
    df_exibicao['Quantidade'] = df_exibicao['Quantidade'].apply(formatar_numero)
    st.dataframe(df_exibicao, use_container_width=True, hide_index=True)
