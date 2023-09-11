from unittest import TestCase

from sqlalchemy import create_engine, text

from data_setup import setup_data

class DataSetupTests(TestCase):

    def setUp(self):
        self.engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

    def test_runs(self):
       setup_data(self.engine)

    def test_has_some_data(self):
       setup_data(self.engine)
       with self.engine.connect() as conn:
           with self.subTest():
               rs = conn.execute(text("SELECT * FROM table_a"))
               self.assertEqual(len(rs.all()), 1)
           with self.subTest():
               rs = conn.execute(text("SELECT * FROM table_b"))
               self.assertEqual(len(rs.all()), 2)
