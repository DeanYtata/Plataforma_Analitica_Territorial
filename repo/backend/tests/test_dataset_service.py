"""Tests for dataset persistence"""
import tempfile
from pathlib import Path
import unittest

from services.dataset_service import DatasetService


class DatasetServiceTestCase(unittest.TestCase):
    """Dataset persistence test cases"""

    def test_save_dataset_persists_row(self):
        """Saving a dataset should persist and return the stored record."""
        with tempfile.TemporaryDirectory() as temp_dir:
            database_path = Path(temp_dir) / "territorial_test.db"
            payload = {
                "name": "Dataset de prueba",
                "description": "Inserción manual para validar persistencia",
                "source": "test",
                "payload": {
                    "region": "Norte",
                    "value": 42
                }
            }

            saved_dataset = DatasetService.save_dataset(payload, database_path=database_path)
            datasets = DatasetService.list_datasets(database_path=database_path)

            self.assertIsNotNone(saved_dataset)
            self.assertEqual(saved_dataset["name"], "Dataset de prueba")
            self.assertEqual(len(datasets), 1)
            self.assertEqual(datasets[0]["id"], saved_dataset["id"])
            self.assertEqual(datasets[0]["payload"]["value"], 42)