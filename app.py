
import streamlit as st
import pandas as pd
import plotly.express as px

from src.data_processor import (
    calcular_faturamento,
    produto_mais_vendido,
    vendedor_destaque,
    calcular_quantidade_total,
    faturamento_por_categoria,
    percentual_por_categoria
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

            st.subheader("Prévia dos dados")
            st.dataframe(df, use_container_width=True)

            quantidade_total = calcular_quantidade_total(df)

            st.write("Quantidade total vendida:", quantidade_total)

            faturamento = calcular_faturamento(df)
            produto, quantidade = produto_mais_vendido(df)
            vendedor, valor = vendedor_destaque(df)

            resultado_categoria = faturamento_por_categoria(df)

            percentuais_categoria = percentual_por_categoria(df)

            dados_grafico_categoria = (
                percentuais_categoria
                .rename_axis("Categoria")
                .reset_index()
            )

            grafico_categoria = px.pie (
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

            st.plotly_chart(
                grafico_categoria,
                use_container_width=True
            )

            percentuais_categoria = percentual_por_categoria(df)

            dados_grafico_categoria = (
                percentuais_categoria
                .rename_axis("Categoria")
                .reset_index()
            )  
            
            st.write("Faturamento por categoria:")

            st.dataframe(
                resultado_categoria.rename("Faturamento").to_frame().style.format(
                    lambda valor: f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                ),
                use_container_width=True
            )

            st.subheader("Indicadores de vendas")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Faturamento total",
                f"R$ {faturamento:,.2f}"
            )

            col2.metric(
                "Produto mais vendido",
                produto,
                f"{quantidade} unidades"
            )

            col3.metric(
                "Vendedor destaque",
                vendedor,
                f"R$ {valor:,.2f}"
            )
    
            st.divider()

            st.subheader("📊 Análise visual das vendas")

            # Agrupar faturamento por produto
            faturamento_produto = (
                df.groupby("Produto", as_index=False)["Valor_Total"]
                .sum()
            )

            # Agrupar faturamento por vendedor
            faturamento_vendedor = (
                df.groupby("Vendedor", as_index=False)["Valor_Total"]
                .sum()
            )

            col4, col5 = st.columns(2)

            with col4:
                grafico_produtos = px.bar(
                    faturamento_produto,
                    x="Produto",
                    y="Valor_Total",
                    title="Faturamento por produto",
                    text_auto=True
                )

                st.plotly_chart(
                    grafico_produtos,
                    use_container_width=True
                )

            with col5:
                grafico_vendedores = px.bar(
                    faturamento_vendedor,
                    x="Vendedor",
                    y="Valor_Total",
                    title="Faturamento por vendedor",
                    text_auto=True
                )

                st.plotly_chart(
                    grafico_vendedores,
                    use_container_width=True
                )


    except Exception as erro:
        st.error(f"Não foi possível analisar a planilha: {erro}")
