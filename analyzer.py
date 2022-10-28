import logging

from nltk.corpus import PlaintextCorpusReader
from nltk.sentiment import SentimentIntensityAnalyzer


def get_words_from_file(path_root: str, dictionary_name: str) -> list[str]:
    return [elem.lower() for elem in PlaintextCorpusReader(path_root, '.*').words(dictionary_name)]


def get_text_from_file(path_to_file: str) -> str:
    with open(path_to_file, 'r', encoding="utf-8") as file:
        return file.read()


def define_text_mood(processed_data: dict[str, float]) -> str:
    result_mood = {k: processed_data[k] for k in list(processed_data)[:3]}
    return max(result_mood, key=result_mood.get)


def process_sentiment_intensity_analysis(text: str) -> str:
    sia = SentimentIntensityAnalyzer()
    processed_data = sia.polarity_scores(text)
    logging.debug("Text was processed. Common estimation of sentiment: %s", str(processed_data))
    return define_text_mood(processed_data)
