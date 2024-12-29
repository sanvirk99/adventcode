import re
from collections import defaultdict
from itertools import combinations 
import networkx as nx
#import matplotlib.pyplot as plt

graph=defaultdict(lambda : [])
g=nx.Graph()
with open('input/day23.txt','r') as f:
    regex=r"\w+"
    for line in f:
        vs,vd=re.findall(regex,line)
        graph[vs].append(vd)
        graph[vd].append(vs)
        #g.add_edge(vs,vd)

#x.draw(g, with_labels = True)

def part1():
    res=set()
    def dfs(s,hasT,comps,i):
        if i == 3:
            if (comps[0] in graph[comps[-1]]):
                flag=False
                for x in comps:
                    if x[0] == 't':
                        flag = True
                if flag:
                    res.add(tuple(sorted(comps)))
            return
        for neighbour in graph[s]:
            arr=comps.copy()
            arr.append(neighbour)
            dfs(neighbour,hasT,arr,i+1)
    for key in graph:
        dfs(key,False,[],0)

    print(len(res))
    
#part1()

totalV=len(graph.keys())
def part2():
    visited=set()
    res=0
    sets=defaultdict(lambda : 0)
    stack=[]
    def validate(s,cur,i):
        if cur == s:
            nonlocal res
            sets[tuple(sorted(stack))]+=1
            res=max(res,i)
            return 
        if not (i<totalV):
            return
        if cur in visited:
            return
        if not (cur in graph[s]):
            return
        visited.add(cur)
        stack.append(cur)
        for neighbour in graph[cur]:
            validate(s,neighbour,i+1)
        stack.pop()
        return
    for key in graph:
        visited=set()
        stack.append(key)
        for neigbour in graph[key]:
            validate(key,neigbour,1)
        stack.pop()
    maxkey=None
    maxvalue=0

    for key,value in sets.items():
        if len(key) == value:
            if value > maxvalue:
                maxkey=key
                maxvalue=value
    
    print(','.join(maxkey))

import time

# Measure execution time of part2()
start_time = time.time()
part2()
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Execution time of part2(): {elapsed_time:.6f} seconds")