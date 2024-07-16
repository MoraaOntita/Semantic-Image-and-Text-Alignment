from utils.text_utils import extract_text_from_image
import config

class TextExtractionAgent:
    def __init__(self):
        pass

    def perform_task(self, image_path):
        text = self.extract_text(image_path)
        self.process_extracted_text(text)

    def extract_text(self, image_path):
        try:
            text = extract_text_from_image(image_path)
            print(f"Extracted text from image: {text}")
            return text
        except Exception as e:
            print(f"Failed to extract text from image: {image_path}, error: {e}")
            return None

    def process_extracted_text(self, text):
        # Implement your text processing logic here
        if text:
            print(f"Processing extracted text: {text}")
        else:
            print("No text to process.")
