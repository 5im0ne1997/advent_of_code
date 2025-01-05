from pathlib import Path
from abc import ABC, abstractmethod
from copy import copy

#Create a Little-Endian like list, so the least significant byte is stored at the lowest index of the list
def IntToBit(number: int) -> list:
    bitnnumber = bin(number)
    bit16number = [0 for n in range(16)]
    index = -1
    for n in range(number.bit_length()):
        bit16number[n] = int(bitnnumber[index - n])
    return bit16number

#Convert bit list to int
def BitToInt(bitnumber: list) -> int:
    number = 0
    for i, n in enumerate(bitnumber):
        number += pow(2,i) * n
    return number
    
#Create Gates class for manage bitwise operation in Little-Endian mode

class Gate(ABC):
    
    def __init__(self):
        super().__init__()
        self.connected_from = []
        self.connected_to = []
        self.signals_recived = 0

    @abstractmethod
    def send_signal(self):
        pass

    def add_connection_to(self, connect_to: object):
        self.connected_to.append(connect_to)

    def add_connection_from(self, connect_from: object):
        self.connected_from.append(connect_from)

    def recive_signal(self):
        self.signals_recived += 1
        return self
    



class AndGate(Gate):

    def __init__(self):
        super().__init__()

    #       [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] (decimal 5)
    #AND    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] (decimal 3)
    #  =    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] (decimal 1)
    def send_signal(self):
        if self.signals_recived == 2:
            gateresult = IntToBit(0)
            for i in range(len(self.connected_from[0].value)):
                if self.connected_from[0].value[i] == self.connected_from[1].value[i]:
                    gateresult[i] = self.connected_from[0].value[i]
                else:
                    gateresult[i] = 0
            self.connected_to[0].set_value(gateresult)
            self.signals_recived = 0
            return self.connected_to[0]

class OrGate(Gate):

    def __init__(self):
        super().__init__()

    #       [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] (decimal 5)
    #OR     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] (decimal 3)
    #  =    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] (decimal 7)
    def send_signal(self):
        if self.signals_recived == 2:
            gateresult = IntToBit(0)
            for i in range(len(self.connected_from[0].value)):
                if self.connected_from[0].value[i] == self.connected_from[1].value[i]:
                    gateresult[i] = self.connected_from[0].value[i]
                else:
                    gateresult[i] = 1
            self.connected_to[0].set_value(gateresult)
            self.signals_recived = 0
            return self.connected_to[0]

class NotGate(Gate):

    def __init__(self):
        super().__init__()

    #NOT    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] (decimal 7)
    #  =    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] (decimal 65528)
    def send_signal(self):
        if self.signals_recived == 1:
            gateresult = IntToBit(0)
            for i in range(len(self.connected_from[0].value)):
                if self.connected_from[0].value[i] == 0:
                    gateresult[i] = 1
                else:
                    gateresult[i] = 0
            self.connected_to[0].set_value(gateresult)
            self.signals_recived = 0
            return self.connected_to[0]

class LShiftGate(Gate):

    def __init__(self, shift: int):
        super().__init__()
        self.shift = shift

    #LSHIFT 1   [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] (decimal 7)
    #       =   [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] (decimal 14)
    #LSHIFT 2   [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] (decimal 7)
    #       =   [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] (decimal 28)
    def send_signal(self):
        if self.signals_recived == 1:
            gateresult = copy(self.connected_from[0].value)
            for i in range(self.shift):
                gateresult.insert(0,0)
                gateresult.pop()
            self.connected_to[0].set_value(gateresult)
            self.signals_recived = 0
            return self.connected_to[0]

