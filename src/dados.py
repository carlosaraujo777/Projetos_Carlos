import numpy as np
import pandas as pd

def gerar_dados(n_linhas: int = 300, seed: int = 42) -> pd.DataFrame:
    np.random.seed(seed)

    produtos = ['Licença Cloud Enterprise', 'Notebook Pro 15', 'Servidor Rack 2U', 'Sistema ERP SaaS']
    categorias = {'Licença Cloud Enterprise': 'SaaS', 'Notebook Pro 15': 'Hardware',
                  'Servidor Rack 2U': 'Hardware', 'Sistema ERP SaaS': 'SaaS'}
    precos = {'Licença Cloud Enterprise': 1200, 'Notebook Pro 15': 8500,
              'Servidor Rack 2U': 25000, 'Sistema ERP SaaS': 3500}
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
    return df
