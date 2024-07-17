from transformers import pipeline

class TextAnalysisAgent:
    def __init__(self):
        self.summarizer = pipeline('summarization')
        self.keyword_extractor = pipeline('ner')

    def text_summarization(self, text):
        summary = self.summarizer(text, max_length=50, min_length=25, do_sample=False)
        return summary[0]['summary_text']

    def key_phrase_identification(self, text):
        key_phrases = self.keyword_extractor(text)
        phrases = [phrase['word'] for phrase in key_phrases]
        return phrases

    def narrative_understanding(self, text):
        summary = self.text_summarization(text)
        key_phrases = self.key_phrase_identification(text)
        return {'summary': summary, 'key_phrases': key_phrases, 'score': 80}  # Adding dummy score for example
