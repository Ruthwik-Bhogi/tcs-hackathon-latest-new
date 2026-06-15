
from src.agents.icu_agent import ICUAgent
from src.agents.staffing_agent import StaffingAgent
from src.agents.decision_agent import DecisionAgent
from src.agents.explanation_agent import ExplanationAgent
from src.graph.hospital_graph import HospitalGraph
from src.rag.retriever import SOPRetriever
from src.guardrails.guards import HallucinationGuard,ConfidenceGuard

class Orchestrator:
    def run(self,question,state):
        docs=SOPRetriever().retrieve(question)
        if not HallucinationGuard().validate(docs):
            return {'error':'No evidence found'}
        graph=HospitalGraph()
        graph.build()
        resources=graph.impacted_resources('ICU')
        rec=DecisionAgent().generate(state,resources)
        conf=ConfidenceGuard().score(len(docs))
        return ExplanationAgent().explain(rec,conf)
