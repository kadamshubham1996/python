n=int(input("number of element "))
b=[]
for i in range(0,n):
    a=int(input("enter the number: "))
    b.append(a)
avg=sum(a)/n
print("Average of list",round(avg,2))
