x=int(input("enter the x value "))
y=int(input("enter the y value "))
for no in range(x,y):
    if no > 1:
         for i in range(2,no):
             if(no % i) == 0:
                 break
         else:
             print(no)
s=[]
print(list(no))
