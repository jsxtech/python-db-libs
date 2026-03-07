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
pip install psycopg2-binary pymysql pymongo cassandra-driver redis sqlalchemy cx_Oracle
```

## Usage
Each file is a standalone example. Set credentials via environment variables:
```bash
export DB_USER=your_user
export DB_PASSWORD=your_password
export DB_HOST=localhost
```

## Testing
```bash
python test_sqlite_integration.py
```

## Running Examples
```bash
python sqlite.py  # Works out of the box
```

Note: Other examples require database servers running and proper credentials configured.