"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st
import dados

livros = dados.ler_livros()

st.title("📚 Dashboard de Livros")
st.write("Se você está vendo esta página, o seu ambiente está pronto! 🎉")

total = len(livros)

soma = 0
for livro in livros:
    preco = float(livro["preco"].replace("£", ""))
    soma += preco
preco_medio = soma / total

cinco_estrelas = sum(1 for livro in livros if livro["nota"] == "Five")

mais_caro = max(livros, key=lambda l: float(l["preco"].replace("£", "")))
preco_mais_caro = mais_caro["preco"]
titulo_mais_caro = mais_caro["titulo"]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de livros", total)
col2.metric("Preço médio", f"£{preco_medio:.2f}")
col3.metric("Livros com 5 estrelas", cinco_estrelas)
col4.metric("Livro mais caro", preco_mais_caro, titulo_mais_caro)

st.dataframe(livros)