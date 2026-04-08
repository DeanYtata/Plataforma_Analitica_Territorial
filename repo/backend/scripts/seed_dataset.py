"""Manual dataset seed script."""
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from services.dataset_service import DatasetService


def main():
    """Insert a sample dataset into the configured database."""
    sample_dataset = {
        "name": "Dataset de prueba manual",
        "description": "Registro insertado para validar el guardado",
        "source": "manual-seed",
        "payload": {
            "departamento": "Ejemplo",
            "indicador": "Poblacion",
            "valor": 12345
        }
    }

    saved_dataset = DatasetService.save_dataset(sample_dataset)
    print(f"Dataset guardado con ID {saved_dataset['id']}")


if __name__ == "__main__":
    main()