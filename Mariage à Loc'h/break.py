f=open("traverseeBaie.txt",'r')
line=f.readline()
res=0

i=0

line=line.split(",")
while(res<35410):
    
        
    res+=int(line[i])
    res+=1
    i+=1
print(i)