### Python env

Criar o ambiente env python

```
 python3 -m venv env
```

Ativar o ambiente Python

```
source env/bin/activate
```

### Instalar dependências da API

Primeira opção:

```
pip install bcrypt cryptography fastapi python-jose python-multipart SQLAlchemy uvicorn passlib python-dotenv psycopg2-binary
```

Segunda opção:

```
pip install -r requirements.txt

```
## Erros

Pode existir um erro ao usar a biblioteca psycopg, comando para instalar individualmente.

```
pip install psycopg2-binary
```

Pode existir um erro ao usar a biblioteca pydantic email, comando para instalar individualmente.

```
pip install "pydantic[email]"
```

Pode existir um erro na versão 5.0.0 do bycrypt, é recomendado o uso da 4.0.1

```
pip install bcrypt==4.0.1
```

## Outros comandos

# instalar caso necessario

```
pip install sqlalchemy psycopg2-binary python-dotenv
```

```
pip install requests
```

## Rodar o projeto

```
uvicorn app.main:app --reload --port 8001
```