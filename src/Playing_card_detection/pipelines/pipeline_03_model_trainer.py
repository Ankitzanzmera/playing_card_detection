import sys
from Playing_card_detection.utils.logger import logger
from Playing_card_detection.utils.exception import CustomException
from Playing_card_detection.config.configuration import ConfigurationManager
from Playing_card_detection.components.model_trainer import ModelTrainer

class ModelTrainerPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(model_trainer_config)
            model_trainer.train()
        except Exception as e:
            raise CustomException(e,sys)
        


STAGE_NAME = "Model Trainer"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info("-"*70)
    except Exception as e:
        raise CustomException(e,sys)