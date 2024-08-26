import unittest
import pydoc
from urllib.parse import quote_plus
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

class TestDataBaseConnection(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        server = os.getenv('SERVER')
        database = os.getenv('DATABASE')
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')
        driver = os.getenv('DRIVER')
        connection_string = f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'
        engine = create_engine(f'mssql+pyodbc:///?odbc_connect={quote_plus(connection_string)}')
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def test_connection(self):
        result = self.session.execute(text("SELECT 1")).scalar()
        self.assertEqual(result, 1)
        
if __name__ == '__main__':
    unittest.main()