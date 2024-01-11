import os,sys
from Playing_card_detection.utils.logger import logger
from Playing_card_detection.utils.exception import CustomException
from Playing_card_detection.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self,config:DataValidationConfig) -> None:
        self.config = config
    
    def do_validation(self):
        try:
            validation_status = None
            file_that_exist = os.listdir(self.config.unzip_dir)
            required_files_list = self.config.data_validation_required_file
            for file in required_files_list:
                if file not in file_that_exist:
                    validation_status = False
                    with open(self.config.data_validation_status_file,'w') as f:
                        f.write(f"Validation Status == {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.data_validation_status_file,'w') as f:
                        f.write(f"Validation Status == {validation_status}")
            if validation_status:
                logger.info("Data Validation Succeed")
            else:
                logger.info("Data Validation Failed")
        except Exception as e:
            raise CustomException(e,sys)