import pandas as pd

def calcular_kpis(df: pd.DataFrame) -> dict:
    faturamento_total = df['Faturamento'].sum()
    qtd_total = df['Quantidade'].sum()
    ticket_medio = faturamento_total / max(len(df), 1)
    return {
        'faturamento_total': faturamento_total,
        'qtd_total': qtd_total,
        'ticket_medio': ticket_medio,
    }

def faturamento_por_regiao(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby('Regiao', as_index=False)['Faturamento']
          .sum()
          .sort_values('Faturamento', ascending=False)
    )

def resumo_por_regiao_categoria(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby(['Regiao', 'Categoria'], as_index=False).agg({
        'Quantidade': 'sum',
        'Faturamento': 'sum'
    })
