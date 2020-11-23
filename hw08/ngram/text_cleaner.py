import re


class TextCleaner:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename, 'r', encoding='utf8') as file:
            content = file.read().strip().lower()
            content = content.replace(',', ' COMMA')
            content = re.sub("[-()\"]", " ", content)
            content = re.sub(" +", " ", content)
            contents = re.split("(?<!mr)[.\n]", content)
            contents = [c.strip() for c in contents if c]
        return contents



