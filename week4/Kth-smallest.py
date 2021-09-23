def loc(arr,start,end,index):
    if(end<start):
        return
    pivot=arr[end]
    k=start
    while(start<end):
        if(arr[start]<pivot):
            arr[start],arr[k]=arr[k],arr[start]
            k+=1
        start+=1
    arr[k],arr[end]=arr[end],arr[k]
    if(k==index):
        return arr[k]
    if(k>index):
        return loc(arr,0,k-1,index)
    else:
        return loc(arr,k+1,end,index)



t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    index=int(input())
    print(loc(arr,0,len(arr)-1,index))
    
