import yaml
import os,sys
import base64
from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from Playing_card_detection.utils.exception import CustomException

@ensure_annotations
def create_directories(path_to_dirs: list):
    for path in path_to_dirs:
        os.makedirs(path,exist_ok=True)

@ensure_annotations
def read_yaml_file(path_to_yaml:Path) -> ConfigBox:
    try:
        with open(path_to_yaml,"r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml is Empty")
    except Exception as e:
        raise CustomException(e,sys)
    
def read_for_yolo(filepath:Path,check = None) -> str:
    try:
        if check =='nc':
            with open(filepath,'r') as yaml_file:
                num_classes = int(yaml.safe_load(yaml_file)['nc'])
            return num_classes 
        else:
            with open(filepath,'r') as yaml_file:
                content = yaml.safe_load(yaml_file)
            return content 
    except Exception as e:
        raise CustomException(e,sys)

def save_yaml(path,content):
    try:
        with open(path,'w') as f:
            yaml.dump(content,f)
    except Exception as e:
        raise CustomException(e,sys)
    
def decodeImage(imgstring,filename):
    imgdata = base64.b64decode(imgstring)
    save_directory = "./inference_data/"
    os.makedirs(save_directory,exist_ok= True)
    with open(os.path.join(save_directory,filename),"wb") as file_obj:
        file_obj.write(imgdata)
        file_obj.close

def encodeImageintobase64(croppedImagePath):
    with open(croppedImagePath,"rb") as file_obj:
        return base64.b64encode(file_obj.read())