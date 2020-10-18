import re

from .base_validator import BaseValidator
from ..models import BanContent


class BanContentValidator(BaseValidator):
    uid = 'ban_content'
    regex = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"

    def _load_repository(self):
        """Загрузка справочника."""
        return set(BanContent.objects.values_list("value", flat=True))

    def run_check(self, checked_value):
        find_res = re.findall(self.regex, checked_value)
        result = False
        if len(find_res) > 0:
            for site in find_res:
                if site.replace("https://", "").replace("http://", "") in self.repository:
                    result = not result
        return result
