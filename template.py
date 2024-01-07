import os
import logging
from pathlib import Path

logging.basicConfig(level= logging.INFO,format = '[ %(asctime)s ] : %(message)s')

project_name = "Playing_card_detection"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/utils/exception.py",
    f"src/{project_name}/utils/logger.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/pipelines/__init__.py",
    "notbooks/trials.ipynb",
    "app.py",
    "setup.py",
    "main.py",
    "requirements.txt",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    dirname,filename = os.path.split(filepath)

    if dirname != "":
        os.makedirs(dirname,exist_ok=True)
        logging.info(f"Directory created {dirname}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"File created {filepath}")
    else:
        logging.info("file already exists")