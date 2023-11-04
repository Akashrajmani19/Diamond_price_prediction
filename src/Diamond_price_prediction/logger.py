import logging 
import os
from datetime import datetime

Log_file = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(),'logs')

os.makedirs(log_path,exist_ok = True)

Log_file_path = os.path.join(log_path,Log_file)

logging.basicConfig(level= logging.INFO,
                    filename = Log_file_path,
                    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")

if __name__ == "main":
    logging.info("Here again i am tesitng")