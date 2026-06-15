
from src.orchestrator import Orchestrator
from src.digital_twin.state import hospital_state
from src.digital_twin.simulator import DigitalTwin

twin=DigitalTwin(hospital_state)
state=twin.simulate_surge(20)

result=Orchestrator().run(
    'What should we do if ICU occupancy reaches 95%?',
    state
)

print(result)
