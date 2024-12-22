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

nums=[]
with open('input/day22.txt','r') as f: 
    for line in f:
        nums.append(int(line.strip()))

res=0
for val in secretNumber(nums):
    res+=val
print(res)