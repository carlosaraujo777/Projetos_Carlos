🤖 Automação com Python
Sobre
Script em Python que lê 5 arquivos CSV do dataset público do Olist (e-commerce brasileiro), faz a reserva das tabelas, gera análises e salva no Excel — tudo automaticamente .

🛠 Tecnologias
Python 3
Pandas
Agendador de Tarefas do Windows
📊 O que ele faz
Lê 5 CSVs (pedidos, clientes, itens, produtos, pagamentos)
Juntar todas as tabelas em uma só (merge)
Gera 4 análises:
Top 10 categorias que mais vendem
Top 10 estados que mais compram
Vendas por mês
Formas de balanceamento
Salvar tudo no Excel com 4 abas
⏰ Como roda
O script está agendado no Agendador de Tarefas do Windows e roda automaticamente todos os dias às 08:00 .

📂 Arquivos
olist_tratado.py— script Python
rodar_olist.bat— arquivo de execução
analises_olist.xlsx— resultado gerado (4 abas)
🔗 Fonte dos dados
Kaggle - Conjunto de dados públicos de comércio eletrônico brasileiro por Olist
