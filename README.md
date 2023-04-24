### API_YAMDB

Проект YaMDb собирает отзывы пользователей на произведения.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка».
Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).

### Технологии:
Python 3.7
Django 2.2.16
djangorestframework==3.12.4

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:avnosov3/infra_sp2.git
```

```
cd infra
```

Используем Docker, делаем миграции, создаём юзера, собираем статику:

```
docker-compose up -d --build 
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```


### Проект делали:

Носов Артём https://github.com/avnosov3
Михалицын Андрей https://github.com/misterio92

### Redoc
http://84.201.128.13/redoc/
