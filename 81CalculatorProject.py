import os
def operation(a, operator, b):
    if operator == '+':
        c = a + b
    elif operator == '-':
        c = a - b
    elif operator == '*':
        c = a * b
    elif operator == '/':
        c = a // b
    else:
        print("Choose valid opertion")
    return c

def repeat(a):
    operator = input("+ \n - \n * \n / \n Pick an operation:")
    b = int(input("Enter next number:"))
    result = operation(a,operator,b)
    print(f"{a} {operator} {b} = {result}")
    print(f"Enter 'y' to  continue calculation with {result} or 'n'  to start new calculation or 'x' to exit:")
    operate = input()
    if operate == 'y':
        repeat(result)
    elif operate == 'n':
        os.system('cls')
        return
    elif operate == 'x':
        return 1
while True:
    a = int(input("Enter first number:"))
    flag = repeat(a)
    if flag == 1:
        break