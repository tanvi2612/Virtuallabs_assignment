import unittest
from model import Accuracy
from flask_sqlalchemy import SQLAlchemy
from blueprints import db
from sqlalchemy.sql import select
from sqlalchemy import create_engine
engine = create_engine('sqlite:///accuracy.db', echo = True)
class DatabaseTest(unittest.TestCase):
    def test_ids_correct(self):
        x = len(Accuracy.query.all())
        self.assertEqual(x, 32)

    def test_chk_lang(self):
        eng_present = False
        hin_present = False
        y = select([Accuracy])
        conn = engine.connect()
        result = conn.execute(y)
        for row in result:
            if row.language == "English":
                eng_present = True
            if row.language == "Hindi":
                hin_present = True
        assert eng_present and hin_present    
    def test_accuracy(self):
        accurate = True
        y = select([Accuracy])
        conn = engine.connect()
        result = conn.execute(y)
        for row in result:
            if row.accuracy < "50":
                accurate = False
                break
           
        assert accurate    
   

if __name__ == "__main__":
    unittest.main()