class BaseValidator:
    """Базовый класс валидатора.

    Описывает в себе необходимый интерфейс и минимальные проверки.
    """

    uid = None

    def _load_repository(self):
        """Загрузка справочника."""
        raise NotImplementedError

    def __init__(self):
        """Инициализация класса.

        Проверяется наличие идентификатора и происходит прогрузка начальных значений."""

        if not self.uid:
            raise AttributeError('Класс валидатора не имеет уникального идентификатора')
        self.repository = self._load_repository()

    def run_check(self, checked_value):
        raise NotImplementedError
