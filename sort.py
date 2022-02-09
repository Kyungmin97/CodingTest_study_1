
print("sort!")


nlist=[1,5,2,8,4,7,8,9,0]

def qsort(nlist):
  if len(nlist)<1:
    return nlist
  
  pivot=nlist[0]
  tail=nlist[1:]

  l=[x for x in tail if x<=pivot]
  r=[x for x in tail if x>pivot]

  return qsort(l)+[pivot]+qsort(r)

print(qsort(nlist))












