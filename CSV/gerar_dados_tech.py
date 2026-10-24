import pandas as pd
import numpy as np

# Configurando semente de aleatoriedade para reprodutibilidade
np.random.seed(42)

# Configurações do dataset
n_registros = 1000

# Listas de dados para setor de Tecnologia
produtos = [
    'Licença Cloud Enterprise', 'Notebook Pro 15', 'Servidor Rack 2U', 
    'Suporte TI Anual', 'Sistema ERP SaaS', 'Consultoria em Cibersegurança'
]
categorias = {
    'Licença Cloud Enterprise': 'Software / SaaS',
    'Notebook Pro 15': 'Hardware',
    'Servidor Rack 2U': 'Hardware',
    'Suporte TI Anual': 'Serviços',
    'Sistema ERP SaaS': 'Software / SaaS',
    'Consultoria em Cibersegurança': 'Serviços'
}
precos_base = {
    'Licença Cloud Enterprise': 1200.0,
    'Notebook Pro 15': 8500.0,
    'Servidor Rack 2U': 25000.0,
    'Suporte TI Anual': 15000.0,
    'Sistema ERP SaaS': 3500.0,
    'Consultoria em Cibersegurança': 18000.0
}
regioes = ['Sudeste', 'Sul', 'Nordeste', 'Centro-Oeste', 'Norte']
segmentos_cliente = ['Startup', 'PME', 'Corporativo', 'Governo']
status_pagamento = ['Concluído', 'Concluído', 'Concluído', 'Pendente', 'Cancelado']

# Geração dos dados aleatórios
prod_escolhidos = np.random.choice(produtos, n_registros)
qtd_escolhidas = np.random.randint(1, 10, n_registros)

df = pd.DataFrame({
    'ID_Pedido': [f'TECH-{1000+i}' for i in range(n_registros)],
    'Data_Venda': pd.date_range(start='2025-01-01', periods=n_registros, freq='12h'),
    'Produto': prod_escolhidos,
    'Categoria': [categorias[p] for p in prod_escolhidos],
    'Preco_Unitario': [precos_base[p] for p in prod_escolhidos],
    'Quantidade': qtd_escolhidas,
    'Regiao': np.random.choice(regioes, n_registros),
    'Segmento_Cliente': np.random.choice(segmentos_cliente, n_registros),
    'Status_Pagamento': np.random.choice(status_pagamento, n_registros)
})

# Tratamento e Cálculo de Colunas Derivadas (Pandas)
df['Valor_Total'] = df['Preco_Unitario'] * df['Quantidade']
df['Ano_Mes'] = df['Data_Venda'].dt.strftime('%Y-%m')

# Filtrando vendas válidas para o dashboard
df_limpo = df[df['Status_Pagamento'] == 'Concluído'].copy()

# Exportando a base tratada para CSV
df_limpo.to_csv('vendas_tecnologia_tratado.csv', index=False, encoding='utf-8-sig')

print("✅ Base de dados 'vendas_tecnologia_tratado.csv' gerada com sucesso!")