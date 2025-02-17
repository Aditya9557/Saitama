#random number
import random
n1=random.randint(1,9)
n2=random.randint(1,9)
ans=eval(input("what is "+ str(n1)+"+"+str(n2)+"?"))
print("Your ans is ",n1+n2==ans)
x = True
y = False

print(x and y)
print(x or y)
print(not x)

a=[1,2,3]
b=a
c=[1,2,3]
print(a is b)
print(a is c)
print(a is not c)

