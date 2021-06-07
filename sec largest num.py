#second largest no
n=int(input())
data=list(map(int,input().split()))
data.sort()
k=set(data)
k=list(k)
print(k[-2])
