import re


class DataAnalysis:

    def __init__(self, file):
        # TODO: set up the necessary instance variables
        self.lang_dict = {}
        self.country_dict = {}
        self.read_data(file)

    def read_data(self, file_name):
        # TODO: read the data and get the counts
        with open(file_name, encoding='utf-8') as f:
            lines = f.readlines()
        LANG_COLUMN = 6
        EMAIL_COLUMN = 3
        lines = [x.strip() for x in lines]
        for i in range(1, len(lines)):
            words = lines[i].split(',')
            language = words[LANG_COLUMN]
            self.lang_dict[language] = self.lang_dict[
                language] + 1 if language in self.lang_dict else 1
            email = words[EMAIL_COLUMN]
            country_code_list = re.findall(r'(?<=\.)[a-z]{2}$', email)
            if country_code_list:
                country_code = country_code_list[0]
                self.country_dict[country_code] = self.country_dict[
                  country_code] + 1 if country_code in self.country_dict else 1

        record_count = len(lines) - 1
        for key in self.lang_dict.keys():
            self.lang_dict[key] = self.lang_dict[key] / record_count
        for key in self.country_dict.keys():
            self.country_dict[key] = self.country_dict[key] / record_count

    # take a number N as an argument and return
    # an N-length list of tuples representing languages
    # and their frequencies in the data, ordered from
    # highest frequency to lowest.
    def top_n_lang_freqs(self, N):
        sequence = sorted(
            self.lang_dict.items(), key=lambda x: x[1], reverse=True)
        return sequence[0:N]

    # take a number N as an argument and return
    # an N-length list of tuples representing country (2-letter)
    # top-level domain identifiers (e.g. 'jp', 'uk', 'cn', 'ca')
    # and their frequencies as email domains the data, ordered
    # from highest frequency to lowest.
    def top_n_country_tlds_freqs(self, N):
        """Process a line of characters"""
        sequence = sorted(
            self.country_dict.items(), key=lambda x: x[1], reverse=True)
        return sequence[0:N]
