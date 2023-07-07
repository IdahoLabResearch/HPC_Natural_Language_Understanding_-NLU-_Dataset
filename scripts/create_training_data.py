import random
import yaml
from rich.pretty import pprint

lookup_file = "data/hpc/lookups.yml"
node_list = list(range(1, 21))
core_list = list(range(1, 100))
time_num = list(range(1, 101))
time_unit = ["minutes", "hours", "days"]

terms_dict = {}

with open(lookup_file, "r") as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

for lookup in data['nlu']:
    terms_dict[lookup['lookup']] = []
    for item in lookup['examples'].replace("-", "").strip().split("\n"):
       terms_dict[lookup['lookup']].append(item.strip())
# pprint(terms_dict)        

start_words = [
    "run", "submit", "execute", "start", "kick off", "create", "open", "launch", "give me", "can you give", 
    "can you provide", "I would like to submit", "I want to request a", "Do you mind", "Could I get", 
    "Would it be okay if", "could you", "can I get", "I want"
    ]
# Not yet used
end_words = ["now", "please", ""]

core_words = terms_dict['cpu']
core_words.append("cpu")

node_words = terms_dict['node']
node_words.append("nodes")

program_list = ["jupyter", "desktop", "paraview", "starccm", "bison", "interactive", "python", "python3", "abaqus"]
programs = {}
for prog in program_list:
    programs[prog] = [prog]
    try:
        programs[prog].extend(terms_dict[prog])
    except KeyError:
        pass

system_list = ["sawtooth", "lemhi", "hoodoo"]
systems = {}
for sys in system_list:
    systems[sys] = [sys]
    try:
        systems[sys].extend(terms_dict[sys])
    except KeyError:
        pass

def create_job_submission_details(count: int) -> None:
    for key,value in systems.items():
        for system_synonym in value:
        # ran_system = random.choice(system_list)
        # ran_system_synonym = random.choice(systems[ran_system])
            sentence = f'- [{system_synonym}]{{"entity": "system_name", "value": "{key}" }}'
            print(f"    {sentence}")

    for _ in range(count):
        ran_core_num = random.choice(core_list) 
        sentence = f'- [{ran_core_num} {random.choice(core_words)}]{{"entity": "cores", "value": "{ran_core_num} cores"}}'
        print(f"    {sentence}")

    for _ in range(count):
        ran_node_num = random.choice(node_list)
        sentence = f'- [{ran_node_num} {random.choice(node_words)}]{{"entity": "nodes", "value": "{ran_node_num} nodes"}}'
        print(f"    {sentence}")

    for _ in range(count):
        sentence = f"- [{random.choice(time_num)} {random.choice(time_unit)}](walltime)"
        print(f"    {sentence}")

    for key,value in programs.items():
        for program in value:
            # ran_program = random
            sentence = f'- [{program}]{{"entity": "program", "value": "{key}" }}'
            print(f"    {sentence}")

def create_submit_job(count: int) -> None:
    # start a job on X nodes with Y cores for Z hours
    for _ in range(count):
        ran_node_num = random.choice(node_list)
        ran_core_num = random.choice(core_list)  
        sentence = f'    - \
{random.choice(start_words)} a job on \
[{ran_node_num} {random.choice(node_words)}]{{"entity": "nodes", "value": "{ran_node_num} nodes"}} with \
[{ran_core_num} {random.choice(core_words)}]{{"entity": "cores", "value": "{ran_core_num} cores"}} for \
[{random.choice(time_num)} {random.choice(time_unit)}](walltime) \
{random.choice(end_words)}'
        print(sentence)

    # start a job on SYSTEM with X cores for Z hours
    for _ in range(count):
        ran_system = random.choice(system_list)
        ran_system_synonym = random.choice(systems[ran_system])
        ran_core_num = random.choice(core_list)  
        sentence = f'    - {random.choice(start_words)} a job on \
[{ran_system_synonym}]{{"entity": "system_name", "value": "{ran_system}" }} with \
[{ran_core_num} {random.choice(core_words)}]{{"entity": "cores", "value": "{ran_core_num} cores"}} for \
[{random.choice(time_num)} {random.choice(time_unit)}](walltime) \
{random.choice(end_words)}'
        print(sentence)

    # start PROGRAM on SYSTEM with X cores for Z hours
    for _ in range(count):
        ran_system = random.choice(system_list)
        ran_system_synonym = random.choice(systems[ran_system])
        ran_program = random.choice(program_list)
        ran_program_synonym = random.choice(programs[ran_program])
        ran_core_num = random.choice(core_list)  
        sentence = f'    - \
{random.choice(start_words)} \
[{ran_program_synonym}]{{"entity": "program", "value": "{ran_program}" }} on \
[{ran_system_synonym}]{{"entity": "system_name", "value": "{ran_system}" }} with \
[{ran_core_num} {random.choice(core_words)}]{{"entity": "cores", "value": "{ran_core_num} cores"}} for \
[{random.choice(time_num)} {random.choice(time_unit)}](walltime) \
{random.choice(end_words)}'
        print(sentence)

if __name__ == "__main__":
    count = 150
    # print(core_words)
    # print(programs)
    # print(systems)
    # print(node_words)
    # print(programs)

    # print()
    # create_job_submission_details(count)
    create_submit_job(count)

                              
                              
                              
                              