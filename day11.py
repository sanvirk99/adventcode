file=open('./input/day11.txt','r')


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





big_arr=[]
for num in input:
    res=[num]
    for i in range(25):
        arr=[]
        for num in res:
            arr.append(rules(num))
        res=flatten(arr)
    big_arr.append(len(res))
    


print(sum(big_arr))