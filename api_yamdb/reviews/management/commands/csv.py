import csv

from django.core.management.base import BaseCommand

from reviews.models import (
    Category, Comment, Genre, GenreTitle, Review,
    Title, User
)

CASES = (
    (User, 'users.csv'),
    (Category, 'category.csv'),
    (Genre, 'genre.csv'),
    (Title, 'titles.csv'),
    (Review, 'review.csv'),
    (Comment, 'comments.csv'),
    (GenreTitle, 'genre_title.csv')
)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for table, file in CASES:
            with open(f'static/data/{file}', 'r', encoding='utf8') as f:
                dr = csv.DictReader(f, delimiter=',')
                for row in dr:
                    if file == 'titles.csv':
                        category = Category.objects.get(
                            id=row.pop('category'))
                        table.objects.get_or_create(category=category, **row)
                    elif file == 'genre_title.csv':
                        title = Title.objects.get(id=row.pop('title_id'))
                        genre = Genre.objects.get(id=row.pop('genre_id'))
                        table.objects.get_or_create(
                            title_id=title, genre_id=genre, **row
                        )
                    elif file == 'review.csv':
                        title = Title.objects.get(id=row.pop('title_id'))
                        author = User.objects.get(id=row.pop('author'))
                        table.objects.get_or_create(
                            title=title, author=author, **row
                        )
                    elif file == 'comments.csv':
                        review = Review.objects.get(id=row.pop('review_id'))
                        author = User.objects.get(id=row.pop('author'))
                        table.objects.get_or_create(
                            review=review, author=author, **row
                        )
                    else:
                        table.objects.get_or_create(**row)

                self.stdout.write(f'Таблица {table.__name__} заполнена')
