t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split(" ")))
    comp=0
    swap=0
    for j in range(0,n-1):
        index=j
        for k in range(j+1,n):
            if(arr[index]>arr[k]):
                
                index=k
            comp+=1
            
        
        
        temp=arr[index]
        arr[index]=arr[j]
        arr[j]=temp
        swap+=1
        
        


    print(f"{arr} \n comparisons={comp} \n swaps={swap}")
