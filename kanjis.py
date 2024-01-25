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

    # cchar = Kanji.request('哀')

    # sentences = Sentence.request('水')

    # rtokens = Tokens.request('昨日すき焼きを食べました')

    # word_requests = scrape(Word, ['water', 'fire'], './generated/')
    word_requests = scrape(Kanji, ['哀', '火'], './generated/')
    # logging.info(f"Searching sentence tokens : {word_requests}")

    eword = Word.request('哀愁')


def getKanjiResultExtended(argv=None):
    # eword = Word.request('water')

    # cchar = Kanji.request('哀')

    # sentences = Sentence.request('水')

    # rtokens = Tokens.request('昨日すき焼きを食べました')

    # word_requests = scrape(Word, ['water', 'fire'], './generated/')
    word_requests = scrape(Kanji, ['哀', '火'], './generated/')
    # logging.info(f"Searching sentence tokens : {word_requests}")

    eword = Word.request('哀愁')
    sentences1 = Sentence.request('呼び水')
    sentences2 = Sentence.request('水揚げ')
    sentences3 = Sentence.request('飲み水')
    sentences4 = Sentence.request('水位')
    sentences5 = Sentence.request('用水')
    sentences6 = Sentence.request('浄水')

if __name__ == "__main__":
    # 获取N５−N1的单个汉字并生成csv文件。
    # getKanjiList()　　

    ###
    # 从获取的N5-N1的单字生成每个单字的json文件，并将这些单字按照N5-N1再生成anki的note。
    # 这种note再生成汉字单字的学习卡，卡片包含音读及音读组词、训读和训读组词。每个词都是振り仮名。
    ###
    getKanjiResult()

    ###
    # 从获取的N5-N1的单字生成每个单字的json文件，并将这些单字按照N5-N1再生成anki的note。
    # 这种note再生成汉字单字的学习卡，卡片包含音读及音读组词、训读和训读组词。每个词都是振り仮名。每个词都有例句。
    ###
    getKanjiResultExtended()

