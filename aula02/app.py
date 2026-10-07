"""Dashboard de Livros - Aula 2.
"""

import streamlit as st

import dados


def classificar_preco(preco):
    """Classifica o livro por faixa de preço."""
    if preco < 20:
        return "Barato"
    elif preco <= 40:
        return "Médio"
    else:
        return "Caro"


def montar_tabela(livros):
    """Monta uma tabela mais amigável para exibição."""
    tabela = []

    for livro in livros:
        linha = {
            "Título": livro["titulo"],
            "Categoria": livro["categoria"],
            "Nota": "⭐" * livro["nota"],
            "Preço": f"£ {livro['preco']:.2f}",
            "Faixa": classificar_preco(livro["preco"]),
        }

        tabela.append(linha)

    return tabela


def contar_por_faixa(livros):
    """Conta quantos livros existem em cada faixa de preço."""
    contagem = {}

    for livro in livros:
        faixa = classificar_preco(livro["preco"])

        if faixa in contagem:
            contagem[faixa] = contagem[faixa] + 1
        else:
            contagem[faixa] = 1

    return contagem


st.title("📚 Dashboard de Livros - Aula 2")

livros = dados.carregar_livros()

total = len(livros)
preco_medio = sum(livro["preco"] for livro in livros) / total
cinco_estrelas = sum(1 for livro in livros if livro["nota"] == 5)
mais_caro = max(livros, key=lambda livro: livro["preco"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total de livros", total)
col2.metric("Preço médio", f"£ {preco_medio:.2f}")
col3.metric("Livros com 5 estrelas", cinco_estrelas)
col4.metric(
    "Livro mais caro",
    f"£ {mais_caro['preco']:.2f}",
    mais_caro["titulo"],
)

st.subheader("Faixas de preço")

faixas = contar_por_faixa(livros)

col_barato, col_medio, col_caro = st.columns(3)

col_barato.metric("Baratos (< £20)", faixas["Barato"])
col_medio.metric("Médios (£20 a £40)", faixas["Médio"])
col_caro.metric("Caros (> £40)", faixas["Caro"])

st.subheader("Buscar livro")

busca = st.text_input("Digite parte do título")

if busca:
    livros_filtrados = [
        livro
        for livro in livros
        if busca.lower() in livro["titulo"].lower()
    ]
else:
    livros_filtrados = livros

st.dataframe(montar_tabela(livros_filtrados))