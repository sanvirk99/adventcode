
file = open('input/day15.txt','r')
input=[]
input2=[]
with file as f:

    for line in f:
        line = line.strip()
        row=[]
        row2=[]
        for e in line:
            row.append(e)
            if e == '@':
                row2.append('@')
                row2.append('.')
                continue
            if e == 'O':
                row2.append('[')
                row2.append(']')
                continue

            row2.append(e)
            row2.append(e)
        if not row:
            break
        input.append(row)
        input2.append(row2)
    moves=(f.read().strip().replace('\n',''))

def draw():
    for row in input:
        print(row)

def draw2():
    for row in input2:
        print((' '.join(row)))
#print(moves)

directions={
    '>':(0,1),
    'v':(1,0),
    '<':(0,-1),
    '^':(-1,0)
}


def part1():

    dir=None
    def dfs(i,j):

        if input[i][j] == '#':
            return False
        if input[i][j] == '.':
            return True
        
        dx,dy=directions[dir]
        if dfs(i+dx,j+dy):
            input[i+dx][j+dy]=input[i][j]
            input[i][j]='.'
            return True
        return False

    rx,ry=0,0
    found=False
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j]=='@':
                rx=i
                ry=j
                found=True
                break
        if found:
            break
    for mov in moves:
        dir=mov
        dx,dy=directions[dir]
        # print('//////',mov,rx,ry)
        if dfs(rx+dx,ry+dy):
            input[rx+dx][ry+dy]=input[rx][ry]
            input[rx][ry]='.'
            rx=rx+dx
            ry=ry+dy
        #draw()
    count=0
    for i in range(len(input)):
        for j in range(len(input[0])):
            
            if input[i][j] == 'O':
                count += i * 100 + j
    print(count)

        
directions={
    '>':(0,1),
    'v':(1,0),
    '<':(0,-1),
    '^':(-1,0)
}

def part2():
    #print('width',len(input2[0]))
    #draw2()

    dir=None
    def dfsvalid(i,j):
        cur=input2[i][j]
        if input2[i][j] == '#':
            return False
        if input2[i][j] == '.':
            return True        
        dx,dy=directions[dir]
        if dir == '^' or dir == 'v':
            if cur == '[' and dfsvalid(i+dx,j+dy) and dfsvalid(i+dx,j+1+dy):
                return True
            if cur == ']' and dfsvalid(i+dx,j+dy) and dfsvalid(i+dx,j-1+dy):
                return True
        else: 
            if dfs(i+dx,j+dy):
                return True
        return False
    
    def dfs(i,j):
        cur=input2[i][j]
        if input2[i][j] == '#':
            return False
        if input2[i][j] == '.':
            return True        
        dx,dy=directions[dir]
        
        if dir == '^' or dir == 'v':
            if cur == '[' and dfs(i+dx,j+dy) and dfs(i+dx,j+1+dy):
                input2[i+dx][j+dy]=input2[i][j]
                input2[i][j]='.'
                input2[i+dx][j+1+dy]=input2[i][j+1]
                input2[i][j+1]='.'
                return True

            if cur == ']' and dfs(i+dx,j+dy) and dfs(i+dx,j-1+dy):
                input2[i+dx][j+dy]=input2[i][j]
                input2[i][j]='.'
                input2[i+dx][j-1+dy]=input2[i][j-1]
                input2[i][j-1]='.'
                return True
        else: 
            if dfs(i+dx,j+dy):
                input2[i+dx][j+dy]=input2[i][j]
                input2[i][j]='.'
                return True

        return False
    
    rx,ry=0,0
    found=False
    for i in range(len(input2)):
        for j in range(len(input2[0])):
            if input2[i][j]=='@':
                rx=i
                ry=j
                found=True
                break
        if found:
            break
    #print(rx,ry)
    for i,mov in enumerate(moves):
        dir=mov
        dx,dy=directions[dir]
        
        
        if dfsvalid(rx+dx,ry+dy):
            dfs(rx+dx,ry+dy)
            input2[rx+dx][ry+dy]=input2[rx][ry]
            input2[rx][ry]='.'
            rx=rx+dx
            ry=ry+dy
     
    count=0
    for i in range(len(input2)):
    
        for j in range(len(input2[0])):
            if input2[i][j] == '[':
                assert (input2[i][j+1] == ']')
                count += i * 100 + j
            if input2[i][j] == ']':
                assert (input2[i][j-1] == '[')
    print(count)

part1()
part2()