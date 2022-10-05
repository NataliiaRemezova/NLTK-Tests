from nltk.corpus import PlaintextCorpusReader
from nltk.sentiment import SentimentIntensityAnalyzer

PATH_ROOT = "./"
POSITIVE_DICTIONARY_NAME = "positive_dictionary.txt"
NEGATIVE_DICTIONARY_NAME = "negative_dictionary.txt"
FILE_TEXT_NAME = "text.txt"


def get_words_from_file(path_root: str, file_name: str):
    return [elem.lower() for elem in PlaintextCorpusReader(path_root, '.*').words(file_name)]


def get_text_from_file(path_to_file: str):
    with open(path_to_file, 'r') as file:
        return file.read()


def count_input_words_from_list(first_list, second_list):
    counter = 0
    for elem in first_list:
        if elem in second_list:
            counter += 1
    return counter


def compare_counters(first_counter: int, second_counter: int, difference_rate: int):
    if abs(first_counter - second_counter) <= difference_rate:
        return 0
    if first_counter > second_counter:
        return 1
    return -1


def define_mood_of_text(result_of_comparing: int):
    if result_of_comparing == -1:
        return "negative"
    if result_of_comparing == 0:
        return "neutral"
    return "positive"


if __name__ == "__main__":
    enter_number = input("Which dictionary should be used?\n"
                         "(1) User's dictionary\n"
                         "(2) Vador's dictionary\n"
                         "(Any other to quit)\n> ")

    if enter_number == "1":
        text = get_words_from_file(PATH_ROOT, FILE_TEXT_NAME)
        print(text)
        positive_counter = count_input_words_from_list(text, get_words_from_file(PATH_ROOT, POSITIVE_DICTIONARY_NAME))
        negative_counter = count_input_words_from_list(text, get_words_from_file(PATH_ROOT, NEGATIVE_DICTIONARY_NAME))
        print("positive_counter:", positive_counter)
        print("negative_counter:", negative_counter)
        print("the mood of the text is", define_mood_of_text(compare_counters(positive_counter, negative_counter, 10)))

    elif enter_number == "2":
        sia = SentimentIntensityAnalyzer()
        print(sia.polarity_scores(get_text_from_file(PATH_ROOT + FILE_TEXT_NAME)))
    else:
        print("Bye!")
