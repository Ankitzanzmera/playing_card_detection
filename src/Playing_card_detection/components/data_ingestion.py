import gdown
import os,sys
from zipfile import ZipFile
from Playing_card_detection.utils.exception import CustomException
from Playing_card_detection.utils.logger import logger
from Playing_card_detection.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig) -> None:
        self.config = config
    
    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                gdown.download(self.config.source,self.config.local_data_file,quiet=True)
                logger.info("Zip File Downloaded Successfully")
            else:
                logger.info("Zip File Already Existed")
        except Exception as e:
            raise CustomException(e,sys)
        
    def extract_file(self):
        try:
            if os.path.exists(self.config.unzip_dir):
                logger.info("Zip File Is Already Extracted")
            else:
                with ZipFile(self.config.local_data_file,"r") as zip_ref:
                    zip_ref.extractall(self.config.unzip_dir)
                logger.info("Zip File Extracted Successfully")
        except Exception as e:
            raise CustomException(e,sys)