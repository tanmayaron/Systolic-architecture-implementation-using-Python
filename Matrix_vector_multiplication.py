import multiprocessing
from multiprocessing import Array
from array import *
    
def worker(a,arr,x,i,j):
    arr[j]+=x[i]*a[j][i]
    return

def multiplication(a,x):
    arr=Array('i',range(n))
    op=Array('i',range(n))
    for i in range (0,n):
        arr[i]=0
    for i in range (0,n):
        op[i]=0 
    processes = []
    for i in range(0,n):
        for j in range(0,n):
            process = multiprocessing.Process(target=worker, args=(a,arr,x,i,j))                                    
            processes.append(process)
            process.start()
        for process in processes:
            process.join()
        print("Output after iteration ",i," is ",arr[:])    

    print("OUTPUT MATRIX ",arr[:])
    return

if __name__ == "__main__":  
    matrix=[]
    n = int(input("Enter the matrix size:"))
    for i in range(n):          
        ele =[]
        for j in range(n):      
            ele.append(int(input()))
        matrix.append(ele)
    x=[]
    print("Input the vector")
    for i in range(0, n):
        ele = int(input())
        x.append(ele)
    multiplication(matrix,x)
    
