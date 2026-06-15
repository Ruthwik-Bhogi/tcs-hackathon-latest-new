
class DigitalTwin:
    def __init__(self,state):
        self.state=state
    def simulate_surge(self,percent):
        add=int(self.state['patient_count']*percent/100)
        self.state['patient_count']+=add
        self.state['icu_occupied']=min(
            self.state['icu_capacity'],
            self.state['icu_occupied']+int(add*0.1)
        )
        return self.state
