from .base_validator import BaseValidator
from ..models import BanContent


class BanContentValidator(BaseValidator):
    uid = 'ban_content'
    regex = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"

    def _load_repository(self):
        """Загрузка справочника.

        set - потому что он на хэш таблица и проверка на вхождение в него самая быстрая
        """
        return set(BanContent.objects.values_list("value", flat=True))

    def run_check(checked_value):
        """Тут уже описывай логику."""
