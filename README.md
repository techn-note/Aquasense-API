# AquaSense API

## Visão Geral

A **AquaSense API** foi desenvolvida para coletar, gerenciar e fornecer dados de sistemas de **piscicultura em ciclo fechado**. Este método de criação de peixes em ambientes controlados permite um monitoramento contínuo das condições da água, como pH, temperatura, para garantir a saúde dos peixes e a eficiência do sistema de cultivo.

A API é integrada ao sistema, que exibe os dados em um dashboard interativo, oferecendo **alertas** e **recomendações** baseadas nas condições do tanque, ajudando o usuário a otimizar o ambiente aquático.

## Funcionalidades

- Cadastro de tanques, espécies de peixes e sensores de monitoramento.
- Coleta de dados dos sensores (pH, temperatura, oxigênio).
- Geração de alertas e recomendações baseadas nas condições da água.
- API REST para integração com a plataforma desktop e outros sistemas.
- Autenticação e autorização com JWT.

## Tecnologias Utilizadas

- **Flask**: Framework para a construção de aplicações web.
- **MongoDB com PyMongo**: Para armazenar os dados dos tanques e monitoramento.
- **Flask-Marshmallow**: Para serialização e validação de dados.
- **Flask-Bcrypt**: Para criptografia de senhas.
- **Flask-JWT-Extended**: Para autenticação segura baseada em tokens.
- **Postman**: Para testar a API durante o desenvolvimento.

## Instalar e rodar o projeto

Rodar a AquaSense API em sua máquina local é uma tarefa simples.

### Dependências globais

Você precisa ter as seguintes dependências instaladas:

- Python 3.8+
- MongoDB (local ou em MongoDB Atlas)

### Dependências locais

Com o repositório clonado e as dependências globais instaladas, você pode configurar o ambiente virtual e instalar as dependências locais do projeto:

1. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   ```

2. Ative o ambiente virtual:

   - No Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - No Linux/MacOS:
     ```bash
     source venv/bin/activate
     ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

### Rodar o projeto

Para rodar o projeto localmente, siga os passos abaixo:

1. Execute o servidor sem Debugger:

   ```bash
   flask run
   ```

1. Execute o servidor com Debugger:

   ```bash
   Python ./app.py
   ```

3. Acesse a API em `http://localhost:5000`.

### Cadastro e Login de usuários

No ambiente de desenvolvimento, você pode criar usuários manualmente ou utilizar usuários pré-cadastrados.

#### Criar um usuário manualmente

1. Após subir os serviços, acesse `http://localhost:5000/register`.
2. Preencha os dados e utilize **qualquer email** com formato válido.
3. Com a conta criada, realize o login em `http://localhost:5000/login`.

#### Utilizar usuários pré-cadastrados

Para conveniência, você pode configurar usuários pré-cadastrados em seu banco de dados local. Use a API para injetar usuários ou diretamente insira no banco MongoDB.

## Endpoints Principais

- **POST /register**: Criação de usuários.
- **POST /login**: Autenticação de usuários.
- **POST /tanks**: Criação de tanques de piscicultura.
- **GET /sensors**: Coleta de dados dos sensores.
- **GET /recommendations**: Recomendação baseada nos dados de monitoramento.

## Contribuidores

Agradecimentos especiais aos seguintes contribuidores:

- **@Rodrigo Silva** - Desenvolvedor Back-End
- **@Eliharison** - Desenvolvedor Full-stack
- **@Eder Tashiro** - Desenvolvedor IoT