import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)  # Correct variable name

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s -%(message)s",  # Correct format, removed extra %
    level=logging.INFO,
)  # Added closing parenthesis

'''

if __name__ == "__main__":

    try:
        a=1/10
    except:
        logging.info("Logging has started")
        raise CustomException   
        
'''