from braket.circuits import Circuit, Gate, Noise, Observable, Instruction
from braket.devices import LocalSimulator
from braket.circuits.noise_model import (GateCriteria, NoiseModel,
                                         ObservableCriteria)
from braket.circuits.noises import (AmplitudeDamping, BitFlip, Depolarizing,
                                    PauliChannel, PhaseDamping, PhaseFlip,
                                    TwoQubitDepolarizing)
import random
import math as m 
import numpy as np

import time

def QRC(N,D, max_gates):
  # N = number of qubits
  # D = depth
  # noise_model = build a noise model separately and use as input
  # max_gates = allows to use gates of 1, 2 and 3 qubits (input = 1,2,3).
  # For example, if we put max_gates = 2, it will only allow 1 and 2 qubit gates.
  # Gates we could use. We can add or take off gates, if we want to restric to simpler gates sets.
  # print("Creating lists of gates and circuit")
  Gate_Names_1q = [ 'H','PhaseShift', 'Rx', 'Ry', 'Rz', 'S', 'Si',  'T', 'Ti', 'V', 'Vi', 'X',  'Y',  'Z']
  Gate_Names_2q = ['ECR', 'CNot', 'CPhaseShift', 'CPhaseShift00', 'CPhaseShift01', 'CPhaseShift10', 'CV', 'CY', 'CZ','Swap','XX', 'XY', 'ZZ','YY']
  Gate_Names_3q = ['CCNot', 'CSwap']
  # Create circuit:
  circ = Circuit()
  # We first iterate through the circuit depth:
  #print("Generating Instructions")  
  for _ in range(D):
      # Generate a list of (randomly chosen) 1 and 2 qubits choices and
      # an empty list to be filled with instructions.
      L = []
      r = range(N)
      qubits_numbers = list(r)
      choices = []
      if max_gates == 3:
         while 2<len(qubits_numbers):
            a = random.randint(1, 3)
            b = random.sample(qubits_numbers, k=a)
            choices.append(b)
            for x in b:
                qubits_numbers.remove(x)
         while 1<len(qubits_numbers):
            a = random.randint(1, 2)
            b = random.sample(qubits_numbers, k=a)
            choices.append(b)
            for x in b:
                qubits_numbers.remove(x)
         if 0<len(qubits_numbers):
            choices = choices + [[qubits_numbers[0]]]
      elif max_gates == 2:
         while 1<len(qubits_numbers):
            a = random.randint(1, 2)
            b = random.sample(qubits_numbers, k=a)
            choices.append(b)
            for x in b:
                qubits_numbers.remove(x)
         if 0<len(qubits_numbers):
            choices = choices + [[qubits_numbers[0]]]
      elif max_gates == 1:
         while 0<len(qubits_numbers):
         # At this point, in this case, one could just iterate over all qubits...
         # But this gives the same result, and makes the relation to the other cases clearer.
            b = random.sample(qubits_numbers, k=1)
            choices.append(b)
            for x in b:
                qubits_numbers.remove(x)           
      # Now we use the list choices to generate the corresponding random gates.        
      for x in choices:        
         if len(x) == 1:
            a = "Gate."
            b = random.choice(Gate_Names_1q)
            if b == "Rz":
               angle =  2*(m.pi)*(random.random())
               c = a+b+"(str(angle))"
               d = Instruction(eval(c),x)
            elif b == "Rx":
               angle =  2*(m.pi)*(random.random())
               c = a+b+"(str(angle))"
               d = Instruction(eval(c),x)
            elif b == "Ry":
               angle =  2*(m.pi)*(random.random())
               c = a+b+"(str(angle))"
               d = Instruction(eval(c),x) 
            elif b == "PhaseShift":
               angle =  2*(m.pi)*(random.random())
               c = a+b+"(str(angle))"
               d = Instruction(eval(c),x) 
            else:          
               c = a+b+"()"
               d = Instruction(eval(c),x)          
            L.append(d)
         elif len(x) == 2:   
            a = "Gate."
            b = random.choice(Gate_Names_2q)
            if b == "Rz":
               angle =  2*(m.pi)*(random.random())
               c = a+b+"(str(angle))"
               d = Instruction(eval(c),x)
            elif b == 'CPhaseShift':
               angle =  2*(m.pi)*(random.random())
               c = a+b+"(str(angle))"
               d = Instruction(eval(c),x)
            elif b == 'CPhaseShift00':
               angle =  2*(m.pi)*(random.random())
               c = a+b+"(str(angle))"
               d = Instruction(eval(c),x)   
            elif b == 'CPhaseShift10':
               angle =  2*(m.pi)*(random.random())
               c = a+b+"(str(angle))"
               d = Instruction(eval(c),x)
            elif b == 'CPhaseShift01':
               angle =  2*(m.pi)*(random.random())
               c = a+b+"(str(angle))"
               d = Instruction(eval(c),x)   
            elif b == 'XX':
               angle =  2*(m.pi)*(random.random())
               c = a+b+"(str(angle))"
               d = Instruction(eval(c),x)         
            elif b == 'YY':
               angle =  2*(m.pi)*(random.random())
               c = a+b+"(str(angle))"
               d = Instruction(eval(c),x) 
            elif b == 'ZZ':
               angle =  2*(m.pi)*(random.random())
               c = a+b+"(str(angle))"
               d = Instruction(eval(c),x)     
            elif b == 'XY':
               angle =  2*(m.pi)*(random.random())
               c = a+b+"(str(angle))"
               d = Instruction(eval(c),x)                     
            else:          
               c = a+b+"()"
               d = Instruction(eval(c),x)          
            L.append(d)
         elif len(x) == 3:   
            a = "Gate."
            b = random.choice(Gate_Names_3q)     
            c = a+b+"()"
            d = Instruction(eval(c),x)          
            L.append(d) 
      # print("Generating Ideal Circuit")                 
      for x in L:
         circ.add_instruction(x)
  # Now we compute the density matrix associated to the circuit (first, without noise):   
  # print("Computing Ideal DM")
  circ.density_matrix(target=range(N))   
  device = LocalSimulator(backend="braket_dm")
  task = device.run(circ, shots=0)
  result = task.result()
  RHO = result.values[0]
  dic = {"Ideal Circuit":circ, "Ideal RHO": RHO}        
  return dic