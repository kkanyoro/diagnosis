import streamlit as st

class DrMacadamia:
    def __init__(self):
        # Rules and Facts
        # Knowledge base defined based on production rule principle
        self.rules = [
            {"id": "R1", "if": ["yellow_leaves", "water_logged_soil"], "then": "suspect_root_rot", "prio": 1},
            {"id": "R2", "if": ["suspect_root_rot", "wilting"], "then": "diagnose_phytophthora", "prio": 5},
            {"id": "R3", "if": ["diagnose_phytophthora"], "then": "recommend_drainage", "prio": 10},
            {"id": "R4", "if": ["holes_in_husk", "sawdust_frass"], "then": "suspect_nut_borer", "prio": 1},
            {"id": "R5", "if": ["suspect_nut_borer", "larvae_present"], "then": "diagnose_borer_infestation", "prio": 5},
            {"id": "R6", "if": ["diagnose_borer_infestation"], "then": "apply_pesticide", "prio": 10},
            {"id": "R7", "if": ["yellow_spots_on_husk", "high_humidity"], "then": "diagnose_husk_spot", "prio": 5},
            {"id": "R8", "if": ["diagnose_husk_spot"], "then": "apply_fungicide", "prio": 10},
            {"id": "R9", "if": ["sticky_honeydew", "black_sooty_mould"], "then": "diagnose_aphid_attack", "prio": 5},
            {"id": "R10", "if": ["white_powdery_mould"], "then": "diagnose_powdery_mildew", "prio": 5}
        ]
        self.facts = set()
        self.trace = []

    def forward_chain(self, initial_facts):
        # Data-driven inference
        self.facts = set(initial_facts)
        self.trace = []
        changed = True
        while changed:
            changed = False
            # Conflict Resolution by Priority
            sorted_rules = sorted(self.rules, key=lambda x: x['prio'], reverse=True)
            for rule in sorted_rules:
                if all(cond in self.facts for cond in rule['if']) and rule['then'] not in self.facts:
                    self.facts.add(rule['then'])
                    self.trace.append(f"Rule {rule['id']} fired: Based on {rule['if']}, derived {rule['then']}")
                    changed = True
                    break 
        return self.facts, self.trace

    def backward_chain(self, goal, known_facts):
        # Goal-driven recursive inference
        self.facts = set(known_facts)
        self.trace = []
        
        def prove(target, depth=0):
            indent = "  " * depth
            if target in self.facts:
                self.trace.append(f"{indent} Found: {target} is already in knowledge base.")
                return True
            for rule in self.rules:
                if rule['then'] == target:
                    self.trace.append(f"{indent} Attempting {rule['id']} for {target}. Verifying subgoals: {rule['if']}")
                    if all(prove(cond, depth + 1) for cond in rule['if']):
                        self.facts.add(target)
                        self.trace.append(f"{indent} Proved: {target} via {rule['id']}.")
                        return True
            self.trace.append(f"{indent} Cannot prove: {target}.")
            return False

        result = prove(goal)
        return result, self.trace

# Streamlit Interface Config
st.set_page_config(page_title="Dr. Macadamia")
st.title("Dr. Macadamia")

# Mode Selection
mode = st.sidebar.radio("Inference Mode", ["Forward Chaining", "Backward Chaining"])

expert = DrMacadamia()
all_symptoms = [
    "yellow_leaves", "water_logged_soil", "wilting", "holes_in_husk", "sawdust_frass", 
    "larvae_present", "yellow_spots_on_husk", "high_humidity", "sticky_honeydew", 
    "black_sooty_mould", "white_powdery_mould"
]

if mode == "Forward Chaining":
    st.header("Diagnosis via Forward Chaining")
    selected_symptoms = st.multiselect("Select symptoms:", all_symptoms)
    
    if st.button("Generate Diagnosis"):
        final_facts, trace = expert.forward_chain(selected_symptoms)
        
        st.subheader("System Reasoning Trace")
        for step in trace:
            st.text(step)
            
        st.subheader("Conclusions")
        diagnoses = [f for f in final_facts if f not in all_symptoms]
        if diagnoses:
            for d in diagnoses:
                st.success(f"Confirmed: {d}")
        else:
            st.info("No diagnoses could be reached with provided symptoms.")

else:
    st.header("Verification via Backward Chaining")
    goal_to_prove = st.selectbox("Target diagnosis/treatment:", 
                                 [r['then'] for r in expert.rules])
    known_facts = st.multiselect("Known facts:", all_symptoms)
    
    if st.button("Verify Statement"):
        success, trace = expert.backward_chain(goal_to_prove, known_facts)
        
        st.subheader("Reasoning Path")
        for step in trace:
            st.text(step)
            
        if success:
            st.success(f"Result: The goal '{goal_to_prove}' is verified.")
        else:
            st.error(f"Result: The goal '{goal_to_prove}' remains unproven.")