import csv
import re
import logging

from jisho_api.word import Word
from jisho_api.kanji import Kanji
from jisho_api.sentence import Sentence
from jisho_api.tokenize import Tokens
from jisho_api import scrape


kanjis = []
kanjisSet = []

# Read the CSV file
# input_file_path = 'generated/jlpt-n1normal.csv'
# output_file_path = 'generated/jlpt-n1Kanji.csv'

input_file_path = 'generated/commonnormal.csv'
output_file_path = 'generated/commonnormal-Kanji.csv'

def getKanjiList(argv=None):
    with open(input_file_path, 'r') as file:
        csv_reader = csv.reader(file)

        # Iterate over each line in the CSV file
        for line in csv_reader:
            # Get the first word in the line
            word = line[0]

            # split the word into individual characters
            characters = list(word)
            pattern = re.compile(r'[\u4e00-\u9fff]')  # Unicode range for Chinese characters
            for item in characters:
                if pattern.search(item):
                    # Add the word to the kanjis list
                    kanjis.append(item)

    kanjisSet = list(set(kanjis))
    # print(kanjisSet)

    # save kanjisSet to a csv file.
    with open(output_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(kanjisSet)

def getKanjiResult(argv=None):
    # eword = Word.request('water')

    cchar = Kanji.request('水')

    sentences = Sentence.request('水')

    # rtokens = Tokens.request('昨日すき焼きを食べました')

    # word_requests = scrape(Word, ['water', 'fire'], './generated/')
    word_requests = scrape(Kanji, ['水', '火'], './generated/')
# logging.info(f"Searching sentence tokens : {word_requests}")


if __name__ == "__main__":
    # getKanjiList()
    getKanjiResult()