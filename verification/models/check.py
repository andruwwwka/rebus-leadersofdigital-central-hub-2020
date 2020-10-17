import re
import string

from verification.models import ObsceneWord, BanContent


class Check(object):
    def __init__(self, checked_text):
        self.checked_text = checked_text
    regex = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"

    def _ban_content_check(self):
        find_res = re.findall(self.regex, self.checked_text)
        result = False
        if len(find_res) > 0:
            rkn_content = BanContent.objects.values_list("value", flat=True)
            for site in find_res:
                if site.replace("https://", "").replace("http://", "") in rkn_content:
                    result = not result
        return result

    def _obscene_word_check(self):
        result = False
        clear_text = ''.join([t for t in self.checked_text if t not in set(string.punctuation)])
        ban_list = ObsceneWord.objects.values_list("value", flat=True)
        for word in clear_text.split():
            if word.lower() in ban_list:
                result = not result
        return result

    def run_checks(self):
        return {
            "bad_content": self._ban_content_check(),
            "bad_words": self._obscene_word_check()
        }
