
import re
from collections import defaultdict
register = r"Register [A-C]: \d+"

program = r"Program: \d+"

store=[]
ops=[]

with open('input/day17.txt','r') as f:
    lines = f.readlines()
    for line in lines:

        if(re.match(register,line)):
            store.append(int(re.search(r"\d+",line).group()))
        if(re.match(program,line)):
            ops=list(map(int,re.findall(r"\d+",line)))

print(store)
program_string=','.join(map(str,ops))
ops = [[ops[i], ops[i+1]] for i in range(0, len(ops), 2)]
print(ops)
storecopy=store.copy()
regisMap={
    'A' : 0,
    'B' : 1,
    'C' : 2,
}

def comboOpRegister(op):

    if op in range(4,7):
        return store[op-4]
    return op            

instruction_pointer=0
outs=[]

# Define functions for each opcode
def adv(op):
    num=store[regisMap['A']]
    den=2 ** comboOpRegister(op) 
    res=num//den
    store[regisMap['A']]=res
    
    global instruction_pointer
    instruction_pointer+=1

def bxl(op):
    num=store[regisMap['B']]
    xor=num ^ comboOpRegister(op) 
    store[regisMap['B']]=xor
    global instruction_pointer
    instruction_pointer+=1
    
def bst(op):
    res=comboOpRegister(op) %8
    store[regisMap['B']]=res
    global instruction_pointer
    instruction_pointer+=1

def jnz(op):
    global instruction_pointer
    if store[regisMap['A']]==0:
        instruction_pointer+=1
        return
    instruction_pointer=comboOpRegister(op) 

def bxc(op):
    xor=store[regisMap['B']] ^ store[regisMap['C']]
    store[regisMap['B']]=xor
    global instruction_pointer
    instruction_pointer+=1
        
def out(op):
    outs.append(comboOpRegister(op)%8)
    global instruction_pointer
    instruction_pointer+=1
    

def bdv(op):
    num=store[regisMap['A']]
    den=2 ** comboOpRegister(op)  
    res=num//den
    store[regisMap['B']]=res
    global instruction_pointer
    instruction_pointer+=1

def cdv(op):
    num=store[regisMap['A']]
    den=2 ** comboOpRegister(op)  
    res=num//den
    store[regisMap['C']]=res
    global instruction_pointer
    instruction_pointer+=1

# Dictionary of functions
opcode_functions = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv,
}

opcode_mapping = {
    0: 'adv',
    1: 'bxl',
    2: 'bst',
    3: 'jnz',
    4: 'bxc',
    5: 'out',
    6: 'bdv',
    7: 'cdv',
}

print(program_string)

while 0 <= instruction_pointer < len(ops):
    opcode,oprand=ops[instruction_pointer]
    #print(opcode,oprand)
    opcode_functions[opcode](oprand)
    print(opcode_mapping[opcode],comboOpRegister(oprand), '->' , store, '->', ','.join(map(str,outs) ))



comma_separated_string = ','.join(map(str,outs))
print(comma_separated_string)



# #51000000
# count=51000000
# while True:

#     instruction_pointer=0
#     outs=[]
#     store=storecopy.copy()
#     store[0]=count

#     while 0 <= instruction_pointer < len(ops):
#         opcode,oprand=ops[instruction_pointer]
#         #print(opcode,oprand)
#         opcode_functions[opcode](oprand)
#         # print(instruction_pointer , opcode) 

#     if  program_string == ','.join(map(str,outs)):
#         print(count)
#         print(program_string)
#         break
#     if count%100000 == 0:
#         print(count)
#     count+=1
# print(count , 'register a value')
