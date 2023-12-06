import multiprocessing
from multiprocessing import Array

def worker(arr,list,a,i,j):
    arr[i]+=list[i+j]*a[j] 
    return

def conv(list,n,a,m):
    arr = Array('i', range(n-m+1))
    for i in range (n-m+1):
        arr[i]=0    
    processes = []
    for i in range(0,n-m+1):
        for j in range(0,m):
            process = multiprocessing.Process(target=worker, args=(arr,list,a,i,j))
                                            
            processes.append(process)
            process.start()

        for process in processes:
            process.join()
        print("Output array after iteration ",i," is ",arr[:])  
    print("OUTPUT: ", arr[:])
    return 

if __name__ == "__main__":
    input_list = []
    n = int(input("Enter number of elements in first array : "))
    for i in range(0, n):
        ele = int(input())
        # adding the element
        input_list.append(ele)  
    
    list2=[]
    m = int(input("Enter number of elements in second array : "))
    for i in range(0, m):
        ele = int(input())
        # adding the element
        list2.append(ele) 
   
    conv(input_list,n,list2,m)
    
