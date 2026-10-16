# Daily Diet API

API REST desenvolvida com Flask para cadastrar, consultar, atualizar e excluir refeições, permitindo acompanhar se cada refeição está dentro ou fora da dieta.

## Tecnologias

- Python
- Flask 2.3.0
- Flask-SQLAlchemy 3.1.1
- PyMySQL 1.1.0
- Werkzeug 2.3.0

## Funcionalidades

- Criar uma refeição
- Listar todas as refeições
- Consultar uma refeição pelo ID
- Atualizar uma refeição
- Excluir uma refeição
- Registrar data e hora da refeição automaticamente
- Informar se a refeição está dentro da dieta

## Estrutura do projeto

```text
.
├── app.py
├── database.py
├── model/
│   └── refeicao.py
├── requirements.txt
└── .gitignore
```

## Pré-requisitos

- Python 3.10 ou superior
- MySQL ou outro banco compatível com a URL configurada no SQLAlchemy
- `pip`

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/laeciojn/daily-diet-api.git
   cd daily-diet-api
   ```

2. Crie e ative um ambiente virtual:

   **Linux/macOS:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   **Windows (PowerShell):**

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua-chave-secreta
DATABASE_URL=mysql+pymysql://usuario:senha@localhost:3306/daily_diet
```

A aplicação utiliza as variáveis `SECRET_KEY` e `DATABASE_URL` para configurar o Flask e a conexão com o banco de dados.

## Executando a aplicação

```bash
python app.py
```

Por padrão, o servidor Flask é iniciado em modo de desenvolvimento. A API ficará disponível em:

```text
http://127.0.0.1:5000
```

## Endpoints

### Criar refeição

`POST /refeicao`

Corpo da requisição:

```json
{
  "nome": "Almoço",
  "descricao": "Arroz, feijão, frango e salada",
  "dentroDaDieta": true
}
```

### Listar refeições

`GET /refeicao`

### Consultar uma refeição

`GET /refeicao/<id_refeicao>`

Exemplo:

```text
GET /refeicao/1
```

### Atualizar refeição

`PUT /refeicao/<id_refeicao>`

Corpo da requisição:

```json
{
  "nome": "Jantar",
  "descricao": "Omelete e salada",
  "dentroDaDieta": true
}
```

### Excluir refeição

`DELETE /refeicao/<id_refeicao>`

Exemplo:

```text
DELETE /refeicao/1
```

## Modelo de dados

Cada refeição possui os seguintes campos:

| Campo | Tipo | Descrição |
| --- | --- | --- |
| `id` | Integer | Identificador único da refeição |
| `nome` | String | Nome da refeição, com até 30 caracteres |
| `descricao` | String | Descrição da refeição, com até 80 caracteres |
| `data_refeicao` | DateTime | Data e hora de criação da refeição |
| `dentroDaDieta` | Boolean | Indica se a refeição está dentro da dieta |

## Testando com cURL

Criar uma refeição:

```bash
curl -X POST http://127.0.0.1:5000/refeicao \
  -H "Content-Type: application/json" \
  -d '{"nome":"Café da manhã","descricao":"Pão, ovos e café","dentroDaDieta":true}'
```

Listar as refeições:

```bash
curl http://127.0.0.1:5000/refeicao
```

## Status do projeto

Projeto em desenvolvimento.

## Licença

Nenhuma licença foi definida para este repositório até o momento.
