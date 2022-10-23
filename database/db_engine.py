import configparser
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import config

properties_file = configparser.ConfigParser()
properties_file.read(config.PROPERTIES_PATH)
db_properties = dict(properties_file.items("db"))
comment_column_properties = dict(properties_file.items("comment_columns"))


def init_db_connection() -> scoped_session:
    logging.info("Connecting to database")
    engine = create_engine(f'{db_properties.get("engine")}://'
                           f'{db_properties.get("login")}:'
                           f'{db_properties.get("password")}@'
                           f'{db_properties.get("hostname")}:'
                           f'{db_properties.get("port")}/'
                           f'{db_properties.get("name")}')
    return scoped_session(sessionmaker(bind=engine))
