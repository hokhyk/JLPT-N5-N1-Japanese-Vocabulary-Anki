import csv
import re

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


if __name__ == "__main__":
    getKanjiList()
