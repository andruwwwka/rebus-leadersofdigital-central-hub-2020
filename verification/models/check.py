import re
import string

from verification.models import ObsceneWord, BanContent


class BanContentCheck(object):
    def __init__(self, checked_text):
        self.checked_text = checked_text
    regex = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"

    def check_content(self):
        find_res = re.findall(self.regex, self.checked_text)
        if len(find_res) > 0:
            rkn_content = BanContent.objects.values_list("value", flat=True)
            for site in find_res:
                if site.replace("https://", "").replace("http://", "") in rkn_content:
                    return "НАЙДЕН ЗАПРЕЩЕННЫЙ РКН РЕСУРС"
        return "запрещенные ресурсы не найдены"


class ObsceneWordCheck(object):
    def __init__(self, checked_text):
        self.checked_text = checked_text

    def check_content(self):
        clear_text = ''.join([t for t in self.checked_text if t not in set(string.punctuation)])
        ban_list = ObsceneWord.objects.values('value')
        for word in clear_text.split():
            if word.lower() in [ban['value'] for ban in ban_list]:
                return "НАЙДЕНА НЕЦЕНЗУРНАЯ ЛЕКСИКА"
        return "нецензурная лексика не найдена"
