patterns=set()
towels=[]
max_pattern=0
with open('input/day19.txt','r') as f:

    temp=f.readline()
    temp=temp.strip()
    temp=temp.split(',')
    for pat in temp:
        pattern=pat.strip()
        max_pattern=max(len(pattern),max_pattern)
        patterns.add(pattern)
    f.readline()   
    for line in f:
        towels.append(line.strip())
#print(patterns)
#print(towels)


def part1():
    def dfs(towel):
        if len(towel) == 0:
            return True
        flag=False
        for pattern in patterns:
            if len(pattern) <= len(towel) and pattern == towel[:len(pattern)]:
                # print(pattern)
                # print(towel[len(pattern):])
                if dfs(towel[len(pattern):]):
                    return True
        return False
    count=0
    for towel in towels:
        if dfs(towel):
            #print(towel)
            count+=1
    print(count)

#part1()
def part2():
    mem={}
    def dfs(towel):
        #print(towel)
        if len(towel) == 0:    
            return 1
        if towel in mem:
            return mem[towel]
        res=0
        for i in range(0,max_pattern+1):
            if i <= len(towel) and towel[:i] in patterns:
                res+=dfs(towel[i:]) 
        mem[towel]=res
        return res
    res=0
    for i,towel in enumerate(towels):
        print(i)
        res+=dfs(towel)
        mem={}
    print(res)


print(max_pattern,"max pattern")
part2()