input=[]
file=open('input/day20.txt')
startx, starty = 0,0
endx, endy = 0,0
with file as f:
    for line in f:
        line = line.strip()
        row=[]
        for e in line:
            row.append(e)
        input.append(row)

for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == 'S':
            startx,starty=i,j
        if input[i][j] == 'E':
            endx,endy=i,j

def draw(input):
    for row in input:
        print(''.join(row))


#draw()

directions=[(0,1),(1,0),(0,-1),(-1,0)]
from collections import defaultdict
import heapq
def dijkstra(input):
    global startx,starty,endx,endy
    dist=defaultdict(lambda : float('inf'))
    dist[startx,starty]=0
    parent={}
    que=[]
    heapq.heappush(que,(0,startx,starty))

    while que:
        d,ci,cj=heapq.heappop(que)
        for dir in directions:
            i,j=dir
            i,j=ci+i,cj+j
            if not (0 <= i < len(input) and 0 <= j < len(input[0])) or input[i][j] == '#':
                continue
            if d + 1 < dist[i,j]:
                dist[i,j] = d + 1
                parent[i,j]=(ci,cj)
                heapq.heappush(que,(dist[i,j],i,j))
    
    stack=[(endx,endy)]
    visited=set()
    while stack:
        x,y=stack.pop()
        if (x,y) in visited:
            continue
        visited.add((x,y))
        if (x,y) not in parent:
            break
        stack.append(parent[x,y])
    return visited,dist

#print(dijkstra(copy.deepcopy(input)))
orginal_path,dist=dijkstra(input)
#idea is to relax past a edge and see if leads to reduce time
total=dist[endx,endy]



# def cheatcords(ci,cj):

#     visted=set()
#     def dfs(time):
#         nonlocal ci,cj
#         di,dj = cur
#         if time <= 0:
#             return
#         if cur in visted:
#             return
#         visted.add(cur)
#         if dist[ci,cj]+time < dist[di,dj]: 
#             shortcut[(dist[di,dj] - (dist[ci,cj]+time))]+=1
#         for dir in directions:
#             i,j=dir
#             dfs(time-1,(cur[0]+i,cur[1]+j))

#     dfs(20)

cheatspace=defaultdict(lambda: [])

for i in range(-20,21):
    for j in range(-20,21):
        if abs(i) + abs(j) <= 20 and (abs(i) >= 2 or abs(j) >=2):
            cheatspace[abs(i) + abs(j)].append((i,j))



def part1():
    shortcut=defaultdict(lambda : 0)
    for cord in orginal_path:
        ci,cj=cord
        for dir in directions:
            i,j=dir
            i*=2
            j*=2    
            di,dj=ci+i,cj+j
            if (di,dj) not in dist: #another wall
                continue
            if dist[ci,cj]+2 < dist[di,dj]: 
                shortcut[(dist[di,dj] - (dist[ci,cj]+2))]+=1


    cheats=0
    for key in shortcut:

        if key >= 100:
            cheats+=shortcut[key]

    print(cheats) 


def calculateCord(cord,i,j):
    ci,cj=cord
    ci=i+ci
    cj=j+cj
    return ci,cj

def part2():
    cheats=defaultdict(lambda: 0)
    def bestincheatspace(cord):
        ci,cj=cord

        
        for key in cheatspace:
            for point in cheatspace[key]:
                i,j=point
                di,dj = calculateCord(cord,i,j)
                if (di,dj) not in dist: #another wall
                    continue
                if dist[ci,cj]+key < dist[di,dj]: 
                    cheats[(dist[di,dj] - (dist[ci,cj]+key))]+=1



    for cord in orginal_path:
        bestincheatspace(cord)

    keys = sorted(cheats.keys(),reverse=True)
    part2=0
    for cheat in keys:
        if cheat>=100:
            part2+=cheats[cheat]
        else:
            break
    print(part2)


part1()
part2()