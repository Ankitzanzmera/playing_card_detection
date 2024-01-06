import logging
import os,sys
from datetime import datetime

dir_name = f"{datetime.now().strftime('%d_%m_%y')}"
dir_path = os.path.join(os.getcwd(),"logs",dir_name)
os.makedirs(dir_path,exist_ok=True)

file_name = f"{datetime.now().strftime('%H_%M_%S')}.txt" 
LOG_FILE_PATH = os.path.join(dir_path,file_name)
# print(LOG_FILE_PATH)

logging.basicConfig(
    # filename = LOG_FILE_PATH,
    level= logging.INFO,
    format= '[ %(asctime)s ] - %(lineno)d - %(module)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("Bike_helmet_detection")