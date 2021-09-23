


global comp
comp=0
global inversion
inversion=0
def main():    
    t=int(input())
    for i in range(0,t):
        n=int(input())
        arr=list(map(int,input().split()))
        arr=divide(arr)
        print(arr)
        print(f"comp:{comp}")
        print(f"inversion:{inversion}")
def divide(arr):
    if(len(arr)==0 or len(arr)==1):
        return arr
    mid=len(arr)//2
    left=divide(arr[:mid])
    right=divide(arr[mid:])
    return combine(left,right)
def combine(arr1,arr2):
    i,j=0,0
    arr=[]
    while(i<len(arr1) and j<len(arr2)):
        global inversion
        if(i<=j and arr1[i]>arr2[j]):
            inversion+= (len(arr1)-1-i)
        if(j<i and arr2[j]>arr1[i]):
            inversion+=(len(arr2)-1-j)
        if(arr1[i]<arr2[j]):
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1
        global comp
        comp+=1
        
    while(i<len(arr1)):
        arr.append(arr1[i])
        i+=1
        inversion+=1
    while(j<len(arr2)):
        arr.append(arr2[j])
        j+=1
        inversion+=1
    return arr
main()