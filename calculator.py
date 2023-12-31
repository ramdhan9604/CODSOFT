def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def division(x,y):
    if y!=0:
        return x/y
    else:
        return "Error:Division by zero"
    
num1 = float(input("Enter your first number:"))
num2 = float(input("Enter your second number:"))

print("Select operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice(1/2/3/4)")

if choice in('1','2','3','4'):
    if choice=='1':
        result = add(num1,num2)
        operation = "+"
    elif choice=='2':
        result = subtract(num1,num2)
        operation ="-"
    elif choice=='3':
        result = multiply(num1,num2)
        operation= "*"
    elif choice=='4':
        result=division(num1,num2)
        operation="/"

    if isinstance(result,float):
        print(f"{num1}{operation}{num2}={result:.2f}")
    else:
        print(result)
else:
    print("Invalid choice. Please enter valid choice operations.")


