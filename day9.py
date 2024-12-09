
# %%
file=open('./input/day9.txt','r')

input=[]
with file as f:
    
    input=f.read().strip()


def part1():

    #transform
    t1=[]
    for i in range(0,len(input),2):
        id=i//2
        for j in range(int(input[i])):
            t1.append(id)

        if (i+1) < len(input):
            for k in range(int(input[i+1])):
                t1.append('.')
    l=0
    r=len(t1)-1
    while l < r:
        # print(t1)
        while t1[l] != '.':
            l+=1
        
        while t1[r] == '.':
            r-=1
        
        if l >= r:
            break


        t1[l],t1[r] = t1[r],t1[l]

    # print(l,r)
    count=0
    # print(t1)
    for i in range(len(t1)):
        if t1[i] == '.':
            break
        
        count+=i*int(t1[i])
    print(count)
    pass

import heapq
def part2():
    t1=[]
    free_spaces=[]
    locs=[]
    for i in range(0,len(input),2):
        id=i//2
        pos1=len(t1)-1
        for j in range(int(input[i])):
            t1.append(id)
        heapq.heappush(locs,(-id,abs(pos1-(len(t1))),pos1+1))

        if (i+1) < len(input):
            start=len(t1)-1
            for k in range(int(input[i+1])):
                t1.append('.')
            heapq.heappush(free_spaces,((start+1),abs(start-(len(t1)))))
   
  
    while locs:
        id , lo , pos = heapq.heappop(locs)
        for index,space in enumerate(free_spaces):
            start, lf = space
            if lo <= lf and start < pos:
               # print(start,lf , "freespace")
                for i in range(start,start+lo-1):
                    t1[i]=abs(id)
                    t1[pos]='.'
                    pos+=1
                if lf > lo:
                    lf = abs(lo-lf)
                    start=i
                    free_spaces[index]=start+1,lf+1
                    break
                else:
                    del free_spaces[index]
                break 
  
    count=0 
    for i in range(len(t1)):
        if t1[i] == '.':
            continue
        count+=i*int(t1[i])
    print(count,"result")

    pass

#part1()
part2()