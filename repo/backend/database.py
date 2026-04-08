"""Database utilities for dataset persistence."""
from pathlib import Path
import os
import sqlite3


BASE_DIR = Path(__file__).resolve().parent
SCHEMA_PATH = BASE_DIR / "sql" / "dataset.sql"
DEFAULT_DATABASE_PATH = BASE_DIR / "data" / "territorial.db"


def get_database_path(database_path=None):
    """Resolve the configured database path."""
    if database_path:
        return Path(database_path)

    configured_path = os.environ.get("DATABASE_PATH")
    if configured_path:
        return Path(configured_path)

    return DEFAULT_DATABASE_PATH


def get_connection(database_path=None):
    """Create a SQLite connection with row access by column name."""
    resolved_path = get_database_path(database_path)
    resolved_path.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(resolved_path)
    connection.row_factory = sqlite3.Row
    return connection


def init_database(database_path=None):
    """Create the dataset table if it does not already exist."""
    resolved_path = get_database_path(database_path)
    resolved_path.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(resolved_path) as connection:
        with SCHEMA_PATH.open("r", encoding="utf-8") as schema_file:
            connection.executescript(schema_file.read())
        connection.commit()