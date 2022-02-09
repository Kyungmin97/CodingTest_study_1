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

#구현 ex1
"""
n=int(input())
plans=input().split()
x,y=1,1
dx=[0,0,-1,1]
dy=[-1,1,0,0]
move=['w','s','a','d']

for plan in plans:
  for i in range(4):
    if plan==move[i]:
      nx=x+dx[i]
      ny=y+dy[i]
  if nx<1 or ny<1 or nx>n or ny>n:
    continue
  x,y=nx,ny
print(x,y)
"""

#구현 ex2
"""
n=int(input())
count=0
for i in range(n+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i)+str(j)+str(k):
        count +=1
print(count)
"""

#구현 1
"""
n=input()
x,y=int(n[1]),ord(n[0])-ord('a')+1

dx=[2,2,-2,-2,1,1,-1,-1]
dy=[1,-1,1,-1,2,-2,2,-2]
cnt=0
for i in range(8):
  nx=x+dx[i]
  ny=y+dy[i]

  if nx<1 or ny<1 or nx>8 or ny>8:
    continue
  cnt+=1
print(cnt)
"""

#구현 2
"""
n,m=map(int,input().split())
x,y,d=map(int,input().split())
nlist=[]
for _ in range(n):
  nlist.append(list(map(int,input().split())))

dx=[0,-1,0,1]
dy=[-1,0,1,0]

nlist[y][x]=2
while True:
  for i in range(4):
    d=d-1
    if d==-1:
      d=3
    nx=x+dx[d]
    ny=y+dy[d]
    if nx<0 or ny<0 or nx>m or ny>n or nlist[ny][nx]!=0:
      continue
    nlist[y][x]=2
    x,y=nx,ny

  nx=x-dx[d]
  ny=y-dy[d]
  if nx<0 or ny<0 or nx>m or ny>n or nlist[ny][nx]==1:
    break
    
cnt=0
for i in range(n):
  cnt+=nlist[i].count(2)
print(cnt)
print(nlist)
"""
"""
n,m=map(int,input().split())
d=[[0]* m for _ in range(n)]
x,y,direction=map(int,input().split())

d[x][y]=1

nlist=[]
for _ in range(n):
  nlist.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]
"""

import DFS_BFS









