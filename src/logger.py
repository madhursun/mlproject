import logging
import os
import datetime

# Get project root (go 1 level up from src)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

LOG_File = f'log_{datetime.datetime.now().strftime("%Y-%m-%d")}.log'

logs_path = os.path.join(PROJECT_ROOT, "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_File_Path = os.path.join(logs_path, LOG_File)

logging.basicConfig(
    filename=LOG_File_Path,
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
