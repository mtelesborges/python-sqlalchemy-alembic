import os

from sqlalchemy import Engine, create_engine

from project.exception import DatabaseUrlRequiredException


def get_engine() -> Engine:
    database_url = os.environ.get('DATABASE_URL')
    if database_url is None or database_url == '':
        raise DatabaseUrlRequiredException(
            'DATABASE_URL is not configured in the environment'
        )

    return create_engine(database_url, echo=True)
