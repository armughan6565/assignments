def add(x,y):
    return x + y

def substracts(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def power(x,y):
    return pow(x,y)

print("select operation.")
print("1.add")
print("2.substract")
print("3.multiply")
print("4.divide")
print("5.power")

choice=input("enter choice (1/2/3/4/5):")
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

if choice == '1':
    print(num1, "+", num2,"=",add(num1,num2))
elif choice == '2':
    print(num1,"-", num2,"=", substracts(num1,num2))
elif choice == '3':
    print(num1,"*", num2,"=", multiply(num1,num2))
elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
elif choice == '5':
    print(num1,"^",num2,"=", power(num1,num2))
