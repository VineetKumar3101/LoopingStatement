print('-----------------------------------------------------------')

#LOOPING STATEMENT

#WHILE LOOP

a=int(input("Enter"))
i=1
while(i<=a):
    print(i,end=' ')
    i=i+1

print('\n-----------------------------------------------------------')

#Sum Of Natrual Number
b=int(input("Enter"))
j=1
sum=0
while(j<=b):
    print(j, end=' ')
    sum = sum + j
    j = j + 1
print("\nSum = ",sum)

print('\n-----------------------------------------------------------')

#FOR LOOP

#print natural numbers
c=int(input("Enter"))
for i in range(1,c+1):
    print(i,end=' ')

print('\n-----------------------------------------------------------')

#sum of natural numbers
d=int(input("Enter"))
sum=0
for i in range(1,d+1):
    print(i,end=' ')
    sum=sum+i
print("\nSum = ",sum)

print('\n-----------------------------------------------------------')

#range Check
for i in range(90,101):
    print(i,end=' ')

print('\n-----------------------------------------------------------')

#+2 in series odd number
for i in range(1,10,2):
    print(i,end=' ')

print('\n-----------------------------------------------------------')

#+2 in series even number
for i in range(2,10,2):
    print(i,end=' ')

print('\n-----------------------------------------------------------')

#decrement option
for i in range(10,-1,-1):
    print(i,end=' ')

print('\n-----------------------------------------------------------')

#Factorial Program
e=int(input("Enter = "))
fact=1
for i in range(1,e+1):
    print(i, end=' ')
    fact=fact*i
print("\n Factorial = ",fact)


print('\n-----------------------------------------------------------')