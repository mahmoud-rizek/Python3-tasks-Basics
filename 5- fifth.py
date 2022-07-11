num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

for i in range(101):
   if i%num1==0 or i%num2==0:
    print(i)

