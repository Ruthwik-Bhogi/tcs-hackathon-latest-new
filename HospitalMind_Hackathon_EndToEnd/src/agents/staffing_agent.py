
class StaffingAgent:
    def evaluate(self,state):
        ratio=state['patient_count']/state['nurse_count']
        return 'Shortage' if ratio>12 else 'Adequate'
