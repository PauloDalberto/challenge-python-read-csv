# API Oscar Pior Filme - Backend

API RESTful construída com **FastAPI** que lê um arquivo CSV de filmes, armazena os dados em um banco SQLite em memória, e expõe endpoints para analisar os produtores com os maiores e menores intervalos entre vitórias na categoria "Pior Filme".

---

## Funcionalidades

- Carrega dados do arquivo CSV (`movies.csv`) na inicialização da aplicação
- Armazena os dados em banco SQLite em memória usando SQLAlchemy ORM
- Endpoint para obter produtores com intervalos mínimos e máximos entre prêmios consecutivos
- Arquitetura organizada em camadas (models, services, repositories, etc.)
- Testes de integração usando pytest e TestClient

---

## Começando

### Requisitos

- Python 3.9+
- pip

### Instalação

1. Clone o repositório:

```bash
git clone https://github.com/PauloDalberto/challenge-python-read-csv.git

