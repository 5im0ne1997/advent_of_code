from pathlib import Path
from copy import deepcopy

class WorkFlow():
    def __init__(self, workflows: str) -> None:
        self.conditions = [conditions for conditions in workflows.split(",")]
        self.exit = self.conditions[-1]
        self.conditions.pop()

    def test(self, machine_parts: object, part2: bool = False) -> str:
        for single_condition in self.conditions:
            condition, exit = single_condition.split(":")
            if '<' in condition:
                category, number = condition.split("<")
                if  machine_parts.machine_part[category] < int(number):
                    return exit
            elif '>' in condition:
                category, number = condition.split(">")
                if  machine_parts.machine_part[category] > int(number):
                    return exit
        else:
            return self.exit

class Machine_Parts():
    def __init__(self, machine_parts: str) -> None:
        machine_parts = [part for part in machine_parts.split(",")]
        self.machine_part = {}
        for part in machine_parts:
            category, number = part.split("=")
            self.machine_part[category] = int(number)   
        self.sum = 0
        for number in self.machine_part.values():
            self.sum += number

class Machine_Parts2():
    def __init__(self, machine_parts: dict):
        self.machine_part = deepcopy(machine_parts)

with open(Path("2023","day_19.txt")) as file:
    workflows, machines_parts = file.read().split("\n\n")
    workflows = [workflow for workflow in workflows.split("\n")]
    machines_parts = [machine_parts for machine_parts in machines_parts.split("\n")]
    all_workflows = dict()
    for workflow in workflows:
        name, conditions = workflow.split("{")
        conditions = conditions.rstrip("}")
        all_workflows[name] = WorkFlow(conditions)
    all_machines_parts = []
    for machine_parts in machines_parts:
        machine_parts = machine_parts.strip("{}")
        all_machines_parts.append(Machine_Parts(machine_parts))
sum1 = 0

for machine_parts in all_machines_parts:
    flag = True
    workflow = "in"
    while flag:
        exit = all_workflows[workflow].test(machine_parts)
        if exit == 'A':
            sum1 += machine_parts.sum
            flag = False
        elif exit == 'R':
            flag = False
        else:
            workflow = exit

print(sum1)

pass