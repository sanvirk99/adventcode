
import re
import heapq
from collections import defaultdict 


si,sj=0,0
ei,ej=70,70
scanNums=r"\d+"
cord = [['.' for x in range(ei+1)] for j in range(ej+1)]
count=0
remaining=[]
with open('input/day18.txt','r') as f:

    for line in f:
        
        x,y=re.findall(scanNums,line)
        if count >= 1024:
            remaining.append((int(x),int(y)))
            continue
        cord[int(x)][int(y)]='#'
        count+=1

def draw():
    for row in cord:
        print(''.join(row))


def part1():
    dist = defaultdict(lambda : float('inf'))
    parent={}
    dist[si,sj]=0
    que=[]
    heapq.heappush(que,(dist[si,sj],si,sj))
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    while que:
        d,x,y=heapq.heappop(que)
        for dir in directions:
            di,dj=dir
            i,j=x+di,y+dj
            if not (0 <= i < len(cord) and 0 <= j < len(cord[0])) or cord[i][j] == '#':
                continue
            if d + 1 < dist[i,j]:
                dist[i,j]=d+1
                parent[i,j]=(x,y)
                heapq.heappush(que,(dist[i,j],i,j))
    # if dist[ei,ej] == float('inf'):
    #     draw()

    stack=[(ei,ej)]
    visited=set()
    while stack:
        x,y=stack.pop()
        if (x,y) in visited:
            continue
        visited.add((x,y))
        if (x,y) not in parent:
            break
        stack.append(parent[x,y])
    
    return dist[ei,ej],visited

steps,path = part1()
print(steps)


##part 2
#another approach is to just do a dfs from the end to start or start to end after adding
# the cordinate
res=None
for byte in remaining:

    x,y = byte
    cord[x][y] = '#'
    if (x,y) not in path:
        continue
    steps,path=part1()
    #print(steps)
    if steps == float('inf'):
        res=(x,y)
        break

print(res)


