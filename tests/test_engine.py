import os
import unittest

from project.engine import get_engine
from project.exception import DatabaseUrlRequiredException


class EngineTestCase(unittest.TestCase):
    def test_engine(self):
        os.environ['DATABASE_URL'] = 'sqlite+pysqlite:///:memory:'
        engine = get_engine()

        self.assertIsNotNone(engine)

    def test_engine_without_database_url(self):
        with self.assertRaises(DatabaseUrlRequiredException):
            os.environ['DATABASE_URL'] = ''
            get_engine()
