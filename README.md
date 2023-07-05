# [API YAMDB](https://beerdrink.pythonanywhere.com/redoc/)

<details><summary>Russian language</summary>  

Проект YaMDb [(документация API)](https://beerdrink.pythonanywhere.com/redoc/) собирает отзывы пользователей на произведения.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка».
Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство»).
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). 

## Техно-стек
* python 3.7.9
* django 2.2.16
* drf 3.12.4
* drf-simlejwt 4.7.2
* gunicorn 20.0.4
* postgres 13.0
* nginx 1.21.3
* docker 20.10.16
* docker-compose 3.8

## Запуск проекта

1. Клонировать репозиторий
```
git@github.com:avnosov3/YaMDb.git
```
2. Перейти в папку с проектом
```
cd YaMDb
```
3. Создать файл .env в папке infra
```
cd infra
```
```
SECRET_KEY=<указать секретный ключ>
DEBUG=True (если запуск в боевом режиме, то необходимо удалить переменную)

DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=<Указать имя пользователя>
POSTGRES_PASSWORD=<Указать пароль пользователя>
DB_HOST=db
DB_PORT=<Указать порт для подключения к базе>
``` 
4. Запустить docker-compose
```
docker-compose up -d --build
```
5. Создать миграции
```
docker-compose exec web python manage.py migrate
```
6. Создать супер пользователя
```
docker-compose exec web python manage.py createsuperuser
```
7. Собрать статику
```
docker-compose exec web python manage.py collectstatic --no-input
```
8. Заполнить БД
```
docker-compose exec web python manage.py csv
```

## Проект делали
* [Носов Артём](https://github.com/avnosov3)
* [Михалицын Андрей](https://github.com/misterio92)
</details>

<details><summary>English language</summary>  

The YaMDb project [(API documentation)](https://beerdrink.pythonanywhere.com/redoc/) collects user feedback on works.
The works are divided into categories such as "Books", "Films", "Music".
The list of categories can be expanded (for example, you can add the category "Fine Arts").
A work can be assigned a genre from the predefined list (for example, Fairy Tale, Rock or Arthouse).

## Stack
* python 3.7.9
* django 2.2.16
* drf 3.12.4
* drf-simlejwt 4.7.2
* gunicorn 20.0.4
* postgres 13.0
* nginx 1.21.3
* docker 20.10.16
* docker-compose 3.8

## Launch of the project

1. Clone repository
```
git@github.com:avnosov3/YaMDb.git
```
2. Go to the project folder
```
cd YaMDb
```
3. Create .env file in infra folder
```
cd infra
```
```
SECRET_KEY=<Specify secret key>
DEBUG=True (if the launch is in prod mode, then you need to delete the variable)

DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=<Specify username>
POSTGRES_PASSWORD=<Specify password>
DB_HOST=db
DB_PORT=<Specify the port to connect to the database>
``` 
4. Run docker-compose
```
docker-compose up -d --build
```
5. Create migrations
```
docker-compose exec web python manage.py migrate
```
6. Create super user
```
docker-compose exec web python manage.py createsuperuser
```
7. Collect static
```
docker-compose exec web python manage.py collectstatic --no-input
```
8. Fill in the database
```
docker-compose exec web python manage.py csv
```

## Authors
* [Artem Nosov](https://github.com/avnosov3)
* [Andrey Mikhalizin](https://github.com/misterio92)
</details>
