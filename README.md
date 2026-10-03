# renomeador

Renomeia os arquivos de uma pasta, colocando a data na frente do nome.

## Como usar

```bash
python renomeador.py C:\Users\ph\Downloads fotos
```

```
IMG_2931.jpg     ->  fotos20261003_IMG_2931.jpg
minha foto.png  ->  fotos20261003_minha foto.png
```

O segundo argumento é opcional — sem ele, o nome fica só com a data.

Pastas dentro da pasta são puladas: só arquivos são renomeados.

## Detalhes

Sem dependências externas: roda em qualquer Python 3, sem `pip install`.

A data usada é a de **modificação** do arquivo, não a de criação. É a mais
confiável porque sobrevive a copiar, baixar e mover o arquivo entre pastas.

**Cuidado:** o programa não desfaz. Para testar, use uma pasta de mentira.