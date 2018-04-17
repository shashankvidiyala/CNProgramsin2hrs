def gcd(a,b):
    while True:
        tmp=a%b
        if tmp==0:
            return b
        a=b
        b=tmp
p=13
q=17
n=p*q
phi=(p-1)*(q-1)
msg="hey shashank"
e=2
while gcd(e,phi)!=1:
    e+=1
d=2
while (d*e)%phi!=1:
    d+=1

enc=[]
for i in msg:
    tmp=ord(i)
    enc.append((tmp**e)%n)
print(str(enc))
dec=""
for i in enc:
    ans=(i**d)%n
    dec+=chr(ans)
print(dec)
