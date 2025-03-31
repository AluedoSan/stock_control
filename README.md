# Sistema de Estoque - Flask

Este é um sistema simples de gerenciamento de estoque desenvolvido com Flask. Ele permite o cadastro, login de usuários e gerenciamento de produtos.

## 🚀 Tecnologias Utilizadas

- Python 3
- Flask
- Flask-Login (Autenticação)
- Flask-SQLAlchemy (Banco de Dados)
- SQLite (Banco de dados leve)
- Poetry (Gerenciamento de dependências)

## 📦 Instalação e Execução

### Pré-requisitos

- Python 3 instalado
- [Poetry](https://python-poetry.org/docs/#installation) instalado

### Passo a passo

1. Clone este repositório:
   ```sh
   git clone https://github.com/AluedoSan/stock_control
   cd stock_control
   ```

2. Instale as dependências com Poetry:
   ```sh
   poetry install
   ```

3. Ative o ambiente virtual do Poetry:
   ```sh
   poetry shell
   ```

4. Crie o banco de dados:
   ```sh
   python -c "from app import db, app; app.app_context().push(); db.create_all()"
   ```

5. Execute a aplicação:
   ```sh
   flask --app main.py run
   ```

6. Acesse no navegador:
   ```
   http://127.0.0.1:5000
   ```

## 🔥 Funcionalidades

- [x] Cadastro e login de usuários  
- [x] Proteção de rotas com autenticação  
- [x] CRUD de produtos (a ser implementado)  
- [ ] Relatórios de estoque (futuro)  

## 🤝 Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests!  
