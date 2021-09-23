n1=int(input())
arr1=list(map(int,input().split(" ")))
n2=int(input())
arr2=list(map(int,input().split(" ")))
i,j=0,0
count=0
while(i<len(arr1) and j<len(arr2)):
    if(arr1[i]==arr2[j]):
        count+=1
        print(f"{arr1[i]}")
        i+=1
        j+=1
    elif(arr1[i]<arr2[j]):
        i+=1
    else:
        j+=1
if(j==len(arr2) and i-1>=0 and arr2[j-1]!=arr1[i]):
    while(i<len(arr1)):
        if(arr1[i]==arr2[j-1]):
            count+=1
            print(f"{arr1[i]}")
            break
        i+=1
if(i==len(arr1) and i-1>=0 and arr1[i-1]!=arr2[j]):
    while(j<len(arr2)):
        if(arr2[j]==arr1[i-1]):
            count+=1
            print(f"{arr2[j]}")
            break
        j+=1



