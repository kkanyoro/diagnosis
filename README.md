# Dr. Macadamia

This project is a rule-based expert system designed to assist Macadamia farmers in diagnosing pests and diseases. It utilizes symbolic AI techniques, specifically Forward and Backward Chaining, to provide diagnostic conclusions and treatment recommendations based on observed symptoms.

## Features

* **Knowledge Base:** Contains 10 production rules and over 15 unique facts regarding Macadamia crop health.
* **Forward Chaining:** A data-driven approach that moves from symptoms to a final diagnosis.
* **Backward Chaining:** A goal-driven approach that verifies if a specific diagnosis or treatment is supported by current facts.
* **Conflict Resolution:** Uses a priority-based (salience) system to ensure critical diagnoses are prioritized during inference.
* **Interactive UI:** A streamlined interface built with Streamlit for ease of use.

## Prerequisites

Before running the project, ensure you have Python installed on your system. You will also need the `streamlit` library.

You can install the required dependency using pip:

```bash
pip install streamlit

```

## How to Run

1. Navigate to the directory containing the project files.
2. Run the following command in your terminal:

```bash
streamlit run app.py

```

3. The application will automatically open in your default web browser (usually at `http://localhost:8501`).

## How to Use

### Forward Chaining (Diagnosis Mode)

1. Select **Forward Chaining** from the sidebar menu.
2. Use the multi-select box to choose the symptoms currently observed on the tree or nuts (e.g., `yellow_leaves`, `water_logged_soil`).
3. Click the **Generate Diagnosis** button.
4. Review the **System Reasoning Trace** to see which rules were fired and the **Conclusions** section for the final diagnosis.

### Backward Chaining (Verification Mode)

1. Select **Backward Chaining** from the sidebar menu.
2. Choose a **Target diagnosis/treatment** you wish to verify (e.g., `recommend_drainage`).
3. Select any **Known facts** you currently have.
4. Click **Verify Statement**.
5. The system will display the **Reasoning Path**, showing the recursive steps taken to prove or disprove the selected goal.