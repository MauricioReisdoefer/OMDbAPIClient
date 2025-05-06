# 🎬 OMDbAPIClient

Uma API para gerenciamento e consulta de obras audiovisuais (filmes e séries), unificadas como "Pieces".

## 📌 Tecnologias usadas

- Python 3.11+
- Flask
- SQLAlchemy
- PostgreSQL

## 🚀 Como executar

### Para Rodar ###
pip install -r requirements.txt 

### Sobre o Banco ###
As informações do banco de dados estão no db.env, ignorados por conta do gitignore. 

## Código ##

### Principais Funções ###

- [routes.py] CreateMovie(data) -> Adiciona o filme / série no Banco de Dados
- [routes.py] GetPieceByTitle(title) -> Encontra o filme / série no Banco de Dados por título
- [routes.py] GetPieceByID(id) -> Encontra o filme / série no Banco de Dados pelo IMDb_ID

- [service.py] GetPieceByID(id) -> Procura pelo filme / série na API do OMDb pelo IMDb_ID
- [service.py] GetPieceByTitle(title) -> Procura pelo filme / série na API do OMDb pelo título

### Funcionamento ###

No App.py, cria os caminhos para as requests do Flask. Quando chama o GetPieceByTitle ou ByID do routes.py ele vai procurar no banco de dados por aquela série / filme. Caso não achar, faz a requisição para o serivce.py (GetPieceByID ou GetPieceByTitle), se houver retorna, armazena no banco de dados e retorna para o usuário. Caso contrário retorna que não houve filme / série encontrada.
