from collections import deque
input='input/day22.txt'
def mixMulti(multi,num):
    tomix = num * multi
    return num ^ tomix
def mixDiv(div,num):
    tomix=num//div
    return num ^ tomix
def prune(holder,num):
    return num % 16777216
mapfunc = {
    'mixMulti' : mixMulti,
    'mixDiv': mixDiv,
    'prune' : prune,
}
operations=[('mixMulti',64),('prune',0),('mixDiv',32),('prune',0),('mixMulti',2048),('prune',0)]
def secretNumber(arr):
   
    for num in arr:
        n=0
        while n < 2000:
            for func,val in operations:
                #print(func,val)
                num=mapfunc[func](val,num)
    
            n+=1
        yield num

#return current price and the price change
def eachNum(num,iterations):
    n=0
    dp=num%10
    while n < iterations:
        for func,val in operations:
            num=mapfunc[func](val,num)
        n+=1
        change = num%10 - dp
        dp = num%10
        yield dp,change

def part1():
    nums=[]
    with open(input,'r') as f: 
        for line in f:
            nums.append(int(line.strip()))

    res=0
    for val in secretNumber(nums):
        res+=val
    print(res)



#find all maximums looking for repeating numbers
#it takes the first sequence to occur if multiple consective should be ignored

def part2():
    que=deque()
    mem={}
    iterations=2000
    with open(input,'r') as f:
        for line in f:
            num=int(line.strip())
            for secret in eachNum(num,iterations):
                curprice,pricechange=secret
                #print(f"{num:<10} {curprice:<1} {pricechange:<1}") 
                que.appendleft(pricechange)
                if len(que) == 4:
                    #take snapshot anc count occurange
                    mem[tuple(que)]=0
                    que.pop()
                
    #print(len(unique))
    with open(input,'r') as f:
       
        for line in f:
            num=int(line.strip()) 
            seen=set()
            que.clear()
            for secret in eachNum(num,iterations):
                curprice,pricechange=secret
                #print(f"{num:<10} {curprice:<1} {pricechange:<1}") 
                que.appendleft(pricechange)
                if len(que) == 4:
                    tque=tuple(que)
                    if tque not in seen and tque in mem:
                        mem[tque] += curprice
                        seen.add(tque)
                    que.pop()

    print(max(mem.values()),max(mem.keys(),key=lambda x:mem[x]))

part2()