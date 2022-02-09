"""
stack=[]

stack.append(1)
stack.append(2)
stack.pop()
stack.append(3)

print(stack)
print(stack[::-1])


from collections import deque

q=deque()

q.append(1)
q.append(2)
q.popleft()
q.append(3)

print(q)
q.reverse()
print(q)
"""
"""
INF=99999999
graph=[[0,1,2],[3,4,INF],[7,INF,9]]
graph=[[] for _ in range(3)]
print(graph)
"""
"""
n,m=map(int,input().split())
graph=[]
for i in range(n):
  graph.append(list(map(int,input())))

def dfs(x,y):
  if x<0 or y<0 or x>=n or y>=m:
    return False
  
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True
  return False

result=0
for i in range(n):
  for j in range(m):
    if dfs(i,j)==True:
      result+=1

print(result)
"""
from collections import deque

n,m=map(int,input().split())
graph=[]
for _ in range(n):
  graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
  q=deque()
  q.append((x,y))
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if nx<0 or ny<0 or nx>=n or ny>=m or graph[nx][ny]==0:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny]=graph[x][y]+1
        q.append((nx,ny))
  return graph[n-1][m-1]
print(bfs(0,0))


























