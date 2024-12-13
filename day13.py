# %%
file=open('./input/day13.txt','r')
import numpy as np
import re
import time
import sys

pattern = r'\d+'

input=[]
with file as f:
    
    for line in file:
        line=line.strip()
        arr=re.findall(pattern,line)
        if arr:
            input.append(arr)
       
#print(input)
inputlist=[]
for i in range(0,len(input),3):
    #print(input[i],input[i+1],input[i+2])
    dic={
        'a':list(map(int,input[i])),
        'b':list(map(int,input[i+1])),
        'p':list(map(int,input[i+2]))
    }

    inputlist.append(dic)


def part1():
    
    cur={}
    cache={}
    
    def dfs(x,y,a,b):

        if (x,y) in cache:
            return cache[x,y]

        if not (0<=x<=cur['p'][0] and 0<=y<=cur['p'][1]):
            return sys.maxsize
        if x == cur['p'][0] and y == cur['p'][1]:
            return a*3 + b
        
        ba=dfs(x+cur['a'][0],y+cur['a'][1],a+1,b)
        bb=dfs(x+cur['b'][0],y+cur['b'][1],a,b+1)
        cache[x,y]=min(ba,bb)
        return min(ba,bb)
    total=0 
    for x in inputlist:
        cur=x
        cache={}
        cost=dfs(0,0,0,0)
        if cost == sys.maxsize:
            continue
        total+=cost

    print(total)
    return total

#iteratice solution using stack
def part2Iterative():
    
    cur={}
    
    
    
    def dfs(x,y,a,b):

        stack=[]
        stack.append((x,y,a,b))
        cache={}
        while stack:
            x,y,a,b = stack.pop()

            if (x,y) in cache:
                continue
            if not (0<=x<=cur['p'][0] and 0<=y<=cur['p'][1]):
                cache[(x, y)] = sys.maxsize
                continue
            if x == cur['p'][0] and y == cur['p'][1]:
                cache[(x,y)] = a * 3 + b
                continue

            ba = cache.get((x + cur['a'][0], y + cur['a'][1]), None)
            if ba is None:
                stack.append((x, y, a, b))
                stack.append((x + cur['a'][0], y + cur['a'][1], a + 1, b))
                continue
            
            bb = cache.get((x + cur['b'][0], y + cur['b'][1]), None)
            if bb is None:
                stack.append((x, y, a, b))
                stack.append((x + cur['b'][0], y + cur['b'][1], a, b + 1))
                continue

            cache[(x, y)] = min(ba, bb)
         
        return cache[0,0]
            
    total=0 
    for x in inputlist:
        cur=x
        cur['p'][0]=cur['p'][0]+10000000000000
        cur['p'][1]=cur['p'][1]+10000000000000
        cost=dfs(0,0,0,0)
        if cost == sys.maxsize:
            continue
        total+=cost
        
    print(total)
    return total


#linear quation
def part2():

    #Ax=B -> A^Ax=A^B = x=A^B
    def solve(cur):
        A = np.matrix([cur['a'],cur['b']]).T
        B = np.matrix([[cur['p'][0]],[cur['p'][1]]])
        # print(A)
        # print(B)

        X = np.linalg.solve(A, B)
       # print(X)
        
        a=round(X[0,0]) 
        b=round(X[1,0])
        if cur['a'][0]*a + cur['b'][0]*b == cur['p'][0] and cur['a'][1]*a + cur['b'][1]*b == cur['p'][1]:

            return 3*a + b
        
        return 0
    

    total=0
    for x in inputlist:
        cur=x
        cur['p'][0]=cur['p'][0]+10000000000000
        cur['p'][1]=cur['p'][1]+10000000000000
        cost=solve(cur)
        total+=cost
        
    print(total)
    return total



# start_time = time.time()
# part1()
# end_time = time.time()
# print(f"part1() execution time: {end_time - start_time} seconds")

start_time = time.time()
part2()
end_time = time.time()
print(f"part2() execution time: {end_time - start_time} seconds")