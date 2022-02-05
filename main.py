#Greed 1
"""
n,m,k=map(int,input().split())
nlist=list(map(int,input().split()))
nlist.sort(reverse=True)
sum=0
print(nlist)
cnt=0
for m in range(m):
  if cnt<k:
    sum+=nlist[0]
    cnt+=1
  else:
    sum+=nlist[1]
    cnt=0
print(sum)
"""

#Greed 2
"""
n,m=map(int,input().split())
nlist=[]
for _ in range(n):
  nlist.append(list(map(int,input().split())))
print(nlist)
result=min(nlist[0])
for i in range(n):
  result=max(result,min(nlist[i]))
print(result)
"""

#Greed 3
"""
n,k=map(int,input().split())
result=n
cnt=0
while result>1:
  if result%k==0:
    result=result//k
    cnt+=1
  else:
    result=result//k
    cnt+=result%k

print(cnt)
"""
