# ✨ FastAPI Funhouse: Seu Portal para o Backend Mágico! ✨

Bem-vindo(a) ao **FastAPI Funhouse**! Prepare-se para mergulhar em um mundo onde a criação de APIs é tão divertida quanto mágica. Este projeto é um pequeno e encantador backend construído com **FastAPI**, perfeito para quem quer aprender ou ter uma base sólida para suas próximas aventuras.

Aqui, você encontrará tudo o que precisa para construir serviços web modernos, desde a gestão de usuários até a criação de pedidos, tudo isso com a velocidade e a elegância que só o FastAPI pode oferecer!

## 🌟 O que você vai encontrar neste parque de diversões:

*   **Registro e Login de Usuários Encantados**: Crie novas contas e faça login com segurança.
*   **Autenticação Mágica com JWT**: Tokens de acesso e refresh para manter suas sessões seguras e fluidas.
*   **Gestão de Pedidos Flexível**: Crie e gerencie pedidos com facilidade.
*   **Conexão com Banco de Dados Robusta**: Use o SQLAlchemy para conversar com seu banco de dados (SQLite, neste caso!).
*   **Boas Práticas de Código e Documentação**: Tudo cuidadosamente documentado para você entender cada truque de mágica!

## 🚀 Como fazer a mágica acontecer (Setup):

Para que o Funhouse funcione em sua máquina, siga estas etapas:

### Pré-requisitos (Os Ingredientes Mágicos):

Certifique-se de ter instalado:

*   **Python 3.8+** (Recomendamos a versão 3.10 ou superior para a melhor experiência!)
*   **pip** (o gerenciador de pacotes do Python)

### 🪄 Invocando o Projeto:

1.  **Clone este repositório mágico:**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```
    (Lembre-se de substituir `seu-usuario/seu-repositorio.git` pelo caminho real do seu projeto!)

2.  **Crie seu caldeirão virtual (Virtual Environment):**
    É uma boa prática isolar as dependências do projeto.
    ```bash
    python -m venv venv
    ```

3.  **Ative seu caldeirão:**

    *   **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **macOS / Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Instale os Feitiços (Dependências):**
    Com seu caldeirão ativado, instale todas as bibliotecas necessárias:
    ```bash
    pip install -r requirements.txt
    ```

5.  **A Poção Secreta (.env file):**
    Crie um arquivo chamado `.env` na raiz do seu projeto (na mesma pasta do `main.py` e `requirements.txt`). Este arquivo conterá suas chaves secretas.

    ```
    SECRET_KEY="seu_segredo_super_secreto_aqui_e_bem_longo"
    ALGORITHM="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```
    **Lembre-se:** `SECRET_KEY` deve ser uma string longa e aleatória para garantir a segurança dos seus tokens!

### 🔮 Rodando o Show (Executando a Aplicação):

Com tudo configurado, você pode iniciar o servidor Uvicorn:

```bash
uvicorn src.main:app --reload
```

Agora, abra seu navegador e visite `http://127.0.0.1:8000/docs` para ver a interface interativa da API (Swagger UI)!

## 🗺️ Mapa das Rotas Mágicas (Endpoints da API):

Aqui estão alguns dos caminhos que você pode explorar no Funhouse:

*   **`/auth/create-user` (POST)**: Crie um novo usuário mágico.
*   **`/auth/login` (POST)**: Autentique-se e receba seus tokens de acesso e refresh.
*   **`/auth/refresh` (GET)**: Use seu refresh token para obter um novo access token.
*   **`/orders/` (GET)**: Acesse a rota padrão de pedidos.
*   **`/orders/order` (POST)**: Crie um novo pedido encantado.

## 💾 O Grimório do Conhecimento (Base de Dados):

Este projeto usa **SQLAlchemy** para gerenciar a interação com o banco de dados. Ele se conecta a um arquivo SQLite (`base_de_dados.db`), que será criado automaticamente ao interagir com a API (por exemplo, ao criar um usuário).

## 🛡️ Magia de Proteção (Autenticação):

A segurança é levada a sério aqui! Utilizamos **JSON Web Tokens (JWT)** para a autenticação. Após o login, você receberá um `access_token` (de curta duração) e um `refresh_token` (de longa duração). Use o `access_token` para acessar rotas protegidas e o `refresh_token` para emitir novos `access_token` sem precisar fazer login novamente.

## 🤝 Quer Contribuir com a Magia?

Sua ajuda é sempre bem-vinda! Se você tem alguma ideia para melhorar o Funhouse, encontrou um bug ou quer adicionar um novo truque, sinta-se à vontade para:

1.  Fork o repositório.
2.  Crie uma nova branch (`git checkout -b feature/sua-feature-magica`).
3.  Faça suas alterações e commite-as (`git commit -m 'feat: Adiciona novo truque de mágica'`).
4.  Envie para a branch (`git push origin feature/sua-feature-magica`).
5.  Abra um Pull Request!

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes. (Se você não tiver um, pode criar um!).
