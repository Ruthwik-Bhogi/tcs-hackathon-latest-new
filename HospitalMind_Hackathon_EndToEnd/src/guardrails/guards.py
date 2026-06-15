
class HallucinationGuard:
    def validate(self,evidence):
        return len(evidence)>0

class ConfidenceGuard:
    def score(self,evidence_count):
        return min(0.5+evidence_count*0.2,0.99)
