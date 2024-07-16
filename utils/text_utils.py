import pytesseract
from PIL import Image

def process_text_data(data):
    """
    Process text data from the JSON file.

    Parameters:
    - data: list or dictionary loaded from the JSON file

    Returns:
    - processed_data: dictionary or list with non-empty values
    """
    if isinstance(data, dict):
        processed_data = {key: value for key, value in data.items() if value}
    elif isinstance(data, list):
        processed_data = [{key: value for key, value in item.items() if value} for item in data]
    else:
        raise ValueError("Unsupported data type: {}".format(type(data)))

    return processed_data

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Failed to extract text from image: {image_path}, error: {e}")
        return ""
