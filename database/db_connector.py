import logging

import sqlalchemy.orm
from sqlalchemy import text

from database.db_engine import db_properties, comment_column_properties


def get_all_unprocessed_body(db_session: sqlalchemy.orm.scoped_session):
    query = (f"SELECT {comment_column_properties.get('id')}, "
             f"{comment_column_properties.get('body')} "
             f"FROM {db_properties.get('table')} "
             f"WHERE {comment_column_properties.get('sentiment')} = '' OR "
             f"{comment_column_properties.get('sentiment')} = NULL")
    logging.info("Trying to get all unprocessed comments from data base; Query: %s", query)
    return db_session.execute(text(query))


def update_unprocessed_data_by_id(sentiment_estimation: str, message_id: int, db_session: sqlalchemy.orm.scoped_session):
    query = (f"UPDATE {db_properties.get('table')} "
             f"SET {comment_column_properties.get('sentiment')} = '{sentiment_estimation}' "
             f"WHERE {comment_column_properties.get('id')} = {message_id}")
    logging.info("Trying to update estimation of sentiment by id; Query: %s", query)
    db_session.execute(query)
    logging.info("Update was successfully completed")
