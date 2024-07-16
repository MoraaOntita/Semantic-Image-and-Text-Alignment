from utils.image_utils import get_image_metadata
import config

class MetadataAgent:
    def __init__(self):
        pass

    def perform_task(self, image_path):
        metadata = self.extract_metadata(image_path)
        self.process_metadata(metadata)

    def extract_metadata(self, image_path):
        try:
            metadata = get_image_metadata(image_path)
            print(f"Extracted metadata from image: {metadata}")
            return metadata
        except Exception as e:
            print(f"Failed to extract metadata from image: {image_path}, error: {e}")
            return None

    def process_metadata(self, metadata):
        # Implement your metadata processing logic here
        if metadata:
            print(f"Processing metadata: {metadata}")
        else:
            print("No metadata to process.")
