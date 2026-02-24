# Curso FastAPI

Projeto backend desenvolvido com FastAPI, utilizando SQLAlchemy e Alembic para gerenciamento de banco de dados e autenticação via JWT.

## Requisitos

- Python 3.8+
- pip (gerenciador de pacotes do Python)

## Instalação e Configuração

Siga os passos abaixo para configurar e executar o projeto localmente.

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd curso_FastAPI
```

### 2. Configurar o Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto:

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Linux / macOS:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências

Com o ambiente virtual ativado, instale os pacotes necessários:

```bash
pip install -r requirements.txt
```

### 4. Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto e configure suas chaves de segurança:

```env
SECRET_KEY="sua_chave_secreta_aqui"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
> **Nota:** A `SECRET_KEY` deve ser uma string aleatória e segura para a geração dos tokens JWT.

### 5. Configuração do Banco de Dados (Alembic)

O projeto utiliza o Alembic para gerenciar as migrações do banco de dados (SQLite por padrão). Como as migrações e o banco de dados não são enviados para o repositório, você precisará inicializar e gerar a estrutura localmente.

1. Inicialize o ambiente do Alembic (isso criará a pasta `alembic` e o arquivo `alembic.ini`):
   ```bash
   alembic init alembic
   ```
   *(Atenção: verifique se o arquivo `alembic.ini` e `alembic/env.py` estão configurados corretamente com a URL do banco e as metadatas dos modelos da sua aplicação. Caso já existam no repositório, pule este passo).*

2. Gere a migração inicial com base nos modelos existentes (`src/models.py`):
   ```bash
   alembic revision --autogenerate -m "migração inicial"
   ```

3. Aplique a migração para criar o banco de dados (`base_de_dados.db`) e as tabelas:
   ```bash
   alembic upgrade head
   ```

## Executando a Aplicação

Para iniciar o servidor de desenvolvimento, utilize o Uvicorn apontando para a aplicação em `src/main.py`:

```bash
uvicorn src.main:app --reload
```

Acesse a API localmente:
- **Swagger UI (Documentação interativa):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
