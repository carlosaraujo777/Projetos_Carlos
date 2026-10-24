import pandas as pd

print("Carregando dados...")

pedidos = pd.read_csv("olist_orders_dataset.csv")
clientes = pd.read_csv("olist_customers_dataset.csv")
itens = pd.read_csv("olist_order_items_dataset.csv")
produtos = pd.read_csv("olist_products_dataset.csv")
traducao = pd.read_csv("product_category_name_translation.csv")
pagamentos = pd.read_csv("olist_order_payments_dataset.csv")

# ---- JUNTA TUDO ----
df = pedidos.merge(clientes, on="customer_id", how="left")
df = df.merge(itens, on="order_id", how="left")
df = df.merge(produtos, on="product_id", how="left")
df = df.merge(traducao, on="product_category_name", how="left")
df = df.merge(pagamentos, on="order_id", how="left")

# ---- TRATA ----
df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
df["mes"] = df["order_purchase_timestamp"].dt.month
df["ano"] = df["order_purchase_timestamp"].dt.year

# ---- ANÁLISES ----

# 1. Top 10 categorias
top_categorias = (
    df.groupby("product_category_name_english")["price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# 2. Top 10 estados
top_estados = (
    df.groupby("customer_state")["price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# 3. Vendas por mês
vendas_mes = df.groupby(["ano", "mes"])["price"].sum().reset_index()

# 4. Formas de pagamento
formas_pagamento = (
    df.groupby("payment_type")["price"]
    .sum()
    .sort_values(ascending=False)
)

# ---- MOSTRA NA TELA ----
print()
print("=" * 40)
print("TOP 10 CATEGORIAS")
print("=" * 40)
print(top_categorias)
print()
print("=" * 40)
print("TOP 10 ESTADOS")
print("=" * 40)
print(top_estados)
print()
print("=" * 40)
print("FORMAS DE PAGAMENTO")
print("=" * 40)
print(formas_pagamento)
# ---- SALVA EM EXCEL COM VÁRIAS ABAS ----

with pd.ExcelWriter("analises_olist.xlsx") as writer:
    top_categorias.to_excel(writer, sheet_name="Top Categorias")
    top_estados.to_excel(writer, sheet_name="Top Estados")
    vendas_mes.to_excel(writer, sheet_name="Vendas por Mes", index=False)
    formas_pagamento.to_excel(writer, sheet_name="Pagamentos")

print()
print("✅ Arquivo 'analises_olist.xlsx' criado com 4 abas!")