import re
from collections import defaultdict
from itertools import combinations

 
import networkx as nx
import matplotlib.pyplot as plt

graph=defaultdict(lambda : [])
g=nx.Graph()
with open('input/day23.txt','r') as f:
    regex=r"\w+"
    for line in f:
        vs,vd=re.findall(regex,line)
        graph[vs].append(vd)
        graph[vd].append(vs)
        #g.add_edge(vs,vd)
        

#nx.draw(g, with_labels = True)

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
    
part1()



#part2()