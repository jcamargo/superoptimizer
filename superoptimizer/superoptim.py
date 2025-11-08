# -*- coding: utf-8 -*-
"""
Some motivation paper:
https://web.stanford.edu/class/cs343/resources/superoptimizer.pdf

We consider a fantasy machine close to the Intel 4004

Consider the 7 bit representation:
    _________________    
   |CF |ACC |R0 |R1 |
   | 1 |  2 | 2 | 2 |
   \_______________/
   
     The carry flag has 1 bit repr and all others have 2 bit
     
The resulting state has 7 bits (1 byte)

Each operation is a function from the domain 2^7 to possible 2^7 states
For instance, the NOP function is the identity
The function that clears the CF takes [cf, acc, r0, r1] to [0, acc, r0, r1]

In order to define a function we have two possible ways:
    - Function definition, as given by tests or by the assembly manual
    - Extensive enumeration, a brute-force application of the emulated
      function in all possible states
      
      This requires a 128 byte sequece
      
Each assembly operation generates an edge that connects these 128 byte nodes
Needless to say, there are many possible nodes in this graph:
    
    128^128 possible nodes
    
Created on Sat Nov  8 13:53:37 2025

@author: julia
"""
import numpy as np
from dataclasses import dataclass, astuple

@dataclass(order=True)
class CPU_state_layout:
    szCY: int
    szAcc: int
    szR0: int
    szR1: int

toy_4004 = CPU_state_layout(1, 2, 2, 2)
toy_4004_arr = np.array(astuple(toy_4004))

# Form proper flags from this layout
CPU_st_bit_b = np.flip(toy_4004_arr).cumsum()
szCPUstate = toy_4004_arr.sum()
# We will work with arrays of 128 states

iota_st = np.arange(2**szCPUstate)





