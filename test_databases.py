import unittest
from unittest.mock import patch, MagicMock
import sys

class TestSQLite(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_sqlite_connection(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, 'Jaspal', 'jaspal@mail.com')]
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn
        
        import sqlite
        
        mock_connect.assert_called_once_with('test.db')
        mock_cursor.execute.assert_called()
        mock_conn.close.assert_called_once()

class TestPostgreSQL(unittest.TestCase):
    @patch('psycopg2.connect')
    def test_postgresql_connection(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn
        
        import postgresql
        
        mock_connect.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()

class TestMySQL(unittest.TestCase):
    @patch('pymysql.connect')
    def test_mysql_connection(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn
        
        import mysql
        
        mock_connect.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()

class TestRedis(unittest.TestCase):
    @patch('redis.Redis')
    def test_redis_operations(self, mock_redis):
        mock_client = MagicMock()
        mock_redis.return_value = mock_client
        
        import redis as redis_module
        
        mock_redis.assert_called_once()
        mock_client.close.assert_called_once()

class TestMongo(unittest.TestCase):
    @patch('pymongo.MongoClient')
    def test_mongo_connection(self, mock_client):
        mock_instance = MagicMock()
        mock_client.return_value = mock_instance
        
        import mongo
        
        mock_client.assert_called_once_with('mongodb://localhost:27017/')
        mock_instance.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
