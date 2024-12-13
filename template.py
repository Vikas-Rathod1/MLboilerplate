import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

project_name = "mlProject"

list_of_files = [
    ".github/workflows",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_tranformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/utils.py",
    "tests/unit/__init__.py",
    "test/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "exprement/experiments.ipynb",
    "README.md",
]

def create_files_and_directories():
    for filepath in list_of_files:
        filepath = os.path.join(project_name, filepath)
        filedir, filename = os.path.split(filepath)

        if filedir:
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Directory created: {filedir}")

        if not filename:
            continue

        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                f.write("")  # Create an empty file
                logging.info(f"File created: {filepath}")
        else:
            logging.info(f"File already exists: {filepath}")

if __name__ == "__main__":
    create_files_and_directories()
