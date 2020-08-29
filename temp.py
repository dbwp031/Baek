from itertools import combinations
import copy
n,m,d=list(map(int,input().split()))
data=[]

for i in range(n):
  data.append(list(map(int,input().split())))
data_saved=copy.deepcopy(data)

def kill(data,d,y):
  ad=1
  x=n-1
  mid=y
  if(data[x][y]==1):
    data[x][y]=0
    return 1
  ad+=1
  while(ad<=d):

    nx,ny=x,y-(ad-1)

    while(ny<mid):
      if(nx<0 or ny<0):
        nx-=1
        ny+=1
        continue
      else:
        if(data[nx][ny]==1):
          data[nx][ny]=0
          return 1
        else:
          nx-=1
          ny+=1
    while(ny<m):
      if(nx>n-1 or ny>m-1):
        break
      if(data[nx][ny]==1):
        data[nx][ny]=0
        return 1
      else:
        nx+=1
        ny+=1  
    ad+=1
  return 0

#main
item=[]
for i in range(0,m):
  item.append(i)
com=list(combinations(item,3))

result=[]#궁수 위치에 따른 적 죽인 수
cnt=0

for pos in com:
  a=1
  while(a!=0):
    a=0
    cnt+=kill(data,d,pos[0])
    cnt+=kill(data,d,pos[1])
    cnt+=kill(data,d,pos[2])

    for i in range(n-1,0,-1):
      data[i]=data[i-1]
  #------------------
    for i in range(m):
      data[0][i]=0

    for i in range(n):
      a+=sum(data[i])
    if(a==0):
      result.append(cnt)
      cnt=0
      data=copy.deepcopy(data_saved)
  
print(result)  
print(max(result))
