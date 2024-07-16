from utils.color_utils import harmonize_colors
import config

class ColorAgent:
    def __init__(self):
        pass

    def perform_task(self, image_path):
        harmonized_image = self.harmonize_image_colors(image_path)
        self.save_harmonized_image(harmonized_image, image_path)

    def harmonize_image_colors(self, image_path):
        try:
            harmonized_image = harmonize_colors(image_path)
            print(f"Harmonized colors for image: {image_path}")
            return harmonized_image
        except Exception as e:
            print(f"Failed to harmonize colors for image: {image_path}, error: {e}")
            return None

    def save_harmonized_image(self, harmonized_image, image_path):
        if harmonized_image:
            output_path = f"{image_path.rsplit('.', 1)[0]}_harmonized.png"
            harmonized_image.save(output_path)
            print(f"Harmonized image saved to: {output_path}")
        else:
            print("No harmonized image to save.")
