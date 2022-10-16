import os

import analyzer
import argparse
import config
import logging


def init_argparser():
    parser = argparse.ArgumentParser(description='Define mood of the text.')
    parser.add_argument('--path', '-p', type=str, default=config.PATH_ROOT + config.DATA_PATH + config.FILE_TEXT_NAME,
                        help='Path to the text')
    parser.add_argument('--log-path', '-lp', type=str, default=config.PATH_ROOT + config.LOG_PATH)
    return parser.parse_args()


def init_logger(log_path: str):
    if not os.path.isdir(log_path):
        os.mkdir(log_path)
    logging.basicConfig(filename=log_path + 'SentimentAnalyzer.log',
                        filemode='w',
                        format='[%(asctime)s] [%(levelname)s] - %(message)s',
                        level=logging.INFO)


if __name__ == "__main__":
    args = init_argparser()
    init_logger(args.log_path)
    print(analyzer.process_sentiment_intensity_analysis(analyzer.get_text_from_file(args.path)))
