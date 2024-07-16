from PIL import Image
import os

class ImageAgent:
    def __init__(self):
        pass

    def perform_task(self, image_path):
        image = self.load_image(image_path)
        self.process_image(image)

    def load_image(self, image_path):
        try:
            image = Image.open(image_path)
            print(f"Loaded image: {image_path}")
            return image
        except Exception as e:
            print(f"Failed to load image: {image_path}, error: {e}")
            return None

    def process_image(self, image):
        # Implement your image processing logic here
        if image:
            print(f"Processing image of size: {image.size}")
        else:
            print("No image to process.")
