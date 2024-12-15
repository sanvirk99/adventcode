# %%
file=open('./input/day14.txt','r')
from functools import reduce
import time
import re
pattern = r'[-]*\d+'

from scipy.stats import zscore

input=[]
with file as f:
    
    for line in file:
        line=line.strip()
        arr=re.findall(pattern,line)
        arr=list(map(int,arr))
        loc=[arr[1],arr[0]]
        v=[arr[3],arr[2]]
        arr={
            'l':loc,
            's':v
        }
        if arr:
            input.append(arr)
#print(input)

# tall=7
# wide=11
tall=103
wide=101



def draw():
    grid = [[' ' for _ in range(wide)] for _ in range(tall)]
    for r in input:
        x,y=r['l']
        grid[x][y]='x'
    
    empty=0
    filled=0
    for row in grid:
        print((' '.join(row)))
        for e in row:
            if e == ' ':
                empty+=1
            if e == 'x':
                filled+=1
    print('empty space ',empty)
    print('filled space ',filled)

def quadrant(x,y):
    
    if x < tall//2 and y < wide//2:
        return 0
    if x > tall//2 and y < wide//2:
        return 2
    if x < tall//2 and y > wide//2:
        return 1
    if x > tall//2 and y > wide//2:
        return 3


def move():
    for i,r in enumerate(input):
        x=r['l'][0]+r['s'][0]
        if x < 0:
            x=x+tall
        if x >= tall:
            x=x-tall
        y=r['l'][1]+r['s'][1]  
        if y < 0:
            y=y+wide
        if y >= wide:
            y=y-wide
        r['l']=[x,y]



def part1():
   
    for i in range(100):
       
        move()

    count=[0]*4
    for r in input:
        x,y=r['l']
        if x == tall//2:
            continue
        if y == wide//2:
            continue
        i=quadrant(x,y)
        count[i]+=1
    #print(count)
    print(reduce(lambda x,y: x*y,count))
    


directions=[]
for i in range(-1,2,1):
    for j in range(-1,2,1):
        if i==0 and j==0:
             continue
        directions.append((i,j))
           

def check():
    grid = [[' ' for _ in range(wide)] for _ in range(tall)]
    for r in input:
        x,y=r['l']
        grid[x][y]='x'
    
    visted=set()
    def dfs(i,j):

        if not (0<= i < len(grid) and 0<= j < len(grid[0])):
            return 0
        
        if (i,j) in visted:
            return 0

        if grid[i][j] == ' ':
            return 0
        visted.add((i,j))
        
        count=1
        for x,y in directions:
            count+=dfs(i+x,j+y)
        
        return count

    count=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != ' ' and (i,j) not in visted:
                count=max(dfs(i,j),count)
    #print(count)
    if count >= 26:
        draw()
        return True
    return False
    



def part2():
    
    count=0
    d=0
    while d<1:
        #print(count)
        move()
        if check():
            d+=1
            print(count)
        count+=1
        #print(d)
    print(count)
    
 

 

start_time = time.time()
#part1()
end_time = time.time()
print(f"part1() execution time: {end_time - start_time} seconds")

start_time = time.time()
part2()
end_time = time.time()
print(f"part2() execution time: {end_time - start_time} seconds")
# %%
