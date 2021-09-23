t=int(input())
for i in range(t):
    n=int(input())
    arr=input().split(" ")
    count=[0 for i in range(256)]
    for j in range(0,len(arr)):
        count[ord(arr[j])]+=1
    m=0
    index=0
    for k in range(0,len(count)):
        if(count[k]>m):
            m=count[k]
            index=k
    if(m==0 and index==0):
        print("no duplicate elements found")
    elif(m==1):
        print("no duplicate element found")
    else:
        print(chr(index)+":"+f"{m}")
    

        
    