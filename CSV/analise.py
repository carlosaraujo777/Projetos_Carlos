import pandas as pd

# Abre o CSV
dados = pd.read_csv("ecommerce_sales_analytics_5000.csv")

# ----- Resumo geral -----
resumo = pd.DataFrame({
    "Indicador": ["Faturamento Total", "Ticket Médio", "Total de Pedidos", "Dias Médios de Entrega"],
    "Valor": [
        dados["revenue"].sum(),
        dados["revenue"].mean(),
        len(dados),
        dados["delivery_days"].mean()
    ]
})

# ----- Análises por grupo -----
por_categoria = dados.groupby("product_category")["revenue"].sum().sort_values(ascending=False)
por_regiao = dados.groupby("region")["revenue"].sum().sort_values(ascending=False)
por_pagamento = dados.groupby("payment_method")["revenue"].sum().sort_values(ascending=False)

# ----- Cria Excel com várias abas -----
with pd.ExcelWriter("relatorio_completo.xlsx") as writer:
    resumo.to_excel(writer, sheet_name="Resumo", index=False)
    por_categoria.to_excel(writer, sheet_name="Por Categoria")
    por_regiao.to_excel(writer, sheet_name="Por Região")
    por_pagamento.to_excel(writer, sheet_name="Por Pagamento")

print("✅ Relatório completo criado: relatorio_completo.xlsx")