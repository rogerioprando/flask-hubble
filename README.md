# flask-hubble

Template para projetos flask.

### virtualenv
Pasta venv-script possui o arquivo de requisitos e o script para criar o ambiente virtual.
Executar esse script para gerar o ambiente virtual e apontar o interpreter (pycharm) para o ambiente virtual que
esta da pasta venv-sandbox. Ou se preferir, dentro de venv-sandbox/bin iniciar o ambiente virtual digitando $ source activate.

## Branches:

### Simple Flask Web Application (simple_flask_app)
\__init\__.py: arquivo que informa ao interpretador que é um diretório python e também instancia o módulo Flask.
views.py: armazena as rotas iniciais do projeto web.
run.py: arquivo no tipo do diretório que chama o método run() da instancia do Flask (que foi criado em \__init\__.py).

### Setting Up Unit Testing Infrastructure (init_unit_test)
Rotina de testes utilizando nose2.

#### Configuring a Flask Application (instance_folder)
Usado uma pasta de instãncia para manipular as configurações da aplicação Flask.
Nessa pasta ficam configuraços do tipo DEBUG, TESTING, SECRET_KEY, SQLALCHEMY_DATABASE_URI, etc.
SECRET_KEY é um paràmetro crítico da aplicaço flask,  usado para encriptar a informação que será 
armazenada para cada cada usurio. Nunca deve ser armazenada em respositórios públicos.
Nesse caso toda vez que um deploy para produção for necessário deve ser criado manualmente.

Criar uma pasta instance e adicionar um arquivo  config.py com as configurações do tpo (DEBUG, SECRET_KEY, etc)
Na criação da instância flask adicionar :
app = Flask(\__name\__, instance_relative_config=True)
app.config.from_pyfile('config.py')
