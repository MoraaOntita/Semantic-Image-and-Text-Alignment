from PIL import Image

class ImageAgent:
    def __init__(self):
        pass

    def perform_task(self, image):
        # Assuming image is already a PIL Image object
        processed_image = self.process_image(image)
        return self.analyze_image(processed_image)

    def process_image(self, image):
        # Dummy processing function
        return image

    def analyze_image(self, image):
        # Dummy analysis function
        return {
            "score": 80,  # Dummy score for example
            "analysis": "Image analysis result"
        }
