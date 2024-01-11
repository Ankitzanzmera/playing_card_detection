import sys
from Playing_card_detection.utils.logger import logger
from Playing_card_detection.utils.exception import CustomException
from Playing_card_detection.config.configuration import ConfigurationManager
from Playing_card_detection.components.data_validation import DataValidation

class DataValidationPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(data_validation_config)
            data_validation.do_validation()
        except Exception as e:
            raise CustomException(e,sys)
        
STAGE_NAME = "Data_Validation"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info("-"*70)
    except Exception as e:
        raise CustomException(e,sys)