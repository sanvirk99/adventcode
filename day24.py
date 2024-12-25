import re
from collections import deque
gate = {}


def AND(x,y):
    return x & y
def OR(x,y):
    return x | y
def XOR(x,y):
    return x ^ y 

operations = {
    'XOR' : XOR,
    'OR' : OR,
    'AND': AND
}

def process(line):
    x = gate[line[0]]
    y = gate[line[2]]
    op = operations[line[1]]
    gate[line[3]] = op(x,y)
    

que=deque()
with open('input/day24.txt','r') as f:
    for line in f:
        line=re.findall(r"\w+",line)
        if len(line) == 2:
            gate[line[0]] = int(line[1])
        if len(line) == 4:
            if line[0] in gate and line[2] in gate:
                process(line)
            else:
                que.append(tuple(line))

while que:
    line=que.popleft()
    if line[0] in gate and line[2] in gate:
        process(line)
    else:
        que.append(line)


gatekey="z{num:02d}"
res=""
for i in range(len(gate.keys()),-1,-1):
    zkey=gatekey.format(num=i)
    if zkey in gate:
        res+=str(gate[zkey])

print(int(res,2))