class RShiftGate(Gate):

    def __init__(self, shift: int):
        super().__init__()
        self.shift = shift

    #RSHIFT 1   [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] (decimal 7)
    #       =   [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] (decimal 3)
    #RSHIFT 2   [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] (decimal 7)
    #       =   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] (decimal 1)
    def send_signal(self):
        if self.signals_recived == 1:
            gateresult = copy(self.connected_from[0].value)
            for i in range(self.shift):
                gateresult.append(0)
                gateresult.pop(0)
            self.connected_to[0].set_value(gateresult)
            self.signals_recived = 0
            return self.connected_to[0]

class PassGate(Gate):
    def __init__(self):
        super().__init__()
    
    def send_signal(self):
        if self.signals_recived == 1:
            gateresult = self.connected_from[0].value
            self.connected_to[0].set_value(gateresult)
            self.signals_recived = 0
            return self.connected_to[0]

class InitGate(Gate):

    def __init__(self):
        super().__init__()

    def send_signal(self):
        if self.signals_recived == 1:
            gateresult = self.connected_from[0].value
            self.connected_to[0].set_value(gateresult)
            return self.connected_to[0]

class Wire(Gate):
    
    def __init__(self):
        super().__init__()
        self.value = IntToBit(0)

    def send_signal(self):
        pass

    def set_value(self, value: list):
        self.value = value
        

#Class for all object
class All_Object():

    def __init__(self):
        self.wires = {}
        self.gates = {}
        self.init_gates = {}
    
    def add_wire(self, name: str):
        if name not in self.wires:
            self.wires[name] = Wire()
    
    def add_gates(self, name: str, gate: object):
        if name not in self.gates:
            self.gates[name] = gate
    
    def add_init_gates(self, name: str):
        if name not in self.init_gates:
            self.init_gates[name] = InitGate()

#Create variable with input file
with open(Path('2015','day_07.txt')) as file:
    input_file = [[part for part in row.split(' -> ')] for row in file.read().split('\n')]


