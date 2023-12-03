import os
import unittest

from alembic import command
from alembic.config import Config
from sqlalchemy.orm import Session

from project.engine import get_engine
from project.models import Address, User


class MigrateTablesTestCase(unittest.TestCase):
    def test_migrate(self):
        if os.path.exists('test.sqlite'):
            os.remove('test.sqlite')

        os.environ['DATABASE_URL'] = 'sqlite:///test.sqlite?mode=memory'

        configuration = Config('./../project/alembic.ini')
        configuration.set_main_option(
            'script_location', './../project/alembic'
        )

        command.upgrade(configuration, 'head')

        engine = get_engine()

        with Session(engine) as session:
            users = session.query(User).all()
            address = session.query(Address).all()

            self.assertIsNotNone(users)
            self.assertIsNotNone(address)
