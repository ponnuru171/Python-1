#x=str(input())
x=str(input())
def mail(p):
    z=(x[-1])
    y=(x[-4:-1])
    p=y + z
    if (p == ".com"):
        return p
k=list(filter(mail,x))
print(k)
