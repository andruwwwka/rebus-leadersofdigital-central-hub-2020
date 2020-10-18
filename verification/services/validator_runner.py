from .bad_content_validator import BanContentValidator
from .obscene_words_validator import ObsceneWordValidator


class ValidatorRunner:
    validator_classes = [
        ObsceneWordValidator,
        BanContentValidator
    ]

    def __init__(self):
        """Инициализация объектов валидаторов."""
        self.available_validators = []
        for validator in self.validator_classes:
            self.available_validators.append(validator())

    def run(self, checked_value):
        """Прогон проверок значения."""
        result = {}
        for validator in self.available_validators:
            result[validator.uid] = validator.run_check(checked_value)
        return result
