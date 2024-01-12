import os
from Playing_card_detection.constants import *
from Playing_card_detection.utils.logger import logger
from Playing_card_detection.utils.common import read_for_yolo,save_yaml,read_yaml_file
from Playing_card_detection.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig,config_filepath = CONFIG_FILEPATH):
        self.config = config
        self.data_ingestion_config = read_yaml_file(config_filepath).data_ingestion

    def __clone_repository__(self):
        os.system("git clone https://github.com/ultralytics/yolov5.git")

    def __get_num_classes__(self):
        nc = read_for_yolo(self.config.dataset_yaml_file,check = "nc")
        return nc
    
    def __custom_yaml_for_yolo__(self,model_name,nc):
        yolo_config = read_for_yolo(f"yolov5/models/{model_name}.yaml")
        yolo_config['nc'] = nc

        save_yaml(f"yolov5/models/custom_{model_name}.yaml",yolo_config)
        logger.info("Successfully saved Custom Yolo Config")
    
    def train(self):
        num_classes = self.__get_num_classes__()
        print(num_classes)
        logger.info("Got the Number of Classes")

        if not "yolov5" in os.listdir(os.getcwd()):
            self.__clone_repository__()
            logger.info("Cloned Yolov5 Repoisitory")
        else:
            logger.info("Already Cloned Yolov5 Repoisitory")

        model_name = self.config.pretrained_model_weight_name.split(".")[0]
        self.__custom_yaml_for_yolo__(model_name = model_name,nc = num_classes)

        ##>>>>>>>>>>>>>>>>>>>>>>> Use Git Bash for following Commands <<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        os.system(f"cp {self.data_ingestion_config.local_data_file} {os.getcwd()}")## Copying Zip to main directory
        os.system(f"unzip data.zip")

        os.system(f"cd yolov5/ && python train.py --img 416 --batch {self.config.BATCH_SIZE} --epochs {self.config.EPOCHS} --data ../data.yaml --cfg ./models/custom_{model_name}.yaml --weights {self.config.pretrained_model_weight_name} --name {model_name}_results --cache")
        logger.info("Training Completed")
        
        os.system(f"cp yolov5/runs/train/{model_name}_results/weights/best.pt yolov5/") ## Copy best.pt to yolov5 directory
        os.system(f"cp yolov5/runs/train/{model_name}_results/weights/best.pt {self.config.root_dir}")
        logger.info("Copied Weights To Artifacts")
        
        os.system("rm -rf train")
        os.system("rm -rf valid")
        os.system("rm -rf data.yaml")
        os.system("rm -rf data.zip")
        os.system("rm -rf yolov5/runs")
