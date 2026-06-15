
class ICUAgent:
    def evaluate(self,state):
        occ=(state['icu_occupied']/state['icu_capacity'])*100
        if occ>90:return 'High Risk'
        if occ>75:return 'Medium Risk'
        return 'Normal'
