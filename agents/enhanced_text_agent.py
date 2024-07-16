import json

class EnhancedTextAgent:
    def __init__(self):
        pass

    def perform_task(self, json_file_path):
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        self.process_text_data(data)

    def process_text_data(self, data):
        from utils.text_utils import process_text_data
        processed_data = process_text_data(data)
        print(f"Processed data: {processed_data}")
        # Add further processing logic here
