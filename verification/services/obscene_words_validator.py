from .base_validator import BaseValidator
from ..models import ObsceneWord


class ObsceneWordValidator(BaseValidator):
    uid = 'bad_words'

    def _load_repository(self):
        """Загрузка справочника.

        set - потому что он на хэш таблица и проверка на вхождение в него самая быстрая
        """

        return set(ObsceneWord.objects.values_list('value', flat=True))

    def run_check(checked_value):
        """Тут уже описывай логику."""
