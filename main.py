import os
from PIL import Image
from agents.image.image_analysis_agent import ImageAnalysisAgent
from agents.text.text_analysis_agent import TextAnalysisAgent
from agents.critic.critic_grading_agent import CriticGradingAgent
from agents.autogen.autogen_agent import AutoGenAgent
import config

def main():
    # Define the directories and files using config
    image_files = [os.path.join(config.IMAGES_DIR, f) for f in os.listdir(config.IMAGES_DIR) if f.endswith(('png', 'jpg', 'jpeg'))]

    # Initialize agents
    image_analysis_agent = ImageAnalysisAgent()
    text_analysis_agent = TextAnalysisAgent()
    critic_grading_agent = CriticGradingAgent()
    autogen_agent = AutoGenAgent()

    assets = [{'image': Image.open(image_file), 'description': "Sample description for analysis"} for image_file in image_files]

    for asset in assets:
        print(f"Processing image: {asset['image'].filename}")

        # Perform tasks with agents
        image_analysis = image_analysis_agent.analyze_image(asset['image'])
        text_analysis = text_analysis_agent.narrative_understanding(asset['description'])

        asset.update({'image_analysis': image_analysis, 'text_analysis': text_analysis})

        analysis_result = critic_grading_agent.analyze_asset(asset)
        print(f"Asset Analysis Result: {analysis_result}")

        if analysis_result['grade'] < critic_grading_agent.threshold:
            edited_asset = autogen_agent.edit_asset(asset, analysis_result['critique'])
            print(f"Edited Asset: {edited_asset}")

if __name__ == "__main__":
    main()
