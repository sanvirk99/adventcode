import time

# %%
file=open('./input/day7.txt','r')
eqs=[]
with file as f:
    input=file.read().strip().split('\n')
    for eq in input:
        total, eq = eq.split(':')
        eq=list(map(int,eq.split()))
        eqs.append([int(total),eq])
# %%
res=[]

def concat(x,y):
    val =str(x) + str(y)
    return int(val)


def dfs(sum,cur,arr,i):
    if cur > sum:
        return False
    if i == len(arr):
        if cur == sum:
            res.append(sum)
            return True
        return False
    
    #part two addition
    if dfs(sum,concat(cur,arr[i]), arr, i+1):
        return True

    if dfs(sum,cur*arr[i],arr,i+1):
        return True
        
    return dfs(sum,cur+arr[i],arr,i+1)


# Timing the execution
start_time = time.time()
for eq in eqs:
    total,arr = eq
    if len(arr) == 0:
        assert False
    dfs(total,arr[0],arr,1)

end_time = time.time()
print(sum(res))
print(f"Execution time: {end_time - start_time} seconds")