for part_2 in [False, True]:
    all_object = All_Object()
    for part in input_file:
        wire_name = part[1]
        all_object.add_wire(wire_name)
        gate_name = part[0]
        gate_parts = part[0].split(' ')
        if 'AND' in gate_name:
            all_object.add_gates(gate_name, AndGate())
            all_object.gates[gate_name].add_connection_to(all_object.wires[wire_name])
            all_object.wires[wire_name].add_connection_from(all_object.gates[gate_name])
            a_name = gate_parts[0]
            try:
                int(a_name)
                all_object.gates[gate_name].add_connection_from(Wire())
                all_object.gates[gate_name].connected_from[0].set_value(IntToBit(int(a_name)))
                all_object.gates[gate_name].recive_signal()
            except:
                all_object.add_wire(a_name)
                all_object.gates[gate_name].add_connection_from(all_object.wires[a_name])
                all_object.wires[a_name].add_connection_to(all_object.gates[gate_name])

            b_name = gate_parts[2]
            try:
                int(b_name)
                all_object.gates[gate_name].add_connection_from(Wire())
                all_object.gates[gate_name].connected_from[1].set_value(IntToBit(int(b_name)))
                all_object.gates[gate_name].recive_signal()
            except:
                all_object.add_wire(b_name)
                all_object.gates[gate_name].add_connection_from(all_object.wires[b_name])
                all_object.wires[b_name].add_connection_to(all_object.gates[gate_name])
        elif 'OR' in gate_name:
            all_object.add_gates(gate_name, OrGate())
            all_object.gates[gate_name].add_connection_to(all_object.wires[wire_name])
            all_object.wires[wire_name].add_connection_from(all_object.gates[gate_name])
            a_name = gate_parts[0]
            try:
                int(a_name)
                all_object.gates[gate_name].add_connection_from(Wire())
                all_object.gates[gate_name].connected_from[0].set_value(IntToBit(int(a_name)))
                all_object.gates[gate_name].recive_signal()
            except:
                all_object.add_wire(a_name)
                all_object.gates[gate_name].add_connection_from(all_object.wires[a_name])
                all_object.wires[a_name].add_connection_to(all_object.gates[gate_name])

            b_name = gate_parts[2]
            try:
                int(b_name)
                all_object.gates[gate_name].add_connection_from(Wire())
                all_object.gates[gate_name].connected_from[1].set_value(IntToBit(int(b_name)))
                all_object.gates[gate_name].recive_signal()
            except:
                all_object.add_wire(b_name)
                all_object.gates[gate_name].add_connection_from(all_object.wires[b_name])
                all_object.wires[b_name].add_connection_to(all_object.gates[gate_name])
        elif 'LSHIFT' in gate_name:
            shift = int(gate_parts[2])
            all_object.add_gates(gate_name, LShiftGate(shift))
            all_object.gates[gate_name].add_connection_to(all_object.wires[wire_name])
            all_object.wires[wire_name].add_connection_from(all_object.gates[gate_name])
            a_name = gate_parts[0]
            all_object.add_wire(a_name)
            all_object.gates[gate_name].add_connection_from(all_object.wires[a_name])
            all_object.wires[a_name].add_connection_to(all_object.gates[gate_name])
        elif 'RSHIFT' in gate_name:
            shift = int(gate_parts[2])
            all_object.add_gates(gate_name, RShiftGate(shift))
            all_object.gates[gate_name].add_connection_to(all_object.wires[wire_name])
            all_object.wires[wire_name].add_connection_from(all_object.gates[gate_name])
            a_name = gate_parts[0]
            all_object.add_wire(a_name)
            all_object.gates[gate_name].add_connection_from(all_object.wires[a_name])
            all_object.wires[a_name].add_connection_to(all_object.gates[gate_name])
        elif 'NOT' in gate_name:
            all_object.add_gates(gate_name, NotGate())
            all_object.gates[gate_name].add_connection_to(all_object.wires[wire_name])
            all_object.wires[wire_name].add_connection_from(all_object.gates[gate_name])
            a_name = gate_parts[1]
            all_object.add_wire(a_name)
            all_object.gates[gate_name].add_connection_from(all_object.wires[a_name])
            all_object.wires[a_name].add_connection_to(all_object.gates[gate_name])
        else:
            try:
                int(gate_name)
                all_object.add_init_gates(gate_name)
                all_object.init_gates[gate_name].add_connection_to(all_object.wires[wire_name])
                all_object.wires[wire_name].add_connection_from(all_object.init_gates[gate_name])
                all_object.init_gates[gate_name].add_connection_from(Wire())
                all_object.init_gates[gate_name].connected_from[0].set_value(IntToBit(int(gate_name)))
                all_object.init_gates[gate_name].recive_signal()
            except:
                all_object.add_wire(gate_name)
                all_object.add_gates(gate_name, PassGate())
                all_object.gates[gate_name].add_connection_to(all_object.wires[wire_name])
                all_object.wires[wire_name].add_connection_from(all_object.gates[gate_name])
                all_object.gates[gate_name].add_connection_from(all_object.wires[gate_name])
                all_object.wires[gate_name].add_connection_to(all_object.gates[gate_name])
                
    signal_to_send = [init_gate for init_gate in all_object.init_gates.values()]

    if part_2:
        for gate_name, init_gate in all_object.init_gates.items():
            if all_object.wires['b'] == init_gate.connected_to[0]:
                all_object.init_gates[gate_name].connected_from[0].set_value(IntToBit(int(soluton1)))

    while len(signal_to_send) > 0:
        sended_to_wires = []
        for to_send in signal_to_send:
            to_send = to_send.send_signal()
            if to_send:
                sended_to_wires.append(to_send)
        signal_to_send = []
        for wire in sended_to_wires:
            for gate in wire.connected_to:
                signal_to_send.append(gate.recive_signal())
    if part_2:
        soluton2 = BitToInt(all_object.wires['a'].value)
        print(soluton2)
    else:
        soluton1 = BitToInt(all_object.wires['a'].value)
        print(soluton1)
    

