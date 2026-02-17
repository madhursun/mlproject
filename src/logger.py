import logging
import os
import datetime

LOG_File = f'log_{datetime.datetime.now().strftime("%Y-%m-%d")}.log'

# Create logs folder only
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Create full file path
LOG_File_Path = os.path.join(logs_path, LOG_File)

logging.basicConfig(
    filename=LOG_File_Path,
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

