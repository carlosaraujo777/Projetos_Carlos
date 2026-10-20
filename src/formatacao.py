def formatar_moeda(valor: float) -> str:
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def formatar_numero(valor: float) -> str:
    return f"{valor:,.0f}".replace(",", ".")
