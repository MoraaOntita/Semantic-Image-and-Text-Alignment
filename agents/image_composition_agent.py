from utils.image_utils import compose_image, save_image
import config

class ImageCompositionAgent:
    def __init__(self):
        pass

    def perform_task(self, image_paths, layout):
        composed_image = self.compose_images(image_paths, layout)
        self.save_composed_image(composed_image, config.COMPOSED_IMAGE_PATH)

    def compose_images(self, images, layout):
        try:
            composed_image = compose_image(images, layout)
            print(f"Composed image from: {images}")
            return composed_image
        except Exception as e:
            print(f"Failed to compose images: {images}, error: {e}")
            return None

    def save_composed_image(self, composed_image, output_path):
        if composed_image:
            save_image(composed_image, output_path)
            print(f"Composed image saved to: {output_path}")
        else:
            print("No composed image to save.")
