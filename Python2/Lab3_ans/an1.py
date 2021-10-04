import csv    
with open('marks.csv') as csv_file:    
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    next(csv_reader)
    next(csv_reader)    
       
    for line in csv_reader:    
        for i in range(1, len(line)-1):
            x=0
            if line[i] != 'NA' and line[i] !='':
                x+= float(line[i])
                
            line[-3]=x
        print(line)