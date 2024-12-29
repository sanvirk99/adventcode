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
from collections import defaultdict
from itertools import permutations
numMoves=defaultdict(lambda: defaultdict())
for i in range(len(numPad)):
    for j in range(len(numPad[0])):
        if numPad[i][j] == '#':
            continue 
        for move in moveSpace:
            dx,dy=move
            nx,ny=i+dx,j+dy
            if nx in range(len(numPad)) and ny in range(len(numPad[0])) and numPad[nx][ny] != '#':
                #print(numPad[nx][ny])
                seq1=symbolx(dx)+symboly(dy)
                #print(seq)
                #if (i,j) == (2,1) and (nx,ny) == (0,2):
                perm=list(permutations(seq1))
                unique=set()
                for p in perm:
                    if validate(numPad,(i,j),(nx,ny),''.join(p)):
                        unique.add(''.join(p))

                numMoves[numPad[i][j]][numPad[nx][ny]]=unique
                # seq=symboly(dy)+symbolx(dx)
                # if seq == seq1:
                #     continue
                # numMoves[numPad[i][j]][numPad[nx][ny]].append(seq)

dirMoves=defaultdict(lambda: {})
for i in range(len(dirPad)):
    for j in range(len(dirPad[0])):
        if dirPad[i][j] == '#':
            continue 
        for move in dirSpace:
            dx,dy=move
            nx,ny=i+dx,j+dy
            if nx in range(len(dirPad)) and ny in range(len(dirPad[0])) and dirPad[nx][ny] != '#':
                #print(numPad[nx][ny])
                if dirPad[i][j] == '<':
                    seq=symboly(dy)+symbolx(dx)
                elif dirPad[i][j] == 'A':
                    seq=symbolx(dx)+symboly(dy)
                else:
                    seq=symbolx(dx)+symboly(dy)
                #print(seq)
                dirMoves[dirPad[i][j]][dirPad[nx][ny]]=seq



def allcombination(totype):
    res=[]
    def dfs(totype,combo,from_):

        if len(totype) == 0:
            res.append(combo)
            return
        for move in numMoves[from_][totype[0]]:
            choice=combo+move+'A'
            dfs(totype[1:],choice,totype[0])

    dfs(totype,'','A')
    #print(res)    
    return res

#print(allcombination('179A'))
            

# for from_ in numMoves:
#     print(from_,numMoves[from_])

# for from_ in dirMoves:
#     print(from_,dirMoves[from_])
def type(totype):
    print('type1')
    from_='A'
    seqr=''
    
    combinations=allcombination(totype)
    minlen=float('inf')
    
    for seqr in combinations:
        #print(seqr,len(seqr))
        from_='A'
        seqdir=''
        for next in seqr:
            seqdir+=dirMoves[from_][next]+'A'
            from_=next

        #print(seqdir,len(seqdir))
        from_='A'
        final_seq=''
        for next in seqdir:
            final_seq+=dirMoves[from_][next]+'A'
            from_=next
        print(final_seq,len(final_seq))
        minlen=min(minlen,len(final_seq))

    print(minlen, int(totype[:-1]))
    return minlen * int(totype[:-1])

def type21(totype):
    print('type2 orginal')
    from_='A'
    seqr=''
    
    combinations=allcombination(totype)
    minlen=float('inf')
    
    minseqdir=''
    for seqr in combinations:
        print(seqr, len(seqr))
        from_='A'
        seqdir=''
        for next in seqr:
            seqdir+=dirMoves[from_][next]+'A'
            from_=next
        
        print(seqdir,len(seqdir))

        from_='A'
        rseqdir=''
        for next in seqdir:
            rseqdir+=dirMoves[from_][next]+'A'
            from_=next

        print(rseqdir,len(rseqdir))


        from_='A'
        rrseqdir=''
        for next in rseqdir:
            rrseqdir+=dirMoves[from_][next]+'A'
            from_=next

        print(rrseqdir,len(rrseqdir))

        from_='A'
        rrrseqdir=''
        for next in rrseqdir:
            rrrseqdir+=dirMoves[from_][next]+'A'
            from_=next

        print(rrrseqdir,len(rrrseqdir))

        from_='A'
        final_seq=''
        for next in rrrseqdir:
            final_seq+=dirMoves[from_][next]+'A'
            from_=next
        print(final_seq,len(final_seq))
        minlen=min(minlen,len(final_seq))
        #print(seqdir,len(seqdir))


    print(minlen)

def type2(totype):
    print('type2 mofified')
    from_='A'
    seqr=''
    
    #combinations=allcombination(totype)
    minlen=float('inf')
    
    minseqdir=''
    combinations=[['<','A']]
    for seqr in combinations:
        print(seqr, len(seqr))
        from_='A'
        seqdir=''
        for next in seqr:
            seqdir+=dirMoves[from_][next]+'A'
            from_=next
        
        print(seqdir,len(seqdir))

        from_='A'
        rseqdir=''
        for next in seqdir:
            rseqdir+=dirMoves[from_][next]+'A'
            from_=next

        print(rseqdir,len(rseqdir))


        from_='A'
        rrseqdir=''
        for next in rseqdir:
            rrseqdir+=dirMoves[from_][next]+'A'
            from_=next

        print(rrseqdir,len(rrseqdir))

        from_='A'
        rrrseqdir=''
        for next in rrseqdir:
            rrrseqdir+=dirMoves[from_][next]+'A'
            from_=next

        print(rrrseqdir,len(rrrseqdir))

        from_='A'
        final_seq=''
        for next in rrrseqdir:
            final_seq+=dirMoves[from_][next]+'A'
            from_=next
        print(final_seq,len(final_seq))
        minlen=min(minlen,len(final_seq))
        #print(seqdir,len(seqdir))


    print(minlen)
    # return len(final_seq) * int(totype[:-1])

#type('379A')
type21('029A')
type2('0')
#type2('37')

# def part1():
#     with open('input/day21.txt','r') as f:
#         count=0
#         for line in f:
#             count+=type(line.strip())
#             print(count)
#         print(count)
# part1()


# def part2():
#     with open('input/day21.txt','r') as f:
#         count=0
#         for line in f:
#             print(line.strip())
#             #count+=type(line.strip())
#             r1 = type2(line.strip())
#             r2 = type(line.strip())
#             if  r1 != r2:
#                 print('fail')
                
#                 print(r1,r2)
#                 exit()
#             #print(count)
#         #print(count)
# part2()