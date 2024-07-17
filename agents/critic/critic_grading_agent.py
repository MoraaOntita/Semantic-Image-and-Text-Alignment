from agents.image.image_agent import ImageAgent
from agents.text.enhanced_text_agent import EnhancedTextAgent
from agents.text.text_extraction_agent import TextExtractionAgent
from agents.metadata.metadata_agent import MetadataAgent
from agents.image.color_agent import ColorAgent
from agents.image.image_composition_agent import ImageCompositionAgent

class CriticGradingAgent:
    def __init__(self):
        self.image_agent = ImageAgent()
        self.text_agent = EnhancedTextAgent()
        self.text_extraction_agent = TextExtractionAgent()
        self.metadata_agent = MetadataAgent()
        self.color_agent = ColorAgent()
        self.image_composition_agent = ImageCompositionAgent()
        self.threshold = 70  # Define your threshold here

    def analyze_asset(self, asset):
        image_analysis = self.image_agent.perform_task(asset['image'])
        text_analysis = self.text_agent.perform_task(asset['description'])

        try:
            metadata_analysis = self.metadata_agent.perform_task(asset['image'])
        except Exception as e:
            print(f"Failed to extract metadata from image: {asset['image']}, error: {e}")
            metadata_analysis = {"score": 0, "metadata": "Metadata analysis failed"}

        try:
            harmonized_image = self.color_agent.perform_task(asset['image'])
            color_analysis = {"score": 85, "color_analysis": "Color harmonization result"} if harmonized_image else {"score": 0, "color_analysis": "Color harmonization failed"}
        except Exception as e:
            print(f"Failed to harmonize colors for image: {asset['image']}, error: {e}")
            color_analysis = {"score": 0, "color_analysis": "Color harmonization failed"}

        try:
            composition_analysis = self.image_composition_agent.perform_task([asset['image']], asset.get('layout', {}))
            composition_analysis = {"score": 90, "composition_analysis": "Composition result"} if composition_analysis else {"score": 0, "composition_analysis": "Composition failed"}
        except Exception as e:
            print(f"Failed to compose images: {[asset['image']]}, error: {e}")
            composition_analysis = {"score": 0, "composition_analysis": "Composition failed"}

        grade = self.grade_asset(image_analysis, text_analysis, metadata_analysis, color_analysis, composition_analysis)
        critique = self.provide_critique(image_analysis, text_analysis, metadata_analysis, color_analysis, composition_analysis)
        return {"grade": grade, "critique": critique}

    def grade_asset(self, image_analysis, text_analysis, metadata_analysis, color_analysis, composition_analysis):
        scores = [image_analysis['score'], text_analysis['score']]
        if metadata_analysis:
            scores.append(metadata_analysis['score'])
        if color_analysis:
            scores.append(color_analysis['score'])
        if composition_analysis:
            scores.append(composition_analysis['score'])

        overall_score = sum(scores) / len(scores)
        return overall_score

    def provide_critique(self, image_analysis, text_analysis, metadata_analysis, color_analysis, composition_analysis):
        critique = []
        if image_analysis['score'] < self.threshold:
            critique.append("Visuals could be improved.")
        if text_analysis['score'] < self.threshold:
            critique.append("Text needs more engagement.")
        if metadata_analysis and metadata_analysis['score'] < self.threshold:
            critique.append("Metadata is not well optimized.")
        if color_analysis and color_analysis['score'] < self.threshold:
            critique.append("Color scheme could be better.")
        if composition_analysis and composition_analysis['score'] < self.threshold:
            critique.append("Composition needs enhancement.")
        return critique
