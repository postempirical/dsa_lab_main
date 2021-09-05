t=int(input())
for i in range(0,t):
    length=int(input())
    n=list(map(int,input().split(" ")))
    n.sort()
    i=0
    while(i<length-1):
        if(n[i]==n[i+1]):
            print("YES")
            break
        i+=1
    if(i==length-1):
        print("NO")
    

