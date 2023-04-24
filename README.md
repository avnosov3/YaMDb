# [API_YAMDB](https://beerdrink.pythonanywhere.com/redoc/)

Проект YaMDb [(документация API)](https://beerdrink.pythonanywhere.com/redoc/) собирает отзывы пользователей на произведения.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка».
Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
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

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:avnosov3/infra_sp2.git
```

```
cd infra
```
Используем docker-compose, делаем миграции, создаём юзера, собираем статику:
```
docker-compose up -d --build 
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
Заполнить БД
docker-compose exec web python manage.py csv
```

## Проект делали
* [Носов Артём](https://github.com/avnosov3)
* [Михалицын Андрей](https://github.com/misterio92)
