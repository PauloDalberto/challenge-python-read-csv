# Worst Movie Wins - Backend (FastAPI)

API desenvolvida em Python com FastAPI, responsável por processar arquivos CSV contendo dados de premiações de filmes e disponibilizar estatísticas relevantes sobre os vencedores.

## Tecnologias Utilizadas
 - Python 3.11+
 - FastAPI
 - Uvicorn
 - Pydantic
 - Pytest — Testes automatizados
 - Banco em memória (sem uso de banco de dados externo)
 - Arquitetura em camadas (layers)

## Arquitetura em Camadas
O projeto segue uma estrutura clara e escalável com separação por responsabilidades:

```
├── app/
│   ├── api
│   ├── core
│   ├── models
│   ├── repositories
│   ├── schemas
│   ├── services
│   └── utils
├── csv/
├── tests
└── main.py
```

## Como Executar o Projeto

### Passos

1. Crie um ambiente virtual e ative-o
```
python -m venv venv
source venv/bin/activate    # Linux/macOS
.\venv\Scripts\activate     # Windows
```

2. Instale as dependências
```
pip install -r requirements.txt
```

3. Execute a API com Uvicorn
```
uvicorn main:app --reload
```

## Testes

Padrão utilizado: AAA (Arrange, Act, Assert)

Cada teste é dividido em três etapas:
 - Arrange – configuração e preparação do teste
 - Act – chamada da função ou endpoint
 - Assert – verificação do resultado esperado

Para rodar os testes automatizados, utilize o Pytest:
```
pytest 
```
Os testes cobrem os principais serviços e rotas, garantindo a qualidade do código.

![alt text](image.png)