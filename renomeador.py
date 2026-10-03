r"""Renomeia os arquivos de uma pasta, colocando a data da modificação na frente.

    python renomeador.py C:\Users\ph\Downloads fotos
"""

import os
import sys
from datetime import datetime


def renomear(pasta, prefixo=""):
    """Renomeia cada arquivo da pasta para 'prefixoAAAAMMDD_nome.jpg'.

    Devolve quantos foram renomeados.
    """
    nomes = os.listdir(pasta)
    quantos = 0

    for nome in nomes:
        caminho = os.path.join(pasta, nome)

        # pula pastas, so renomeia arquivos
        if os.path.isdir(caminho):
            continue

        quando = os.path.getmtime(caminho)
        dia = datetime.fromtimestamp(quando).strftime("%Y%m%d")

        # separa "foto.jpg" em "foto" e ".jpg"
        base, extensao = os.path.splitext(nome)
        novo = f"{prefixo}{dia}_{base}{extensao}"

        if novo == nome:
            continue

        os.rename(caminho, os.path.join(pasta, novo))
        print(f"{nome}  ->  {novo}")
        quantos += 1

    if quantos == 0:
        print("Nenhum arquivo renomeado.")

    return quantos


if __name__ == "__main__":
    pasta = sys.argv[1] if len(sys.argv) > 1 else "."
    prefixo = sys.argv[2] if len(sys.argv) > 2 else ""

    if not os.path.isdir(pasta):
        print(f"A pasta {pasta!r} nao existe.")
        sys.exit(1)

    renomear(pasta, prefixo)
