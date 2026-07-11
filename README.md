# python-db-libs

Python database library examples demonstrating connections and basic operations.

## Databases Covered
- SQLite (sqlite3)
- PostgreSQL (psycopg2)
- MySQL (pymysql)
- Oracle (cx_Oracle)
- MongoDB (pymongo)
- Cassandra (cassandra-driver)
- Redis (redis)
- SQLAlchemy (Core & ORM)

## Setup
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage
Each file is a standalone example. Set credentials via environment variables:
```bash
# PostgreSQL
export PG_HOST=localhost
export PG_PORT=5432
export PG_DB=your_database
export PG_USER=your_user
export PG_PASSWORD=your_password

# MySQL
export MYSQL_HOST=localhost
export MYSQL_PORT=3306
export MYSQL_USER=root
export MYSQL_PASSWORD=your_password
export MYSQL_DB=your_database

# Oracle
export ORACLE_HOST=localhost
export ORACLE_PORT=1521
export ORACLE_DB=XEPDB1
export ORACLE_USER=your_user
export ORACLE_PASSWORD=your_password

# MongoDB
export MONGO_HOST=localhost
export MONGO_PORT=27017

# Cassandra
export CASSANDRA_HOST=127.0.0.1
export CASSANDRA_PORT=9042

# Redis
export REDIS_HOST=localhost
export REDIS_PORT=6379
export REDIS_DB=0
```

## Files
| File | Description |
|------|-------------|
| sqlite_example.py | SQLite in-memory example |
| postgresql_example.py | PostgreSQL with psycopg2 |
| mysql_example.py | MySQL with PyMySQL |
| oracle_example.py | Oracle with cx_Oracle |
| mongo_example.py | MongoDB with PyMongo |
| cassandra_example.py | Cassandra with cassandra-driver |
| redis_example.py | Redis operations |
| sqlalchemy_core.py | SQLAlchemy Core (SQLite demo) |
| sqlalchemy_orm.py | SQLAlchemy ORM (SQLite demo) |

## Testing
```bash
python -m pytest test_sqlite_integration.py
python -m pytest test_databases.py
```

## Running Examples
```bash
python sqlite_example.py        # Works out of the box
python sqlalchemy_core.py        # Works out of the box (SQLite)
python sqlalchemy_orm.py         # Works out of the box (SQLite)
```

Note: PostgreSQL, MySQL, Oracle, MongoDB, Cassandra, and Redis examples require their respective database servers running and proper credentials configured via environment variables.

## Notes
- **cx_Oracle deprecation**: The `cx_Oracle` package has been renamed to [`python-oracledb`](https://python-oracledb.readthedocs.io/). The `cx_Oracle` 8.3.0 release is the final version. For new projects, use `import oracledb` instead.
