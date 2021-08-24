
import pickle
t=int(input())
arr=list(map(int,input().split(" ")))
with open("input.txt","wb") as file:
    pickle.dump(t,file)
    pickle.dump(arr,file)
    


