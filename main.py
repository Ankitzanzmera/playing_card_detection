import sys
from Playing_card_detection.utils.logger import logger
from Playing_card_detection.utils.exception import CustomException
from Playing_card_detection.pipelines.pipeline_01_data_ingestion import DataIngestionPipeline


STAGE_NAME = "Data_Ingestion"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info("-"*70)
    except Exception as e:
        raise CustomException(e,sys)