def binary(arr,start,end,key):
    count=0
    while(start<=end):
        mid=start+(end-start)//2
        if(arr[mid]==key):
            count+=1
            count+=binary(arr,mid+1,end,key)
            count+=binary(arr,start,mid-1,key)
            return count
        elif(arr[mid]<key):
            start=mid+1
        else:
            end=mid-1
    return count


t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split(" ")))
    key=int(input())
    flag=0
    start=0
    end=n-1
    count=binary(arr,start,end,key)
    if(count>0):
        print(f"count is {count}")
    else:
        print(f"not Found")



