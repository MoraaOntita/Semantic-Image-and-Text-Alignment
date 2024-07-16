import os
from agents.image_agent import ImageAgent
from agents.enhanced_text_agent import EnhancedTextAgent
from agents.text_extraction_agent import TextExtractionAgent
from agents.metadata_agent import MetadataAgent
from agents.color_agent import ColorAgent
from agents.image_composition_agent import ImageCompositionAgent
from PIL import Image
import config

def main():
    # Define the directories and files using config
    image_files = [os.path.join(config.IMAGES_DIR, f) for f in os.listdir(config.IMAGES_DIR) if f.endswith(('png', 'jpg', 'jpeg'))]

    # Initialize agents
    image_agent = ImageAgent()
    text_agent = EnhancedTextAgent()
    text_extraction_agent = TextExtractionAgent()
    metadata_agent = MetadataAgent()
    color_agent = ColorAgent()
    composition_agent = ImageCompositionAgent()

    assets = [Image.open(image_file) for image_file in image_files]

    for image_file in image_files:
        print(f"Processing image: {image_file}")

        # Perform tasks with agents
        image_agent.perform_task(image_file)
        text_extraction_agent.perform_task(image_file)
        metadata_agent.perform_task(image_file)
        color_agent.perform_task(image_file)

    # Define a simple layout for demonstration purposes
    layout = {
        'positions': [(0, 0), (200, 200), (400, 400)],  # Example positions
        'sizes': [(100, 100), (150, 150), (200, 200)],  # Example sizes
        'orientations': [0, 45, 90]  # Example orientations
    }

    # Perform image composition
    composed_frame = composition_agent.compose_images(assets, layout)
    if composed_frame:
        composed_frame.show()

    text_agent.perform_task(config.JSON_FILE_PATH)

if __name__ == "__main__":
    main()
