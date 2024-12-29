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

levels=0
while que:
    levels+=1
    line=que.popleft()
    if line[0] in gate and line[2] in gate:
        process(line)
    else:
        que.append(line)


zgatekey="z{num:02d}"
xgatekey="x{num:02d}"
ygatekey="y{num:02d}"
res=""
for i in range(len(gate.keys()),-1,-1):
    zkey=zgatekey.format(num=i)
    if zkey in gate:
        res+=str(gate[zkey])

yrow=""
for i in range(len(gate.keys()),-1,-1):
    ykey=ygatekey.format(num=i)
    if ykey in gate:
        yrow+=str(gate[ykey])

xrow=""
for i in range(len(gate.keys()),-1,-1):
    xkey=xgatekey.format(num=i)
    if xkey in gate:
        xrow+=str(gate[xkey])

print(xrow)
print(yrow)
print(res)
test=int(xrow,2) + int(yrow,2)
print(bin(test)[2:])


print(int(res,2))


incorrect=[]
for index,(correct,actual) in enumerate(zip(bin(test)[2:],res)):

    if correct != actual:
        #print(zgatekey.format(num=index))
        incorrect.append(zgatekey.format(num=index))
    else:
        #print(zgatekey.format(num=index),'match')
        pass


print(len(incorrect))
print(levels)