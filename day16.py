import sys
file = open('input/day16.txt','r')

input=[]
with file as f:
    for line in f:
        line = line.strip()
        row=[]
        for e in line:
            row.append(e)
        input.append(row)


def draw():
    for row in input:
        print(''.join(row))



directions={
    'u':(-1,0),
    'd':(1,0),
    'l':(0,-1),
    'r':(0,1)
}

symbol={
    'u':'^',
    'd':'v',
    'l':'<',
    'r':'>'
}

opposite={
    'u':'d',
    'd':'u',
    'l':'r',
    'r':'l'
}

startx, starty = 0,0
endx, endy = 0,0
for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == 'S':
            startx,starty=i,j
        if input[i][j] == 'E':
            endx,endy=i,j
def part1Test():
    mem={}
    path=[]
    paths=[]
    mincost=sys.maxsize
    def dfs(i,j,dir,cost):
        nonlocal mincost
        
        if input[i][j] == '#': 
            return False
        
        if input[i][j] == 'E':
            if mincost > min(mincost,cost):
                #draw()
                paths.append(path.copy())
                mincost=min(mincost,cost)
            return True
        
        if input[i][j] in symbol.values():
            return False
        
        mem[(i,j)] = []
        path.append(f"({i},{j}) {symbol[dir]} {cost}")
        prev=input[i][j]    
        input[i][j]=symbol[dir]
        count=0
        for key,value in directions.items():

            x,y = value
            res=False
            movecost=0
            if dir == key: # same directoin
                movecost=cost+1
            else:
                movecost=cost+1000
            
            res=dfs(i+x,j+y,key,movecost)
            if res:
               mem[(i,j)].append(movecost)
               count+=1

        input[i][j]=prev
        path.pop()
        if count > 0:
            return  True
        return False
    



    isValid=dfs(startx,starty,'r',0)
    if isValid:
        for each in paths[-1]:
            print(each)
        print(len(paths[-1]))
    print(mincost)

class Node:
    def __init__(self,x,y,cost=sys.maxsize,direction=None,parent=None):
        self.x=x
        self.y=y
        self.cost=cost
        self.parent=parent
        self.direction=direction
    

import heapq
from collections import defaultdict
def part1():
    def createGraph():
        nodes={}
        for i in range(len(input)):
            for j in range(len(input[0])):
                if input[i][j] == 'S':
                    nodes[(i,j)]=Node(i,j,0,'r')
                if input[i][j] == '.':
                    nodes[(i,j)]=Node(i,j)
                if input[i][j] == 'E':
                    nodes[(i,j)]=Node(i,j)
                        
        return nodes
    
    nodes=createGraph()
    heap=[]
    heapq.heappush(heap,(0,(startx,starty)))
    # for key in nodes:
    #     heapq.heappush(heap,(nodes[key].cost,key))
    visited=set()
    while heap:
        u=heapq.heappop(heap)
        if u[1] in visited:
            continue
        visited.add(u[1])
        cur=nodes[u[1]]
        for dir in directions:
            x,y=directions[dir]
            x,y=cur.x+x,cur.y+y
            if (x,y) not in nodes:
                continue
            if dir == cur.direction and nodes[(x,y)].cost > cur.cost+1:
                nodes[(x,y)].cost=cur.cost+1
                nodes[(x,y)].parent=cur
                nodes[(x,y)].direction=dir
                
            elif dir != cur.direction and nodes[(x,y)].cost > cur.cost+1000+1:
                nodes[(x,y)].cost=cur.cost+1000+1
                nodes[(x,y)].parent=cur
                nodes[(x,y)].direction=dir

            heapq.heappush(heap,(nodes[(x,y)].cost,(x,y)))
  
    print(nodes[(endx,endy)].cost)  
    
        
part1()

import heapq
sd = 0
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def adjs(cur):
    cx,cy,dir = cur

    yield 1000, (cx,cy,((dir+1)%4))
    yield 1000, (cx,cy,((dir-1)%4))
    dx,dy = dirs[dir]
    fx,fy=cx+dx,cy+dy
    if input[fx][fy] != '#':
        yield 1,(fx,fy,dir)


start = (startx,starty,0)
heap = []
heapq.heappush(heap,(0,start))
dists = defaultdict(lambda: float('inf'))
parents = defaultdict(lambda: set())

while heap:
    dist,cur = heapq.heappop(heap)
    (cx,cy,dir) = cur
    if cur == (endx,endy):
        continue
    for d,adj in adjs(cur):
        if dist + d < dists[adj]:
            dists[adj] = dist + d
            parents[adj]={cur}
            heapq.heappush(heap,(dist+d,adj))
        elif dist + d == dists[adj]:
            parents[adj].add(cur)

for dir in range(4):
    print(dists[(endx,endy,dir)])
stack = [(endx,endy,1)]
visited = set(stack)
while stack:
    cur = stack.pop()
    for parent in parents[cur]:
        if parent not in visited:
            stack.append(parent)
            visited.add(parent)

visited = set(x[:2] for x in visited)
print(len(visited))