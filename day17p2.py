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

program_string=''.join(map(str,ops))
ops = [[ops[i], ops[i+1]] for i in range(0, len(ops), 2)]

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

rop = {v: k for k, v in opcode_mapping.items()}


def guess(num):
    global instruction_pointer
    global outs
    global store

    instruction_pointer=0
    store=storecopy
    store[0]=num
    #print(store)
    outs=[]
    while 0 <= instruction_pointer < len(ops):
        opcode,oprand=ops[instruction_pointer]
        opcode_functions[opcode](oprand)
 

def out(n):
    print(n,bin(n)[2:])



res=0
calls=0
def dfs(binary,i):
    global calls
    calls+=1
    if i == len(program_string):
        global res
        res+=1 
        print(binary)  
        print(int(binary,2))
        print(outs)        
        return
    
    for j in range(8):
        test=binary+bin(j)[2:].zfill(3)
        guess(int(test,2))
        if outs[0] == int(program_string[-(i+1)]):
            dfs(test,i+1)

dfs('11',1)
print(res)
print(calls)
exit()


    

#trail and error until finding out mutliple choices for vaild answer so
#recursive solution was natural to test all paths

# #guess(51342988//8//8//8//8//8)
# #print(51342988//8//8//8//8//8)
# # guess(3)
# # guess(24)
# # guess(196)
# # guess(1573)
# #2413754013035530
# target="11"
# # print(program_string)
# for i in range(1,len(program_string)):

#     print(target)
#     flag=False
#     for j in range(0,8):

#         test=target+bin(j)[2:].zfill(3)
#         #print(test)
#         guess(int(test,2))

#         if i == 9 and j == 4:
#             print('before fail')
#             continue
#         # if i == 10 and j == 5:
#         #     continue

        
#         if outs[0] == int(program_string[-(i+1)]):
#             print('match',int(test,2))
#             target=test
#             flag=True
#             break
#     if flag == False:
#         print('fail',target, i,j)
#         print(outs)
#         exit()
   

# print(len(target)//2)
# print(int(target,2))

# print(outs)    
    

# # for i in range(8):

# #     print(bin(i)[2:].zfill(3))

# # print(bin(store[0]))
# # binary=bin(store[0])
# # print(binary[1])
# # for i in range(0,len(binary)-2,3):
# #     print(binary[i],binary[i+1],binary[i+2])
# #     str=binary[i]+


# # guess((3*8*8))
# # print(3*8*8)
# # guess(192//8)


# # count=90
# # guess(count)
