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


@unittest.skipUnless(
    __import__('importlib').util.find_spec('oracledb') is not None,
    'oracledb not installed'
)
class TestOracle(unittest.TestCase):
    @patch('oracledb.connect')
    @patch('oracledb.makedsn')
    def test_oracle_connection(self, mock_makedsn, mock_connect):
        mock_makedsn.return_value = 'dsn'
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, 'Jaspal', 'jaspal@mail.com')]
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn

        sys.modules.pop('oracle_example', None)
        runpy.run_module('oracle_example', run_name='__main__')

        mock_connect.assert_called_once()
        mock_cursor.execute.assert_called()
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()


@unittest.skipUnless(
    __import__('importlib').util.find_spec('cassandra') is not None,
    'cassandra-driver not installed'
)
class TestCassandra(unittest.TestCase):
    @patch('cassandra.cluster.Cluster')
    def test_cassandra_connection(self, mock_cluster_cls):
        mock_cluster = MagicMock()
        mock_session = MagicMock()
        mock_session.execute.return_value = []
        mock_cluster.connect.return_value = mock_session
        mock_cluster_cls.return_value = mock_cluster

        sys.modules.pop('cassandra_example', None)
        runpy.run_module('cassandra_example', run_name='__main__')

        mock_cluster_cls.assert_called_once()
        mock_session.execute.assert_called()
        mock_session.shutdown.assert_called_once()
        mock_cluster.shutdown.assert_called_once()


@unittest.skipUnless(
    __import__('importlib').util.find_spec('sqlalchemy') is not None,
    'sqlalchemy not installed'
)
class TestSQLAlchemy(unittest.TestCase):
    """These examples run against in-memory SQLite, so run them for real."""

    def test_sqlalchemy_core_runs(self):
        sys.modules.pop('sqlalchemy_core', None)
        # Should execute end-to-end without raising.
        runpy.run_module('sqlalchemy_core', run_name='__main__')

    def test_sqlalchemy_orm_runs(self):
        sys.modules.pop('sqlalchemy_orm', None)
        # Should execute end-to-end without raising.
        runpy.run_module('sqlalchemy_orm', run_name='__main__')


if __name__ == '__main__':
    unittest.main()
