# 🤖 Automação de Análise — Olist E-commerce

Pipeline em Python que lê, trata e consolida 5 CSVs do dataset público da Olist, gera análises de negócio e exporta para Excel — rodando automaticamente todos os dias.

## 🎯 Objetivo
Automatizar um fluxo de ETL que antes seria manual, entregando análises prontas em Excel sem intervenção humana.

## 🛠 Stack
- Python 3
- Pandas
- Agendador de Tarefas do Windows

## ⚙️ Pipeline
5 CSVs → merge → tratamento de datas → 4 análises → Excel (4 abas)

## 📊 Análises geradas
1. Top 10 categorias que mais vendem
2. Top 10 estados que mais compram
3. Vendas por mês
4. Formas de pagamento

## ⏰ Automação
Script agendado no Agendador de Tarefas do Windows, executando diariamente às 08:00.

## 📂 Arquivos
- `olist_tratado.py` — script principal
- `rodar_olist.bat` — execução agendada
- `analises_olist.xlsx` — saída (4 abas)

## 🔗 Fonte
Kaggle — Brazilian E-Commerce Public Dataset by Olist
