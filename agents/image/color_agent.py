from utils.color_utils import harmonize_colors
from PIL import Image
import config

class ColorAgent:
    def __init__(self):
        pass

    def perform_task(self, image):
        harmonized_image = self.harmonize_image_colors(image)
        return harmonized_image

    def harmonize_image_colors(self, image):
        try:
            harmonized_image = harmonize_colors(image)
            print(f"Harmonized colors for image: {image}")
            return harmonized_image
        except Exception as e:
            print(f"Failed to harmonize colors for image: {image}, error: {e}")
            return None
