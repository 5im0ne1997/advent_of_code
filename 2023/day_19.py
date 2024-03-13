from pathlib import Path
from copy import copy

class WorkFlow():
    def __init__(self, workflows: str) -> None:
        self.conditions = [conditions for conditions in workflows.split(",")]
        self.exit = self.conditions[-1]
        self.conditions.pop()

    def test(self, machine_parts: object) -> str:
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
    
    def test2(self, machine_parts: object) -> list:
        part2_to_test = [machine_parts]
        part2_tested = []
        for single_condition in self.conditions:
            temp = []
            for to_test in part2_to_test:
                condition, exit = single_condition.split(":")
                if '<' in condition:
                    category, number = condition.split("<")
                    before = [to_test.machine_part[category][0], min(to_test.machine_part[category][1], int(number) - 1)]
                    after = [max(to_test.machine_part[category][0], int(number)), to_test.machine_part[category][1]]
                    if before[1] >= before[0]:
                        part2_tested.append(Machine_Parts2(to_test.machine_part))
                        part2_tested[-1].machine_part[category] = before
                        part2_tested[-1].status = exit
                    if after[1] >= after[0]:
                        temp.append(Machine_Parts2(to_test.machine_part))
                        temp[-1].machine_part[category] = after
                elif '>' in condition:
                    category, number = condition.split(">")
                    before = [to_test.machine_part[category][0], min(to_test.machine_part[category][1], int(number))]
                    after = [max(to_test.machine_part[category][0], int(number) + 1), to_test.machine_part[category][1]]
                    if before[1] >= before[0]:
                        temp.append(Machine_Parts2(to_test.machine_part))
                        temp[-1].machine_part[category] = before
                    if after[1] >= after[0]:
                        part2_tested.append(Machine_Parts2(to_test.machine_part))
                        part2_tested[-1].machine_part[category] = after
                        part2_tested[-1].status = exit
            part2_to_test = copy(temp)
        else:
            for to_test in part2_to_test:
                to_test.status = self.exit
                part2_tested.append(to_test)
            return part2_tested

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
        self.machine_part = copy(machine_parts)
        self.status = "in"

    def solution(self) -> int:
        dx = self.machine_part['x'][1] - self.machine_part['x'][0] + 1
        dm = self.machine_part['m'][1] - self.machine_part['m'][0] + 1
        da = self.machine_part['a'][1] - self.machine_part['a'][0] + 1
        ds = self.machine_part['s'][1] - self.machine_part['s'][0] + 1
        return (dx * dm * da * ds)

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

sum2 = 0
to_test_part2 = [Machine_Parts2({'x':[1,4000],'m':[1,4000],'a':[1,4000],'s':[1,4000]})]

tested_part2 = []
while len(to_test_part2) > 0:
    all_machines_parts_2 = copy(to_test_part2)
    to_test_part2 = []
    for machine_parts_2 in all_machines_parts_2:
        temp_machine_parts_2 = all_workflows[machine_parts_2.status].test2(machine_parts_2)
        for machine_parts in temp_machine_parts_2:
            if machine_parts.status == 'A':
                tested_part2.append(machine_parts)
            elif machine_parts.status != 'R':
                to_test_part2.append(machine_parts)


for part2 in tested_part2:
    sum2 += part2.solution()

print(sum2)
pass