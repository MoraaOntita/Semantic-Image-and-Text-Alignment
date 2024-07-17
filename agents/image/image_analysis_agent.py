import cv2
from transformers import pipeline
from yolov5 import YOLOv5
from PIL import Image
import pytesseract

class ImageAnalysisAgent:
    def __init__(self, model_path='yolov5s.pt'):
        self.yolo = YOLOv5(model_path)
        self.color_extractor = pipeline('image-classification', model='microsoft/swin-tiny-patch4-window7-224')

    def object_identification(self, image):
        results = self.yolo.predict(image)
        objects = results.pred[0].numpy()
        return objects

    def color_identification(self, image):
        colors = self.color_extractor(image)
        primary_colors = [color['label'] for color in colors]
        return primary_colors

    def position_extraction(self, objects):
        positions = [{'x': obj[0], 'y': obj[1], 'w': obj[2], 'h': obj[3]} for obj in objects]
        return positions

    def character_recognition(self, image):
        text = pytesseract.image_to_string(image)
        return text

    def analyze_image(self, image):
        objects = self.object_identification(image)
        primary_colors = self.color_identification(image)
        positions = self.position_extraction(objects)
        text = self.character_recognition(image)
        return {'objects': objects, 'colors': primary_colors, 'positions': positions, 'text': text}
