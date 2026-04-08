"""Dataset service module"""
import json
from database import get_connection, init_database


class DatasetService:
    """Service for dataset persistence operations"""

    @staticmethod
    def save_dataset(dataset, database_path=None):
        """Persist a dataset row and return the stored record."""
        init_database(database_path)

        name = dataset.get("name")
        description = dataset.get("description")
        source = dataset.get("source")
        payload = dataset.get("payload", dataset)

        payload_json = json.dumps(payload, ensure_ascii=False)

        with get_connection(database_path) as connection:
            cursor = connection.execute(
                """
                INSERT INTO dataset (name, description, source, payload)
                VALUES (?, ?, ?, ?)
                """,
                (name, description, source, payload_json)
            )
            connection.commit()

            return DatasetService.get_dataset_by_id(cursor.lastrowid, database_path)

    @staticmethod
    def list_datasets(database_path=None):
        """Return all saved datasets."""
        init_database(database_path)

        with get_connection(database_path) as connection:
            rows = connection.execute(
                """
                SELECT id, name, description, source, payload, created_at
                FROM dataset
                ORDER BY id DESC
                """
            ).fetchall()

        return [DatasetService._row_to_dict(row) for row in rows]

    @staticmethod
    def get_dataset_by_id(dataset_id, database_path=None):
        """Return a dataset record by id."""
        init_database(database_path)

        with get_connection(database_path) as connection:
            row = connection.execute(
                """
                SELECT id, name, description, source, payload, created_at
                FROM dataset
                WHERE id = ?
                """,
                (dataset_id,)
            ).fetchone()

        if row is None:
            return None

        return DatasetService._row_to_dict(row)

    @staticmethod
    def _row_to_dict(row):
        """Convert a SQLite row into a serializable dictionary."""
        return {
            "id": row["id"],
            "name": row["name"],
            "description": row["description"],
            "source": row["source"],
            "payload": json.loads(row["payload"]),
            "created_at": row["created_at"]
        }