"""
Run this once after configuring your .env file:

    python init_db.py

It creates the MySQL database (if it doesn't already exist) and all tables
defined by the SQLAlchemy models.
"""
import pymysql
from config.config import Config
from app import create_app
from app.extensions import db
from app import models  # noqa: F401  (ensures models are registered before create_all)


def ensure_database_exists():
    kwargs = {}
    if Config.DB_SSL:
        kwargs["ssl"] = {"ca": Config.DB_SSL_CA} if Config.DB_SSL_CA else {"check_hostname": False}
    connection = pymysql.connect(
        host=Config.DB_HOST,
        port=int(Config.DB_PORT),
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        **kwargs,
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"CREATE DATABASE IF NOT EXISTS `{Config.DB_NAME}` "
                "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
            )
        connection.commit()
        print(f"Database '{Config.DB_NAME}' is ready.")
    finally:
        connection.close()


def create_tables():
    app = create_app()
    with app.app_context():
        db.create_all()
        print("All tables created successfully.")


if __name__ == "__main__":
    try:
        ensure_database_exists()
    except Exception as exc:  # hosted DBs usually already have a database
        print(f"Skipping database creation ({exc}). Using existing database.")
    create_tables()
