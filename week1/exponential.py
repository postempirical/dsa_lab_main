import math
t=int(input())
for i in range(1,t+1):
    n=int(input())
    arr=list(map(int,input().split(" ")))
    key=int(input())
    count=0
    flag=0
    start=0
    end=n-1
    for i in range(0,int(math.log(n,2))):
        if(arr[2**i]<key):
            start=2**i
            count+=1
        if(arr[2**i]>key):
            end=2**i
            count+=1
            break
        if (arr[2**i]==key):
            count+=1
            flag=1
            break
    if(flag==0):
        for i in range(start+1,end+1):
            if(arr[i]==key):
                count+=1
                flag=1
                break
            count+=1
    print(start,end)
    if(flag==0):
        print(f"Not Present {count}")
    else:
        print(f"Present {count}")

