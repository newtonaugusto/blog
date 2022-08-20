# Usuário para acessar os artigos:

user: admin@admin.com.br
password: @Senha@!


# Para testar os endpoints:

python manage.py tests


# Blog
python manage.py makemigrations 
python manage.py migrate --run-syncdb


# Run server
pipenv shell
python manage.py runserver


# Run server em rede externa
python manage.py runserver 0.0.0.0:8000

# .env
DB_ENGINE=django.db.backends.postgresql_psycopg2
DB_NAME=blog
DB_USER=postgres
DB_PASS=mcafee123
DB_HOST=localhost
DB_PORT=5432

DEBUG=on
SECRET_KEY='django-insecure-21o3d7v9iyhki4su%3vcvwuidm8mclc%(l(8boec@j&0niq)_0'