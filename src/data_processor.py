import pandas as pd

def calcular_faturamento(df):
    """Calcula o faturamento total das vendas."""
    return df["Valor_Total"].sum()

def produto_mais_vendido(df):
    """Identifica o produto com maior quantidade vendida."""
    vendas = df.groupby("Produto")["Quantidade"].sum()
    return vendas.idxmax(), vendas.max()

def produto_maior_faturamento(df):
    """Identifica o produto com maior faturamento"""
    vendas = df.groupby("Produto")["Valor_Total"].sum()
    return vendas.idxmax(), vendas.max()

def vendedor_destaque(df):
    """Identifica o vendedor com maior faturamento."""
    vendas = df.groupby("Vendedor")["Valor_Total"].sum()
    return vendas.idxmax(), vendas.max()

def calcular_quantidade_total(df):
    """Calcula a quantidade total de unidades vendidas."""
    return df["Quantidade"].sum()

def faturamento_por_categoria(df):
    """Calcula o faturamento total de cada categoria."""
    faturamento = df.groupby("Categoria")["Valor_Total"].sum()
    return faturamento

def percentual_por_categoria(df):
    """Calcula o percentual de faturamento por categoria."""

    fatur_categ = faturamento_por_categoria(df)
    fatur_total = calcular_faturamento(df)

    percen_categ = (fatur_categ / fatur_total) * 100

    return percen_categ.rename("Percentual")