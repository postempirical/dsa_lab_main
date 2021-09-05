t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split(" ")))
    comp=0
    swapping=0
    for j in range(1,n):
        key=arr[j]
        temp=j
        k=j-1
        while(k>=0 and arr[k]>key):
            comp+=1
            swapping+=1
            arr[k+1]=arr[k]
            k=k-1
        if(k>=0 and arr[k]<key):
            comp+=1
        if(k!=j-1):
            arr[k+1]=key
            swapping+=1
        

    print(arr)
    print(f"comparisons={comp}")
    print(f"shifts={swapping}")
            
