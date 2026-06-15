
import networkx as nx
class HospitalGraph:
    def __init__(self):
        self.g=nx.Graph()
    def build(self):
        self.g.add_edge('ICU','Ventilator')
        self.g.add_edge('ICU','Nurse')
        self.g.add_edge('ICU','Doctor')
    def impacted_resources(self,node):
        return list(self.g.neighbors(node))
