import multiprocessing
from multiprocessing import Array

def compare_function(arr, buff, op,j):  
    mina=min(arr[j],op[j])
    maxa=max(arr[j],op[j])
    buff[j]=maxa
    arr[j]=mina
    op[j]=buff[j-1]    
    
def systolic_sort(ip,n):
    arr = Array('i', range(n))
    buff = Array('i', range(n))
    op = Array('i', range(n))

    for i in range (0,n):
        arr[i]=99999
    for i in range (0,n):
        buff[i]=99999
    for i in range (0,n):
        op[i]=99999 
    
    processes = []
    iter=(2*n)-1
    for i in range(0,iter):
        op[0]=ip[i]
        for j in range(0,n):
            process = multiprocessing.Process(target=compare_function, args=(arr, buff, op,j))                
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        for j in range(0,5):
            op[j]=buff[j-1]
        print("Cells after iteration ",i, " is ",arr[:])  
    print("Sorted List:", arr[:])
    return 

if __name__ == "__main__":
    input_list = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        ele = int(input())
        # adding the element
        input_list.append(ele)  
    print(input_list)
    input_list.reverse()
    for i in range(n-1):
        input_list.append(99999)
    systolic_sort(input_list,n)
    
