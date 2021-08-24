import pickle
with open("input.txt","rb") as file:
    t=pickle.load(file)
    arr=pickle.load(file)
print(t)
print(arr)