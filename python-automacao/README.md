
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
