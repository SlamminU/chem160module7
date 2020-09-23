import sys
from os import path
filename=input("Enter the name of the file: ")
if not os.path.exists(filename):
    sys.exit("Cannot find file given")
file=open(filename,"r")
while 1:
    line=file.readline()
    print(line,end="")
    if line=="":
        break
    words.extend(line.split())
counts=Counter(words)
for i in counts:
    print("%2d: %s"%(counts[i],i)) 
words_lower=[]
for i in words:
    words_lower.append(i.lower())
words=words_lower
