from pathlib import Path
from abc import ABC, abstractmethod
from copy import copy

class Module(ABC):

    def __init__(self, name: str):
        self.name = name
        self.linked_to = []
        self.low_sended = 0
        self.high_sended = 0
        self.can_send_pulse = True
    
    def add_link_to(self, module: object):
        self.linked_to.append(module)
        module.add_link_from(self.name)

    @abstractmethod
    def add_link_from(self, name: str):
        pass

    @abstractmethod
    def recive_pulse(self, pulse: bool, name: str):
        pass

    @abstractmethod
    def send_pulses(self):
        pass
    
class FlipFlop(Module):

    def __init__(self, name: str):
        super().__init__(name)
        self.state = False #Flase is Off and send a low pulse (False), True is On and send high pulse (True)
    
    def add_link_from(self, name: str):
        pass #Not necessary

    def recive_pulse(self, pulse: bool, name: str):
        if not pulse: #If recive a Low Pulse
            self.state = not self.state #Switch state On or Of
            self.can_send_pulse = True #can send pulse in next step
        else:
            self.can_send_pulse = False #If recive an High Pulse can't send pulse in next step

    def send_pulses(self):
        for module in self.linked_to:
            module.recive_pulse(self.state, self.name)
            if self.state:
                self.high_sended += 1
            else:
                self.low_sended += 1
        
class Conjunction(Module):
    
    def __init__(self, name: str):
        super().__init__(name)
        self.linked_from = {}
    
    def add_link_from(self, name: str):
        self.linked_from[name] = False #Necessary for remembering all recived pulses
    
    def recive_pulse(self, pulse: bool, name: str):
        self.linked_from[name] = pulse #Save last recived pulse
    
    def send_pulses(self):
        pulse = False #Send Low pulse if all remembered recived pulses are High
        for remember in self.linked_from.values():
            if not remember:
                pulse = not pulse #Send High pulse if at least one remembered recived pulses are Low
                break
        for module in self.linked_to:
            module.recive_pulse(pulse, self.name)
            if pulse:
                self.high_sended += 1
            else:
                self.low_sended += 1
                print(f"{self.name} {self.linked_from}")

class Broadcaster(Module):

    def add_link_from(self, name: str):
        pass #Not necessary

    def recive_pulse(self, pulse: bool, name: str):
        pass #Not necessary

    def send_pulses(self):
        for module in self.linked_to:
            module.recive_pulse(False, self.name) #Button send low pulse (False) and broadcaster always send low pulse (False)
            self.low_sended += 1

class EndModule(Module):

    def __init__(self, name: str):
        super().__init__(name)
        self.low_pulse_recived = 0 #If this module is RX, print solution when it recives a low pulse

    def add_link_from(self, name: str):
        pass #Not necessary

    def recive_pulse(self, pulse: bool, name: str):
        if not pulse:
            self.low_pulse_recived += 1

    def send_pulses(self):
        pass #Not necessary

if __name__ == "__main__":

    with open(Path("2023","day_20.txt")) as input_file:
        all_comunication = [row for row in input_file.read().split("\n")]
    
    all_modules = {}

    for module in all_comunication:
        name, linked_to = module.split(" -> ")
        if name == "broadcaster":
            all_modules[name] = Broadcaster(name)
        else:
            module_type = name[:1]
            name = name[1:]
            if module_type == '%':
                all_modules[name] = FlipFlop(name)
            else:
                all_modules[name] = Conjunction(name)
        all_modules[name].temp_link = linked_to
    
    temp_end_module = {}

    for module in all_modules.values():
        linked_to = module.temp_link.split(", ")
        for link in linked_to:
            if link in all_modules:
                module.add_link_to(all_modules[link])
            else:
                temp_end_module[link] = EndModule(link)
                module.add_link_to(temp_end_module[link])
        del module.temp_link
    for name, module in temp_end_module.items():
        all_modules[name] = module
    del temp_end_module
    
    all_modules['button'] = Broadcaster("button")
    all_modules['button'].add_link_to(all_modules['broadcaster'])

    counter = 0
    while counter < 1000:
        queue = [all_modules["button"]]
        counter += 1
        while len(queue) > 0:
            temp_queue = []
            for pulse_to_send in queue:
                pulse_to_send.send_pulses()
                if all_modules['rx'].low_pulse_recived == 1:
                    sum_low_2 = 0
                    sum_high_2 = 0
                    for module in all_modules.values():
                        sum_low_2 += module.low_sended
                        sum_high_2 += module.high_sended
                for sender in pulse_to_send.linked_to:
                    if sender.can_send_pulse:
                        temp_queue.append(sender)
            queue = copy(temp_queue)

    sum_low_1 = 0
    sum_high_1 = 0
    for module in all_modules.values():
        sum_low_1 += module.low_sended
        sum_high_1 += module.high_sended
    print(f"Solution 1: {sum_low_1 * sum_high_1}")
    print(f"Solution 2: {sum_low_2 * sum_high_2}")