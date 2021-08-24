t=int(input("enter number of test Cases:"))
for x in range(1,t+1):
    arr=map(int,input().split(" "))
    key=int(input())
    comp=0
    flag=0
    for i in arr:
        if(i==key):
            comp+=1
            flag=1
            break
        comp+=1
    if flag==1:
        print(f"Element found.number of comparison for {x} case were {comp}")
    else:
        print(f"Element not found. Number of comparision for {x} case were {comp}")

    
