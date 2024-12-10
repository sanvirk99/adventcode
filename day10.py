# %%
file=open('./input/day10.txt','r')

input=[]
with file as f:
    
    for line in file:
        line=line.strip()
        row=[]
        for e in line:
            if e == '.':
                row.append(-1)
                continue
            row.append(int(e))
        input.append(row)
# print(input)



def part1():

    def findscore(i,j):
        
        visted=set()
        res=[0]
        def dfs(i,j,prev):
            
            if (i,j) in visted:
                return
            
            if not (0 <= i < len(input) and 0 <= j < len(input[0])):
                return 
            # print(i,j)
            if not ((prev+1) == input[i][j]):
                return
            
            visted.add((i,j))

            if input[i][j] == 9:
                res[0]+=1
                return
            
            dfs(i + 1, j, input[i][j])
            dfs(i - 1, j, input[i][j])
            dfs(i, j + 1, input[i][j])
            dfs(i, j - 1, input[i][j])

        dfs(i + 1, j, input[i][j])
        dfs(i - 1, j, input[i][j])
        dfs(i, j + 1, input[i][j])
        dfs(i, j - 1, input[i][j])
        return res[0]
    
    count=0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j]==0:
                count+=findscore(i,j)
            
    print(count)

def part2():

    def findscore(i,j):
        
        visted=set()
        res=[0]
        def dfs(i,j,prev):
            
            if (i,j) in visted:
                return
            
            if not (0 <= i < len(input) and 0 <= j < len(input[0])):
                return 
            # print(i,j)
            if not ((prev+1) == input[i][j]):
                return
            
            visted.add((i,j))
        

            if input[i][j] == 9:
                res[0]+=1
                visted.remove((i,j))
                return
            
            dfs(i + 1, j, input[i][j])
            dfs(i - 1, j, input[i][j])
            dfs(i, j + 1, input[i][j])
            dfs(i, j - 1, input[i][j])

            visted.remove((i,j))

        dfs(i + 1, j, input[i][j])
        dfs(i - 1, j, input[i][j])
        dfs(i, j + 1, input[i][j])
        dfs(i, j - 1, input[i][j])
        return res[0]
    
    count=0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j]==0:
                count+=findscore(i,j)
            
    print(count,'part2')




#part1()
part2()