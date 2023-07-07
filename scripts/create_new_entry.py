new_entry = "submit_job"
print(f"""version: "3.1"

intents:
- {new_entry}

nlu:
- intent: {new_entry}
  examples: |
    - 
    - 
    - 

responses:
  utter_{new_entry}:
  - text: ""

stories:
- story: {new_entry} 1
  steps:
  - intent: {new_entry}
  - action: utter_{new_entry}

- story: {new_entry} 2
  steps:
  - intent: greet
  - action: utter_greet
  - intent: {new_entry}
  - action: utter_{new_entry}

""")