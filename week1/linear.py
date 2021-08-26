t=int(input())
for i in range(1,t+1):
    n=int(input())
    arr=list(map(int,input().split(" ")))
    key=int(input())
    flag=-1
    for j in range(0,len(arr)):
        if(arr[j]==key):
            flag=j
            break
    if(flag==-1):
        print(f"Not Present {len(arr)+1}")
    else:
        print(f"Present {flag+1}")
    
