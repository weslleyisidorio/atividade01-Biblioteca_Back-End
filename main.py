from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Definir o modelo Livro


class Livro(BaseModel):
    id: int
    titulo: str
    genero: str
    ano: int
    autor: str
    quantidade_de_paginas: int

# Criar uma lista de instâncias de Livro


livros = [
    Livro(
        id=1, titulo="O Senhor dos Anéis", genero="Fantasia", ano=1954,
        autor="J.R.R. Tolkien", quantidade_de_paginas=1000
    ),
    Livro(
        id=2, titulo="Harry Potter", genero="Fantasia", ano=1997,
        autor="J.K. Rowling", quantidade_de_paginas=500
    ),
    Livro(
        id=3, titulo="O Hobbit", genero="Fantasia", ano=1937,
        autor="J.R.R. Tolkien", quantidade_de_paginas=300
    ),
    Livro(
        id=4, titulo="O Pequeno Príncipe", genero="Infantil", ano=1943,
        autor="Antoine de Almeida", quantidade_de_paginas=100
    )
]

# Endpoint para listar todos os livros


@app.get("/livros", status_code=status.HTTP_200_OK)
def listar_livros():
    return livros

# Endpoint para listar um livro específico pelo ID


@app.get("/livros/{id}", status_code=status.HTTP_200_OK)
def listar_livro(id: int):
    for livro in livros:
        if livro.id == id:
            return livro
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Livro não encontrado"
    )

# Endpoint para adicionar um novo livro


@app.post("/livros", status_code=status.HTTP_201_CREATED)
def adicionar_livro(livro: Livro):
    livros.append(livro)
    return livro

# Endpoint para deletar um livro pelo ID


@app.delete("/livros/{id}", status_code=status.HTTP_200_OK)
def deletar_livro(id: int):
    for i in range(len(livros)):
        if livros[i].id == id:
            del livros[i]
            return {"message": "Livro deletado com sucesso"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Livro não encontrado"
    )

# Endpoint para atualizar um livro pelo ID


@app.put("/livros/{id}", status_code=status.HTTP_200_OK)
def atualizar_livro(id: int, livro: Livro):
    for i in range(len(livros)):
        if livros[i].id == id:
            livros[i] = livro
            return livro
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Livro não encontrado"
    )

# Endpoint para listar livros por gênero


@app.get("/livros/genero/{genero}", status_code=status.HTTP_200_OK)
def listar_livros_por_genero(genero: str):
    livros_por_genero = []
    for livro in livros:
        if livro.genero == genero:
            livros_por_genero.append(livro)
#   livros_por_genero = [livro for livro in livros if livro.genero == genero]
    if livros_por_genero == []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Livro não encontrado"
        )

    return livros_por_genero

# Endpoint para listar livros por autor


@app.get("/livros/autor/{autor}", status_code=status.HTTP_200_OK)
def listar_livros_por_autor(autor: str):
    livros_por_autor = []
    for livro in livros:
        if livro.autor == autor:
            livros_por_autor.append(livro)
#   livros_por_autor = [livro for livro in livros if livro.autor == autor]

    if livros_por_autor == []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Livro não encontrado"
        )

    return livros_por_autor

# Endpoint para listar livros por gênero e autor


@app.get("/livros/genero/{genero}/autor/{autor}",
         status_code=status.HTTP_200_OK)
def listar_livros_por_genero_e_autor(genero: str, autor: str):
    livros_por_genero_e_autor = []
    for livro in livros:
        if livro.genero == genero and livro.autor == autor:
            livros_por_genero_e_autor.append(livro)

    if livros_por_genero_e_autor == []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Livro não encontrado"
        )

    return livros_por_genero_e_autor


"""   livros_por_genero_e_autor = [
        livro for livro in livros if livro.genero == genero and
        livro.autor == autor
    ]
    return livros_por_genero_e_autor
"""
