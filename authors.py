import csv
import re
        
def clean(actor):
    actor = ''.join([i if ord(i) < 128 else '' for i in actor])
    return actor
    
    
with open('publishersWeeklyList.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    authors = {}
    for row in spamreader:
        author = clean(row[3]).replace("'","")
        book = clean(row[2]).replace("'","")
        
        
        
        if author in authors.keys():
            authors[author]["books"].append([int(row[0]),int(row[1]),book])
            authors[author]["total"]+=1
            
        else:
            authors[author]={}
            authors[author]["books"]=[]
            
            authors[author]["name"]=author
            authors[author]["books"].append([int(row[0]),int(row[1]),book])
            authors[author]["total"]=1
        
#print authors

array = []
for author in authors:
    array.append(authors[author])
print array