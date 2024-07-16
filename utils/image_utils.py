from PIL import Image

def get_image_metadata(image_path):
    """
    Extract metadata from an image.

    Parameters:
    - image_path: string, path to the image file

    Returns:
    - metadata: dictionary containing image metadata
    """
    try:
        with Image.open(image_path) as img:
            metadata = {
                'format': img.format,
                'mode': img.mode,
                'size': img.size,
                'info': img.info
            }
            return metadata
    except Exception as e:
        print(f"Failed to extract metadata from image: {image_path}, error: {e}")
        return None

def compose_image(images, layout):
    """
    Compose multiple images into a single image based on the provided layout.

    Parameters:
    - images: list of PIL.Image objects
    - layout: dictionary containing positions, sizes, and orientations

    Returns:
    - composed_image: PIL.Image object
    """
    # Create a blank canvas for composition based on the layout
    canvas_width = max([pos[0] + size[0] for pos, size in zip(layout['positions'], layout['sizes'])])
    canvas_height = max([pos[1] + size[1] for pos, size in zip(layout['positions'], layout['sizes'])])
    composed_image = Image.new('RGBA', (canvas_width, canvas_height))

    for image, pos, size, orientation in zip(images, layout['positions'], layout['sizes'], layout['orientations']):
        # Resize image
        resized_image = image.resize(size)

        # Rotate image
        rotated_image = resized_image.rotate(orientation, expand=True)

        # Paste image onto the canvas
        composed_image.paste(rotated_image, pos, rotated_image)

    return composed_image

def save_image(image, path):
    """
    Save a PIL.Image object to a specified path.

    Parameters:
    - image: PIL.Image object
    - path: string, file path where the image will be saved
    """
    image.save(path)
