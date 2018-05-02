# flask-hubble

Template para projetos flask.

Template baseado no tutorial de: http://www.patricksoftwareblog.com/flask-tutorial/

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

### Configuring a Flask Application (instance_folder)
Usado uma pasta de instãncia para manipular as configurações da aplicação Flask.
Nessa pasta ficam configuraços do tipo DEBUG, TESTING, SECRET_KEY, SQLALCHEMY_DATABASE_URI, etc.
SECRET_KEY é um paràmetro crítico da aplicaço flask,  usado para encriptar a informação que será 
armazenada para cada cada usurio. Nunca deve ser armazenada em respositórios públicos.
Nesse caso toda vez que um deploy para produção for necessário deve ser criado manualmente.

Criar uma pasta instance e adicionar um arquivo  config.py com as configurações do tpo (DEBUG, SECRET_KEY, etc)
Na criação da instância flask adicionar :
app = Flask(\__name\__, instance_relative_config=True)
app.config.from_pyfile('config.py')


### Using Blueprints to Organize your Application (add_blueprints)
Blueprints é um ótimo método para organizar a aplicação Flask. Existem diversas formas de usar Blueprints para
estruturar o código, duas recomendadas são funcional e divisional e podem ser vistas [aqui](http://exploreflask.readthedocs.io/en/latest/blueprints.html#where-do-you-put-them).
Aqui vamos implementar dois blueprints.
users: responsavel por login/logout, administração do usuário
core: parte separada do projeto a ser desenvolvida posteriormente

Os arquivos views.py dentro de cada diretório blueprint precisa configurar o blueprint.
ex: core_blueprint = Blueprint('core', \__name\__, template_folder='templates')
core_blueprint é um objector configurado de Blueprint e usado para definiar as rotas por meio de @core_blueprint.route()
Também será usado na configuração geral de Blueprints na aplicação Flask.
O mesmo deve ser feito para cada Blueprint que desejar criar (users, core até o momento).
Após adicionados os Blueprints é necessário que a aplicação Flask saiba desses Blueprints. Isso será feito
no arquivo \__init\__.py no diretorio do projeto.

### Database using PostgreSQL and SQLAlchemy (add_database)
Arquivo config.py recebe as configurações do banco.
SQLALCHEMY_DATABASE_URI: endereço URI (Identificador de Recursos Universal)
SQL irá acompanhar as modificações.
SQLALCHEMY_TRACK_MODIFICATIONS = True
O módulo SQLAlchemy é importado no \__init\__.py. Ao instanciá-lo é passado o objeto flask (app).
db = SQLAlchemy(app)

Criar um arquivo modelo (como é chamado no flask a estrutura da nossa tabela do banco de dados).
project/models.py
No models ficam as estruturas da tabelas do banco de dados.

Para testar a inserção, usar db_create.py (arquivo temporário, será removido)



