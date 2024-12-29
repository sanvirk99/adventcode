
from collections import defaultdict
from itertools import permutations

numPad=[
    ['7','8','9'],
    ['4','5','6'],
    ['1','2','3'],
    ['#','0','A']
]

dirPad=[
    ['#','^','A'],
    ['<','v','>']
]

moveSpace=[]
for i in range(-3,4):
    for j in range(-2,3):
        if abs(i) in range(0,4) and abs(j) in range(0,3):
            moveSpace.append((i,j))

dirSpace=[]
for i in range(-1,2):
    for j in range(-2,3):
        if abs(i) in range(0,2) and abs(j) in range(0,3):
            dirSpace.append((i,j))

#change this symboling reflect move length
def symbolx(x):
    if x < 0:
        return '^'*abs(x)
    if x > 0:
        return 'v'*abs(x)
    return ''
def symboly(y):
    if y < 0:
        return '<'*abs(y)
    if y > 0:
        return '>'*abs(y)
    return ''

directions={
    '^':(-1,0),
    'v':(1,0),
    '<':(0,-1),
    '>':(0,1)
}

def validate(grid,cur,end,seq):


    def dfs(cur,i):
        x,y=cur
        if cur == end:
            return True
        if grid[x][y] == '#':
            return False
        dx,dy=directions[seq[i]]
        return dfs((x+dx,y+dy),i+1)
    
    return dfs(cur,0)

#precalculate all different moves from a poisiton

numMoves=defaultdict(lambda: defaultdict())
for i in range(len(numPad)):
    for j in range(len(numPad[0])):
        if numPad[i][j] == '#':
            continue 
        for move in moveSpace:
            dx,dy=move
            nx,ny=i+dx,j+dy
            if nx in range(len(numPad)) and ny in range(len(numPad[0])) and numPad[nx][ny] != '#':
                seq1=symbolx(dx)+symboly(dy)
                perm=list(permutations(seq1))
                unique=set()
                for p in perm:
                   
                    if validate(numPad,(i,j),(nx,ny),''.join(p)): 
                        temp=list(p)
                        temp.append('A')
                        unique.add(''.join(temp))
                numMoves[numPad[i][j]][numPad[nx][ny]]=unique

dirMoves=defaultdict(lambda: {})
for i in range(len(dirPad)):
    for j in range(len(dirPad[0])):
        if dirPad[i][j] == '#':
            continue 
        for move in dirSpace:
            dx,dy=move
            nx,ny=i+dx,j+dy
            if nx in range(len(dirPad)) and ny in range(len(dirPad[0])) and dirPad[nx][ny] != '#':
                seq1=symbolx(dx)+symboly(dy)
                perm=list(permutations(seq1))
                unique=set()
                for p in perm:
                    if validate(dirPad,(i,j),(nx,ny),''.join(p)):
                        temp=list(p)
                        if not temp:
                            temp=['A']
                        else:
                            temp.append('A')
                        #print(print(temp),'dir')
                        unique.add(''.join(temp))

                dirMoves[dirPad[i][j]][dirPad[nx][ny]]=unique

# %%
def allcombination(totype):
    res=[]
    def dfs(totype,combo,from_):

        if len(totype) == 0:
            res.append(combo)
            return
        for move in numMoves[from_][totype[0]]:
            choice=combo+move
            dfs(totype[1:],choice,totype[0])

    dfs(totype,'','A')
    #print(res)    
    return res

def dircombinations(totype):
    res=[]
    def dfs(totype,combo,from_):

        if len(totype) == 0:
            res.append(combo)
            return
        for move in dirMoves[from_][totype[0]]:
            choice=combo+move
            dfs(totype[1:],choice,totype[0])

    dfs(totype,'','A')
    #print(res)    
    return res


def chainvisual(seq,end):
    minlen=float('inf')
    minseq=''
    def dfs(seq,i):
        print(seq,len(seq))
        if i == end:
            nonlocal minseq,minlen
            if len(seq) < minlen:
                minseq=seq
                minlen=len(seq)
            return
        for combo in dircombinations(seq):
            #print(combo)
            dfs(combo,i+1)
        

    dfs(seq,0)
    print(minseq)
    return minlen





def chainRobot(letter,prev,end,seqstart):
    
    mem={}
    
    def dfs(letter,prev,i,start):
       # print(letter,prev,i)
        if i == end:
            return 1
        if (letter,prev,i,start) in mem:
            return mem[(letter,prev,i,start)]
        mincount=float('inf')
        if start:
            prev='A'
        for index, move in enumerate(dirMoves[prev][letter]):
            count=0
            cur=prev
            begin=True
            for each in move:
                count+=dfs(each,cur,i+1,begin)
                begin=False
                cur=each
            if count < mincount:
                mincount=min(mincount,count)
        mem[(letter,prev,i,start)] = mincount
        return mincount

    return dfs(letter,prev,0,seqstart)

def type(totype,depth):

    combinations=allcombination(totype)
    minlen=float('inf')
    for seq in combinations:
        prev='A'
        start=True
        res=0
        for letter in seq: #repersent 029A
            res+=chainRobot(letter,prev,depth,start)
            start=False
            prev=letter
        minlen=min(res,minlen)
    return minlen*int(totype[:-1])

exampleinputs=['029A','980A','179A','456A','379A']

def part1():
    count=0
    for input in exampleinputs:
        count+=type(input,depth=2) #two directional robots
    
    print(count)
        
part1()








    




