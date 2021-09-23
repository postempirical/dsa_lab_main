
import random
global comp
comp=0
global swap
swap=0
def quickSort(arr,start,end):
    if(end<start):
        return
    pivot=arr[end]
    k=start
    
    while(start<end):
        if(arr[start]<pivot):
            arr[start],arr[k]=arr[k],arr[start]
            k+=1
            global swap
            swap+=1
        start+=1
        global comp
        comp+=1
    arr[k],arr[end]=arr[end],arr[k]
    
    swap+=1
    quickSort(arr,0,k-1)
    quickSort(arr,k+1,end)
    

    


t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    quickSort(arr,0,len(arr)-1)
    print(f"{arr}, {comp},{swap}")


    