
# %%
file=open('./input/day8.txt','r')

grid=[]
with file as f:
    
    for line in f:
        line=line.strip()
        row=[]
        for e in line:
            row.append(e)
        grid.append(row)
        # print(row)


map={}
res=set()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != "." and grid[i][j] != "#":
            if grid[i][j] in map:
                map[grid[i][j]].append((i,j))
            else:
                map[grid[i][j]]=[(i,j)]


for locs in map.values():
    
    for i in range(len(locs)):
        for j in range(len(locs)):

            if locs[i] == locs[j]:
                continue
            i1,j1=locs[i]
            i2,j2=locs[j]
            ax,ay=(i2-i1),(j2-j1)
            res.add((i2,j2)) #part 2 addittion
            p1,p2=i2+ax,j2+ay
            while 0 <= p1 < len(grid) and 0 <= p2 < len(grid[0]): # changed for part 2
                res.add((p1, p2))
                if grid[p1][p2] == '.':
                    grid[p1][p2] = '#'
                
                p1,p2=p1+ax,p2+ay

print(len(res),"result")
