import csv

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
    
    filtered = filter(lambda score: int(score[6])==1, l)
    
    for j in filtered:
      print(j)    
    

list_of_list()