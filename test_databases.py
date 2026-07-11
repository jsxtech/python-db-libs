import unittest
from unittest.mock import patch, MagicMock
import runpy
import sys


class TestSQLite(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_sqlite_connection(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, 'Jaspal', 'jaspal@mail.com')]
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn

        sys.modules.pop('sqlite_example', None)
        runpy.run_module('sqlite_example', run_name='__main__')

        mock_connect.assert_called_once_with(':memory:')
        mock_cursor.execute.assert_called()
        mock_conn.close.assert_called_once()


@unittest.skipUnless(
    __import__('importlib').util.find_spec('psycopg2') is not None,
    'psycopg2 not installed'
)
class TestPostgreSQL(unittest.TestCase):
    @patch('psycopg2.connect')
    def test_postgresql_connection(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn

        sys.modules.pop('postgresql_example', None)
        runpy.run_module('postgresql_example', run_name='__main__')

        mock_connect.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()


@unittest.skipUnless(
    __import__('importlib').util.find_spec('pymysql') is not None,
    'pymysql not installed'
)
class TestMySQL(unittest.TestCase):
    @patch('pymysql.connect')
    def test_mysql_connection(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn

        sys.modules.pop('mysql_example', None)
        runpy.run_module('mysql_example', run_name='__main__')

        mock_connect.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()


@unittest.skipUnless(
    __import__('importlib').util.find_spec('redis') is not None,
    'redis not installed'
)
class TestRedis(unittest.TestCase):
    @patch('redis.Redis')
    def test_redis_operations(self, mock_redis_cls):
        mock_client = MagicMock()
        mock_redis_cls.return_value = mock_client

        sys.modules.pop('redis_example', None)
        runpy.run_module('redis_example', run_name='__main__')

        mock_redis_cls.assert_called_once()
        mock_client.close.assert_called_once()


@unittest.skipUnless(
    __import__('importlib').util.find_spec('pymongo') is not None,
    'pymongo not installed'
)
class TestMongo(unittest.TestCase):
    @patch('pymongo.MongoClient')
    def test_mongo_connection(self, mock_client):
        mock_instance = MagicMock()
        mock_client.return_value = mock_instance

        sys.modules.pop('mongo_example', None)
        runpy.run_module('mongo_example', run_name='__main__')

        mock_client.assert_called_once_with('mongodb://localhost:27017/')
        mock_instance.close.assert_called_once()


if __name__ == '__main__':
    unittest.main()
