API Book - API de gerenciamento de livros

- Tecnologias usadas:

SQLAlchemy
Flask migrate
Dynaconf
Marshmallow e Namespaces
Testes unitários com Pytest
Uso de DTO'S
Docker compose

<!-- Como rodar esse projeto -->

export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True
docker-compose up
flask run

<!-- Como fazer as migrações -->

flask db init
flask db migrate
flask db upgrade








