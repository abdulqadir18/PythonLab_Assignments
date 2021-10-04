import csv
import sys

sum=0
def selcount(s):
  if(s[6]==1):
    return s[6]

Dic={"S.No":[], "Math":[], "CS":[], "GK":[], "Prog":[], "Comm":[], "Sel":[]}
with open("marks.csv","r") as obj:
  fobj = csv.reader(obj)
  selected=map(selcount,fobj)
  for i in list(selected):
    if(i!=None):
      Dic["S.No"].append(i[0])
      Dic["Math"].append(i[1])
      Dic["CS"].append(i[2])
      Dic["GK"].append(i[3])
      Dic["Prog"].append(i[4])
      Dic["Comm"].append(i[5])
      Dic["Sel"].append(i[6])
  print(Dic["S.No"])