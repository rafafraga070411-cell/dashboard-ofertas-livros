"""Leitura e preparação dos dados dos livros.
"""

from pathlib import Path
import csv


PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"


def converter_preco(texto):
    """Converte '£51.77' para 51.77."""
    return float(texto.replace("£", ""))


def converter_nota(texto):
    """Converte a nota escrita em inglês para um número."""
    if texto == "One":
        return 1
    elif texto == "Two":
        return 2
    elif texto == "Three":
        return 3
    elif texto == "Four":
        return 4
    elif texto == "Five":
        return 5
    else:
        return 0


def ler_livros(caminho=CAMINHO_LIVROS):
    """Lê as linhas do arquivo CSV como texto."""
    livros = []

    with open(caminho, encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            livros.append(linha)

    return livros


def preparar_livros(linhas):
    """Converte preço e nota e devolve livros prontos para usar."""
    livros = []

    for linha in linhas:
        livro = {
            "titulo": linha["titulo"],
            "preco": converter_preco(linha["preco"]),
            "nota": converter_nota(linha["nota"]),
            "categoria": linha["categoria"],
            "url": linha["url"],
        }

        livros.append(livro)

    return livros


def carregar_livros(caminho=CAMINHO_LIVROS):
    """Lê o CSV e já devolve os livros convertidos."""
    linhas = ler_livros(caminho)
    return preparar_livros(linhas)


if __name__ == "__main__":
    print("Texto do CSV:      ", ler_livros()[0])
    print("Depois de preparar:", carregar_livros()[0])