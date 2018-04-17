ipv=[]
sz=int(input("Enter number of nodres"))
print("enter indexes")
for i in range(sz):
    ipv.append(input())
ipvect={}
for i in ipv:
    tmp=int(input("number of edges of "+i+"format -:vertice,idx"))
    for j in range(tmp):
        vrt,dst=input().split()
        if i not in ipvect:
            ipvect[i]=[(vrt,int(dst))]
        else:
            ipvect[i].append((vrt,int(dst)))

stv='0'
res={}
selc=set(['0'])
while len(selc)<sz:
    tmpminv=None
    tmpmind=None
    tgt=None
    for i in selc:
        for j in ipvect[i]:
            if j[0] not in selc:
                if tmpmind==None or tmpmind>j[1]:
                    tmpmind=j[1]
                    tmpminv=j[0]
                    tgt=i
    if tmpminv !=None:
        selc.add(tmpminv)
        if tgt not in res:
            res[tgt]=[(tmpminv,tmpmind)]
        else:
            res[tgt].append([tmpminv,tmpmind])
    else:
        break
print(res)