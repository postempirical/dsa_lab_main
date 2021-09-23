t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    target=int(input())
    arr.sort()
    start=0
    end=len(arr)-1
    flag=0
    while(start<end):
        if(arr[start]+arr[end]==target):
            flag=1
            print(f"{arr[start]} {arr[end]}")
            start+=1
            end-=1
        elif(arr[start]+arr[end]>target):
            end-=1
        else:
            start+=1
    if(flag==0):
        print("no such elements found")
    