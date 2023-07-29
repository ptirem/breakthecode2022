f =open('foretBrulee.txt','r')
taille=26
def ver(tab,i,c):
    tabl=[]
    for j in range(-1,2,1):
        for k in range(-1,2,1):
            if (c+k) >=0 and (c+k) < len(tab[i]) and (j+i)>=0 and (i+j) < len(tab):
                print()
                if tab[i+j][c+k]==0 and (j+k)%2==1:
                    tab[i+j][c+k]=int(tab[i][c])+1
                    tabl.append([i+j,c+k])
    print(tabl)
    return tabl
def verif(t):
    for i in range(len(t)):
        for j in range(len(t)):
            if t[i][j]==0:
                return False
    return True



l=f.readlines()
for i in range(len(l)):
    l[i]=l[i].replace('\n','')
    l[i]=l[i].split(',')
tab=[[0 for i in range(taille)]for i in range(taille)]
for i in range(len(l)):
    tab[int(l[i][0])][int(l[i][1])]=-1

tab[0][0]=1

file=[[0,0]]
#
while len(file)>0:
    instru=file
    file=[]
    for i in instru:
            file.append(ver(tab,i[0],i[1]))
    instru=[]
    for i in range(len(file)):
        for j in range(len(file[i])):
            instru.append(file[i][j])
    file=instru



if True:
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j]==-1:
                print('#',end=' ')
            elif tab[i][j]==0:
                print(" ",end=' ')
            else:
                print(tab[i][j],end=' ')
        print()
