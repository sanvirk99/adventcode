
locks=set()
keys=[]


def isLock(grid):
    for e in grid[0]:
        if e!='#':
            return False
    for e in grid[-1]:
        if e!='.':
            return False
    return True

def process(grid):
    if isLock(grid):
        row=[]
        for i in range(len(grid[0])):
            count=0
            for j in range(1,len(grid)):
                if grid[j][i] != '#':
                    break
                count+=1
            row.append(count)
        locks.add(tuple(row))
    else:
        row=[]
        for i in range(len(grid[0])):
            count=0
            for j in range(len(grid)-2,-1,-1):
                if grid[j][i] != '#':
                    break
                count+=1
            row.append(count)
        keys.append(row)



with open('input/day25.txt','r') as f:

    while True:
        grid=[]
        for line in f:
            if line[0] == '\n':
                break
            row=[]
            line=line.strip()
            for each in line:
                row.append(each)
            grid.append(row)
        if not grid:
            break
        assert len(grid) == 7
        process(grid)
        # for row in grid:
        #     print(''.join(row))


def possibleLocks(key):

    res=set()
    stack=[]
    def dfs(i):
        if i >= 5:
            res.add(tuple(stack))
            return
        fit=0
        while fit+key[i] <= 5: 
            stack.append(fit)
            dfs(i+1)
            stack.pop()
            fit+=1

    dfs(0)
    return res


count=0
for key in keys:
    fits=possibleLocks(key)
    for fit in fits:
        if fit in locks:
            count+=1
print(count, "fits")
    