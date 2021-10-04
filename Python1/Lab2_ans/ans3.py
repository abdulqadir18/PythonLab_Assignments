import csv

def listf(lis):
  if(int(lis[6])==1):
    return lis
  else:
    return 0

def list_of_list():
  with open("marks.csv","r") as obj:
    fobj=csv.reader(obj)
    next(fobj)
    next(fobj)
    next(fobj)
    l=[]
    cnt=0
    for i in fobj:
      l.append(i)
      cnt=cnt+1
      if(cnt==200):
        break
    
    result=list(map(listf,l))
    print(result)

list_of_list()