import argparse
import logging
import os

import analyzer
import config
from database import db_connector
from database import db_engine


def init_argparser():
    parser = argparse.ArgumentParser(description='Define mood of the text.')
    parser.add_argument('--path', '-p', type=str, default=config.PATH_ROOT + config.DATA_PATH + config.FILE_TEXT_NAME,
                        help='Path to the text')
    parser.add_argument('--log-path', '-lp', type=str, default=config.PATH_ROOT + config.LOG_PATH)
    parser.add_argument('--mode', '-m', type=str, default=2,
                        help="Mode to analyze data: "
                             "(1)Analyze text from file "
                             "(2)Analyze data from database")
    return parser.parse_args()


def init_logger(log_path: str):
    if not os.path.isdir(log_path):
        os.mkdir(log_path)
    logging.basicConfig(filename=log_path + 'SentimentAnalyzer.log',
                        filemode='a',
                        format='[%(asctime)s] [%(levelname)s] - %(message)s',
                        level=logging.INFO)


def analyze_data_from_file():
    result = analyzer.process_sentiment_intensity_analysis(analyzer.get_text_from_file(args.path))
    logging.info(result)


def analyze_data_from_database():
    db_session = db_engine.init_db_connection()
    result = db_connector.get_all_unprocessed_body(db_session)
    for row in result:
        logging.debug("Received data by id %d: %s", row["id"], row["body"])
        sentiment = analyzer.process_sentiment_intensity_analysis(row["body"])
        logging.debug("Definition of sentiment: %s", sentiment)
        db_connector.update_unprocessed_data_by_id(sentiment, row["id"], db_session)
    db_session.commit()


def choose_analyze_mode(mode: int):
    if mode == 1:
        analyze_data_from_file()
    if mode == 2:
        analyze_data_from_database()


if __name__ == "__main__":
    args = init_argparser()
    init_logger(args.log_path)
    choose_analyze_mode(args.mode)
