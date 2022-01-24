from sources import WordStats
import urllib.request

FILE_DATA_TYPE = "file"
URL_DATA_TYPE = "url"
TEXT_DATA_TYPE = "text"


class LogicManager:
    word_stats = None

    def __init__(self):
        self.word_stats = WordStats.WordStats()

    def log_data(self, data, data_type):
        if data_type == FILE_DATA_TYPE:
            return self.log_file_text(data)
        if data_type == URL_DATA_TYPE:
            return self.log_uri_text(data)
        if data_type == TEXT_DATA_TYPE:
            return self.log_text(data)
        print("Invalid data type")
        return False

    def log_file_text(self, file_path):
        try:
            with open(file_path, 'r+') as input_file:
                for line in input_file:
                    self._log_data(line)
            self.word_stats.flush_stats()
        except:
            return False
        return True

    def log_uri_text(self, uri):
        try:
            data_url = urllib.request.urlopen(uri)
            for line in data_url:
                self._log_data(line.decode("utf-8"))
            self.word_stats.flush_stats()
        except:
            return False
        return True

    def log_text(self, text):
        try:
            self._log_data(text)
            self.word_stats.flush_stats()
        except:
            return False
        return True

    def get_word_count(self, word):
        try:
            res = self.word_stats.get_stat(word.lower())
            return res
        except:
            return None

    def _log_data(self, data):
        try:
            self.word_stats.insert_text(data)
        except:
            print("Failed to log data")
            raise