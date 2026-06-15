
class DecisionAgent:
    def generate(self,state,resources):
        rec=[]
        occ=(state['icu_occupied']/state['icu_capacity'])*100
        if occ>90:
            rec+=['Open Overflow Ward B','Increase ICU Capacity']
        if 'Ventilator' in resources:
            rec.append('Allocate 5 Additional Ventilators')
        return rec
