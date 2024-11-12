from model import TextAnalyzer
from view import TextAnalyzerView

class TextAnalyzerController:
    def __init__(self, view):
        self.view = view
        self.model = TextAnalyzer()
        self.view.analyze_button.config(command=self.perform_analysis)

    def perform_analysis(self):
        text = self.view.get_input_text()
        results = self.model.analyze(text)
        self.view.display_results(results)
