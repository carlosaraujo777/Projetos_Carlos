# 📊 Dashboard de E-commerce — Análise de Vendas

Dashboard em Power BI com análise de vendas de um e-commerce, usando dados públicos do [Kaggle](https://www.kaggle.com/datasets/abbas829/ecommerce-sales-dataset).

## 🎯 Objetivo
Analisar vendas por categoria, região, método de pagamento e evolução mensal, com o objetivo de praticar modelagem, DAX e visualização de dados no Power BI.

## 🛠 Ferramentas
- Power BI
- Power Query
- DAX

## 📈 KPIs
- Total de Vendas: R$ 182 Mi
- Ticket Médio: R$ 92 Mil
- Quantidade de Pedidos: 2 Mil
- Média de Dias para Entrega: 6,13

## 💡 Principais Insights
- Eletrônicos é a categoria que mais vende (R$ 63 Mi)
- Regiões Sul, Leste e Oeste ficam quase empatadas (~25% cada)
- Cartão de crédito é o método de pagamento mais usado (897 pedidos)
- Pico de vendas em agosto

## 🖼 Dashboard
![Painel](painel.png)

## 📂 Estrutura do Projeto
- `dashboard.pbix` — arquivo do Power BI
- `dados/ecommerce_sales_analytics_5000.csv` — dataset utilizado
- `imagens/dashboard.png` — print do dashboard

## 🔗 Fonte dos dados
[Kaggle - Ecommerce sales dataset](https://www.kaggle.com/datasets/abbas829/ecommerce-sales-dataset)

---

> Observação: os dados são sintéticos, disponibilizados publicamente no Kaggle para fins de estudo e prática.

---

## 🤖 Automação com Python

### Sobre
Script em Python que lê 5 arquivos CSV do dataset público da Olist (e-commerce brasileiro), 
faz a junção das tabelas, gera análises e salva em Excel — **tudo automaticamente**.

### 🛠 Tecnologias
- Python 3
- Pandas
- Agendador de Tarefas do Windows

### 📊 O que ele faz
1. Lê 5 CSVs (pedidos, clientes, itens, produtos, pagamentos)
2. Junta todas as tabelas em uma só (merge)
3. Gera 4 análises:
   - Top 10 categorias que mais vendem
   - Top 10 estados que mais compram
   - Vendas por mês
   - Formas de pagamento
4. Salva tudo em Excel com 4 abas

### ⏰ Como roda
O script está agendado no **Agendador de Tarefas do Windows** e roda 
**automaticamente todos os dias às 08:00**.

### 📂 Arquivos
- `olist_tratado.py` — script Python
- `rodar_olist.bat` — arquivo de execução
- `analises_olist.xlsx` — resultado gerado (4 abas)

### 🔗 Fonte dos dados
[Kaggle - Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
