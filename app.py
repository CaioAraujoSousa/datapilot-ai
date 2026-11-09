import streamlit as st
import pandas as pd
import plotly.express as px

from src.data_processor import (
    calcular_faturamento,
    produto_mais_vendido,
    vendedor_destaque,
    calcular_quantidade_total,
    faturamento_por_categoria,
    percentual_por_categoria,
    produto_maior_faturamento,
)

st.set_page_config(
    page_title="DataPilot AI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 DataPilot AI")
st.subheader("Seu assistente inteligente para análise de dados")

st.write("Envie uma planilha CSV para começar sua análise.")

arquivo = st.file_uploader(
    "Selecione sua planilha",
    type=["csv"]
)

if arquivo is not None:
    try:
        df = pd.read_csv(arquivo)

        colunas_necessarias = [
            "Produto",
            "Vendedor",
            "Quantidade",
            "Valor_Total"
        ]

        if not all(coluna in df.columns for coluna in colunas_necessarias):
            st.error("A planilha não possui todas as colunas necessárias.")
        else:
            st.success("Planilha carregada com sucesso!")

            # 1. PROCESSAMENTO DE DADOS (Cálculos) 

            quantidade_total = calcular_quantidade_total(df)
            faturamento = calcular_faturamento(df)
            produto, quantidade = produto_mais_vendido(df)
            vendedor, valor = vendedor_destaque(df)
            produto_faturamento, valor_produto = produto_maior_faturamento(df)
            
            resultado_categoria = faturamento_por_categoria(df)
            percentuais_categoria = percentual_por_categoria(df)
            
            dados_grafico_categoria = (
                percentuais_categoria
                .rename_axis("Categoria")
                .reset_index()
            )
            
            # 2. RENDERIZAÇÃO DA INTERFACE (Visual)
            
            # 1. Prévia dos dados e 2. Tabela de registros
            st.subheader("Prévia dos dados")
            st.dataframe(df, use_container_width=True)

            # 3 e 4. Quantidade total vendida (logo abaixo da prévia)
            st.write(f"**Quantidade total vendida:** {quantidade_total}")
            
            st.divider()

            # 5 e 6. Indicadores de vendas (Quatro cards)
            st.subheader("Indicadores de vendas")
            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Faturamento total", f"R$ {faturamento:,.2f}")
            col2.metric("Produto mais vendido", produto, f"{quantidade} unidades")
            col3.metric("Vendedor destaque", vendedor, f"R$ {valor:,.2f}")
            col4.metric("Produto com maior faturamento", produto_faturamento, f"R$ {valor_produto:,.2f}")

            st.divider()

            # 7 e 8. Faturamento por categoria (Tabela)
            st.write("**Faturamento por categoria:**")
            st.dataframe(
                resultado_categoria.rename("Faturamento").to_frame().style.format(
                    lambda v: f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                ),
                use_container_width=True
            )

            # 9 e 10. Participação do faturamento por categoria (Gráfico de rosca)
            grafico_categoria = px.pie(
                dados_grafico_categoria,
                names="Categoria",
                values="Percentual",
                title="Participação do faturamento por categoria",
                hole=0.5
            )
            grafico_categoria.update_traces(
                textposition="inside",
                texttemplate="%{label}<br>%{percent:.2%}"
            )
            st.plotly_chart(grafico_categoria, use_container_width=True)

            st.divider()

            # 11 e 12. Análise visual das vendas (Gráficos de colunas)
            st.subheader("📊 Análise visual das vendas")

            faturamento_produto = df.groupby("Produto", as_index=False)["Valor_Total"].sum()
            faturamento_vendedor = df.groupby("Vendedor", as_index=False)["Valor_Total"].sum()

            col_grafico1, col_grafico2 = st.columns(2)

            with col_grafico1:
                grafico_produtos = px.bar(
                    faturamento_produto,
                    x="Produto",
                    y="Valor_Total",
                    title="Faturamento por produto",
                    text_auto=True
                )
                st.plotly_chart(grafico_produtos, use_container_width=True)

            with col_grafico2:
                grafico_vendedores = px.bar(
                    faturamento_vendedor,
                    x="Vendedor",
                    y="Valor_Total",
                    title="Faturamento por vendedor",
                    text_auto=True
                )
                st.plotly_chart(grafico_vendedores, use_container_width=True)

    except Exception as erro:
        st.error(f"Não foi possível analisar a planilha: {erro}")