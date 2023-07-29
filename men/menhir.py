from math import sqrt 
import time 

def trifusion(t):
    if len(t)==1:
       return t
    else: 
        return fusion(trifusion(t[:int(len(t)/2)]),trifusion(t[int(len(t)/2):]))

def fusion(t1,t2):
    t=[0 for i in range(len(t1)+len(t2))]
    indice=0
    i1=0
    i2=0
    while indice<len(t):
        if i1==len(t1):
            t[indice]=t2[i2]
            i2+=1
            indice+=1
        elif i2==len(t2):
            t[indice]=t1[i1]
            i1+=1
            indice+=1
        else:
            if t1[i1][0]<t2[i2][0]:
                t[indice]=t1[i1]
                indice+=1
                i1+=1
            elif t1[i1][0]>t2[i2][0]:
                t[indice]=t2[i2]
                indice+=1
                i2+=1
            else:
                if t1[i1][1]<t2[i2][1]:
                    t[indice]=t1[i1]
                    indice+=1
                    i1+=1
                else:
                    t[indice]=t2[i2]
                    indice+=1
                    i2+=1
    return t

def exist(t,c):
    d=0
    f=len(t)
    while d<f:
        m=(d+f)//2
        if c[0]>t[m][0] or (c[0]==t[m][0] and c[1]>t[m][1]):
            d=m+1
        elif c[0]<t[m][0] or (c[0]==t[m][0] and c[1]<t[m][1]):
            f=m-1
        else:
            return True
    return False

def mainfunct():
    for i in range(len(t)):
        for j in range(len(t)-1,-1,-1):
            distance=((t[i][1]-t[j][1])**2+(t[i][0]-t[j][0])**2)**0.5
            diffx=t[j][0]-t[i][0]
            diffy=t[j][1]-t[i][1]
            
            if i!=j and (exist(t,[t[i][0]+diffy,t[i][1]+diffx])and exist(t,[t[j][0]+diffy,t[j][1]+diffx])):
                return distance
            

start_time = time.time()
f=open("men/carre.txt","r")
t=f.readlines()
for i in range(len(t)):
    t[i]=t[i].replace("\n","").split(" ")
    t[i]=[int(t[i][0]),int(t[i][1])]
t=trifusion(t)

print(mainfunct())

print("--- %s seconds ---" % (time.time() - start_time))#test