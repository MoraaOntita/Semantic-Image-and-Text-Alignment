from PIL import Image, ImageEnhance

def harmonize_colors(image_path):
    try:
        image = Image.open(image_path)
        enhancer = ImageEnhance.Color(image)
        harmonized_image = enhancer.enhance(1.5)  # Adjust the factor as needed for color enhancement
        return harmonized_image
    except Exception as e:
        print(f"Failed to harmonize colors for image: {image_path}, error: {e}")
        return None
