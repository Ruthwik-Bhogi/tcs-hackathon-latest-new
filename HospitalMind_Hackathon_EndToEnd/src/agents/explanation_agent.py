
class ExplanationAgent:
    def explain(self,recommendations,confidence):
        return {
            'confidence':confidence,
            'recommendations':recommendations,
            'summary':'Recommendations generated from digital twin state and graph dependencies'
        }
