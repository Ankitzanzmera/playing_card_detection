import os,sys
from flask import Flask, request, jsonify, render_template, Response
from flask_cors import cross_origin, CORS 
from Playing_card_detection.utils.common import  decodeImage, encodeImageintobase64
from Playing_card_detection.utils.exception import CustomException
from Playing_card_detection.utils.logger import logger
import pathlib
from pathlib import Path

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self) -> None:
        self.filename = "inputImage.jpg"

@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/predict",methods = ['POST','GET'])
@cross_origin()
def predictImage():
    try:
        image = request.json['image']
        decodeImage(image,clApp.filename)
    
        os.system(f"cd yolov5/ && python detect.py --weights best.pt --img 416 --conf 0.5 --source ../inference_data/inputImage.jpg")

        coded_image= encodeImageintobase64("yolov5/runs/detect/exp/inputImage.jpg")

        result = {"image": coded_image.decode('utf-8')} 
        os.system("rm -rf yolov5/runs")

        return jsonify(result)
    except Exception as e:
        raise CustomException(e,sys)

if __name__ == "__main__":
    temp = pathlib.PosixPath
    pathlib.PosixPath = pathlib.WindowsPath
    clApp = ClientApp()
    app.run(host = "0.0.0.0",port = '8080',debug=True)