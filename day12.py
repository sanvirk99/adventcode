# %%
file=open('./input/day12.txt','r')
import time

input=[]
with file as f:
    
    for line in file:
        line=line.strip()
        row=[]
        for e in line:
            if e == '.':
                row.append(-1)
                continue
            row.append(e)
        input.append(row)
#print(input)

# rigth,down,left,up
direction=[(0,1),(1,0),(0,-1),(-1,0)]

def part1():

    visited={}
    processed=set()
    #cordinate = negibours #assume 4 0 contribution only and if out of bounds
    def dfs(i,j,prev):
        if (i,j) in visited:
            return 0

        if not (0<= i < len(input) and 0 <= j < len(input[0])):
            return 1

        if prev != input[i][j]:
            return 1
        
        visited[(i,j)]=0
        count=0
        for dir in direction:
            x,y=dir
            count+=dfs(i+x,j+y,input[i][j])

        visited[(i,j)]=count
        #processed
        processed.add((i,j))
        return 0

    cost=0
    for i in range(len(input)):
        for j in range(len(input[0])):
            visited={}
            if (i,j) in processed:
                continue
            dfs(i,j,input[i][j])

            permitter=sum(visited.values())
            area=len(visited)
            #print(permitter*area)
            cost+=permitter*area
    print(cost)



    
def part2():
    visited={}
    processed=set()
    sides = {}
    #cordinate = negibours #assume 4 0 contribution only and if out of bounds
    def dfs(i,j,prev,dir):
        if (i,j) in visited:
            return 0

        if not (0<= i < len(input) and 0 <= j < len(input[0])):
            sides[dir].add((i,j))
            return 1

        if prev != input[i][j]:
            sides[dir].add((i,j))
            return 1
        
        visited[(i,j)]=0
        count=0
        for dir in direction:
            x,y=dir
            count+=dfs(i+x,j+y,input[i][j],dir)

        visited[(i,j)]=count
        #processed
        processed.add((i,j))
        return 0
    
    def countSides():
        
        for key in sides:
            set_sides=sides[key].copy()
            for side in set_sides:
                x,y=side
                if (x,y) not in sides[key]:
                    continue #already removed
                xk,yk=key
                if xk == 0:
                    dxn,dxp=x,x
                    while (dxn-1,y) in sides[key] or (dxp+1,y) in sides[key]:
                        if (dxn-1,y) in sides[key]:
                            dxn-=1
                            sides[key].remove((dxn,y))
                        if (dxp+1,y) in sides[key]:
                            dxp+=1
                            sides[key].remove((dxp,y))

                if yk == 0:
                    dyn,dyp=y,y
                    while (x,dyn-1) in sides[key] or (x,dyp+1) in sides[key]:
                        if (x,dyn-1) in sides[key]:
                            dyn-=1
                            sides[key].remove((x,dyn))
                        if (x,dyp+1) in sides[key]:
                            dyp+=1
                            sides[key].remove((x,dyp))
                        


                        
                

    cost=0
    for i in range(len(input)):
        for j in range(len(input[0])):
            visited={}
            for dir in direction:
                sides[dir]=set()
            if (i,j) in processed:
                continue
            dfs(i,j,input[i][j],(i,j))
           # print(input[i][j], '/////////')
            permitter=sum(visited.values())
            area=len(visited)
            #print(sides)
            countSides()
            #print(sides)
            count=len([x for xx in sides.values() for x in xx])
            #print(count)
            cost+=area*count

    print(cost)

start_time = time.time()
part1()
end_time = time.time()
print(f"part1() execution time: {end_time - start_time} seconds")

start_time = time.time()
part2()
end_time = time.time()
print(f"part2() execution time: {end_time - start_time} seconds")