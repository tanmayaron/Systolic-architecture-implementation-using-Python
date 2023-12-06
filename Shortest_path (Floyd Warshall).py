import multiprocessing as mp
import functools
import math
import time as t

def funct(i, g, size, k): 
    for j in range(size): 
        g[i][j] = min(g[i][j],g[i][k]+ g[k][j])
    return (i,g[i])

def floydWarshall(g , size):
    pool = mp.Pool(processes=mp.cpu_count())
    for k in range(size):
        p = functools.partial(funct, g=g,size=size,k=k)
        result_list = pool.map( p,range(size))
        for result in result_list:
            g[result[0]] = result[1]
    pool.close()
    pool.join()
    return g

if __name__ == "__main__":
    size = int(input("Enter the graph size"))
    graph=[]
    for i in range(size):          
        ele =[]
        for j in range(size):      
            ele.append(int(input()))
        graph.append(ele)
    
    for i in range(size):
        for j in range(size):
            if(graph[i][j]==-1):
                graph[i][j]=math.inf
    shortest_paths = floydWarshall(graph, size)
    print(shortest_paths)