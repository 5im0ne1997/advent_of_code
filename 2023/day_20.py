from pathlib import Path
from abc import ABC, abstractmethod
from copy import copy, deepcopy

class Module(ABC):
    def __init__(self, output: list) -> None:
        self.output = output
        self.pulse = 'low'
        self.input = []
        self.last = []

    def send(self) -> None:
        queue = []
        for module in self.output:
            queue.append((self.pulse, module))
        return queue
    
    @abstractmethod
    def receive(self, pulse: str, module: str):
        pass

class Broadcaster(Module):
    def __init__(self, output: list) -> None:
        super().__init__(output)

    def receive(self, pulse: str, module: str):
        pass

class Flip_Flop(Module):
    def __init__(self, output: list) -> None:
        super().__init__(output)
        self.state = 'off'

    def receive(self, pulse: str, module: str):
        if pulse == 'low':
            match self.state:
                case 'on':
                    self.state = 'off'
                    self.pulse = 'low'
                case 'off':
                    self.state = 'on'
                    self.pulse = 'high'
            return self.send()

class Conjunction(Module):
    def __init__(self, output: list) -> None:
        super().__init__(output)
        self.pulse = 'high'

    def receive(self, pulse: str, module: str):
        self.last[self.input.index(module)] = pulse
        if 'low' in self.last:
            self.pulse = 'high'
        else:
            self.pulse = 'low'
        return self.send()

with open(Path("2023","day_20.txt")) as file:
    input_file = [line for line in file.read().split("\n")]

circuit = {}
for line in input_file:
    start, end = line.split(" -> ")
    end = end.split(", ")
    if start == "broadcaster":
        circuit[start] = Broadcaster(end)
    elif start.startswith("%"):
        start = start.lstrip("%")
        circuit[start] = Flip_Flop(end)
    elif start.startswith("&"):
        start = start.lstrip("&")
        circuit[start] = Conjunction(end)

for module_name, module_object in circuit.items():
    for output in module_object.output:
        if output in circuit:
            circuit[output].input.append(module_name)
            circuit[output].last.append('low')


pulses = {"low": 0, "high": 0}

for i in range(1000):
    to_send = {"broadcaster": circuit["broadcaster"].send()}
    pulses["low"] += 1
    while len(to_send) > 0:
        temp_to_send = {}
        for sender, output in to_send.items():
            for module in output:
                pulses[module[0]] += 1
                if module[1] in circuit:
                    temp_queue = (circuit[module[1]].receive(module[0], sender))
                    if temp_queue != None:
                        new_sender = module[1]
                        queue = []
                        for pulse in temp_queue:
                            queue.append(pulse)
                        temp_to_send[new_sender] = copy(queue)
        to_send = deepcopy(temp_to_send)

print(pulses['low'] * pulses['high'])
pass