from utils.image_utils import compose_image, save_image
import config

class ImageCompositionAgent:
    def __init__(self):
        pass

    def perform_task(self, images, layout):
        composed_image = self.compose_images(images, layout)
        return composed_image

    def compose_images(self, images, layout):
        try:
            composed_image = compose_image(images, layout)
            print(f"Composed image from: {images}")
            return composed_image
        except Exception as e:
            print(f"Failed to compose images: {images}, error: {e}")
            return None
