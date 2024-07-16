import os

# Configuration file for setting up paths and other constants

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, 'data')
IMAGES_DIR = os.path.join(DATA_DIR, 'adludio_storyboard_examples')
JSON_FILE_PATH = os.path.join(DATA_DIR, 'concepts.json')
COMPOSED_IMAGE_PATH = os.path.join(BASE_DIR, 'composed_image.png')

