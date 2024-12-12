file=open('./input/day11.txt','r')
import time

input=[]
with file as f:
    
    input=list(map(int,file.read().strip().split(' ')))
        
print(input)



def rules(number):

    if number == 0:
        return [1]
    
    string=str(number)
    if len(string)%2 == 0:
        left=string[:len(string)//2]
        right=string[len(string)//2:]

        return [int(left),int(right)]
    
    return [number*2024]


def flatten(arr):
    #print(arr)
    return [x for element in arr for x in element]




def part1(arr,blinks):

    for i in range(blinks):
        res=[]
        for num in arr:
            res.append(rules(num))
        arr=flatten(res)
        #print(i)

    #print(len(input))
    return len(arr)

 

def part2(input,blinks):

    mem={}
    def dfs(num,i):

        
        if i == 0:
            return 1
        
        if (num,i) in mem:
            return mem[(num,i)]
        
        count=0
        arr=rules(num)
        for n in arr:
            count+=dfs(n,i-1)

        mem[(num,i)] = count
        return count 


    count=0
    for num in input:
        count+=dfs(num,blinks)
    #print(count)
    return count


#print(part1(input,25))
print(part2(input,75))
