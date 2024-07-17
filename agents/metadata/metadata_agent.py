from PIL import Image, ImageEnhance
import piexif
from transformers import pipeline
import config
import os

class MetadataAgent:
    def __init__(self):
        self.summarizer = pipeline("summarization")

    def extract_metadata(self, image_path):
        try:
            img = Image.open(image_path)
            exif_data = piexif.load(img.info["exif"]) if "exif" in img.info else None
            return exif_data
        except Exception as e:
            print(f"Failed to extract metadata from image at path {image_path}, error: {e}")
            return None

    def harmonize_colors(self, image_path):
        try:
            img = Image.open(image_path)
            enhancer = ImageEnhance.Color(img)
            harmonized_img = enhancer.enhance(1.5)
            new_image_path = image_path.replace('.png', '_harmonized.png')
            harmonized_img.save(new_image_path)
            return harmonized_img
        except Exception as e:
            print(f"Failed to harmonize colors for image at path {image_path}, error: {e}")
            return None

    def validate_positions(self, positions):
        try:
            if isinstance(positions, list) and all(isinstance(pos, dict) for pos in positions):
                for pos in positions:
                    if not all(key in pos for key in ['x', 'y', 'w', 'h']):
                        raise ValueError("Position missing required keys")
                return True
            else:
                raise ValueError("Positions format is incorrect")
        except ValueError as e:
            print(f"Failed to validate positions: {e}")
            return False

    def summarize_text(self, text, max_length_factor=0.5):
        try:
            input_length = len(text.split())
            max_length = max(1, int(input_length * max_length_factor))
            summary = self.summarizer(text, max_length=max_length)[0]['summary_text']
            return summary
        except Exception as e:
            print(f"Failed to summarize text, error: {e}")
            return None

if __name__ == "__main__":
    agent = MetadataAgent()
    image_path = os.path.join(config.IMAGES_DIR, 'example_image.png')
    metadata = agent.extract_metadata(image_path)
    harmonized_image = agent.harmonize_colors(image_path)
    positions = [{'x': 2353.4, 'y': 447.3, 'w': 2950.5, 'h': 1719.1}]
    is_valid = agent.validate_positions(positions)
    text = "Sample description for analysis"
    summary = agent.summarize_text(text)

    print("Extracted metadata:", metadata)
    print("Positions valid:", is_valid)
    print("Summary:", summary)
