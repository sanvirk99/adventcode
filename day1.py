


file=open('./input/day1.txt','r',encoding="utf-8")

l1 = []
l2 = []

with file as f:
    
    for line in f:
        #print(line.split())
        e1,e2=line.split()
        l1.append(int(e1))
        l2.append(int(e2))

l1.sort()
l2.sort()


res=0
for pair in zip(l1,l2):
    #print(pair)
   
    diff=abs(pair[0]-pair[1])
    res+=diff

print(res)