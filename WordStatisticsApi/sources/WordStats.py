import os
import sys
from collections import defaultdict
import re
import pickle

STATS_FILE = "../data/WordStatsData.pkl"


class WordStats:
    word_count = defaultdict(int)

    def __init__(self):
        self.stats_file_path = os.path.join(sys.path[0], STATS_FILE)

        if not os.path.isfile(self.stats_file_path):
            with open(self.stats_file_path, 'wb+') as open_file:
                pickle.dump(self.word_count, open_file)
        else:
            try:
                with open(self.stats_file_path, 'rb+') as open_file:
                    self.word_count = pickle.load(open_file)
            except:
                print("Statistics file not found and server failed to create one. Exiting..")
                exit(1)

    def insert_text(self, text):
        for word in re.split(r'\W|\d', text):
            if word:
                self.word_count[word.lower()] += 1

    def flush_stats(self):
        try:
            with open(self.stats_file_path, 'wb+') as open_file:
                pickle.dump(self.word_count, open_file)
        except:
            print("Error: failed to save the data")
            raise

    def get_stat(self, word):
        return self.word_count[word]
