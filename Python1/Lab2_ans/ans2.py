import csv

def list_of_list():
  with open("marks.csv","r") as obj:
    fobj=csv.reader(obj)
    next(fobj)
    next(fobj)
    next(fobj)
    l=[]
    
    for i in fobj:
      l.append(i)
    print(l)
    print(len(l))

list_of_list()