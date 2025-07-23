import logging
import os
from datetime import datetime

# Create log filename with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%H_%Y_%M_%S')}.log"

# Create full path for the log file inside 'logs/' directory
logs_path = os.path.join(os.getcwd(), 'logs')
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Set up logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s %(levelname)s %(message)s",
    level=logging.INFO,
)
