import string

from .base_validator import BaseValidator
from ..models import ObsceneWord


class ObsceneWordValidator(BaseValidator):
    uid = 'bad_words'

    def _load_repository(self):
        """Загрузка справочника."""

        return set(ObsceneWord.objects.values_list('value', flat=True))

    def run_check(self, checked_value):
        result = False
        clear_text = ''.join([t for t in checked_value if t not in set(string.punctuation)])
        for word in clear_text.split():
            if word.lower() in self.repository:
                result = not result
        return result
