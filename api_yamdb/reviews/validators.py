import re
from datetime import datetime

from django.core.exceptions import ValidationError


def validate_year(value):
    year = datetime.now().year
    if value > year:
        raise ValidationError(
            (f'Проверьте дату произведения: {value}.'
             'Кажется оно из будущего'
             f'Текущий год: {year}')

        )
    return value


FINDER = re.compile(r'[^\w.@+-]+')


def validate_username(name):
    if name == 'me':
        raise ValidationError('Имя пользователя "me" запрещено')
    bad_characters = "".join(set(FINDER.findall(name)))
    if bad_characters:
        raise ValidationError(
            f'Недопустимые символы {bad_characters} в имени'
        )
    return name
