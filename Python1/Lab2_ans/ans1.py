import sys
import csv

if len(sys.argv)<2:
    print("Not a valid argument")
else:
    obj= open(sys.argv[1],"r")
    fobj=csv.reader(obj)
    cnt=0
    for i in fobj:
        print(i)
        if(i[0].isdigit()):
            cnt=cnt+1
    print(cnt)
