def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "impossible"
    else:
        return a / b
    
operation = {"+" : add, "-" : subtract, "*" : multiply, "/" : divide}

should_accumulate = True
a = int(input("Enter the first number : "))
while should_accumulate:
    for symbol in operation :
        print(symbol)
    opertaion_symbol = input("pick an  operation : ")
    b = int(input("Enter the seconde number : ")) 
    answer = operation[opertaion_symbol](a,b)
    print(f"{a} {opertaion_symbol}  {b} = {answer}")

    print(f"type y to continue calculating {answer}, or type n to stop")
    choice = input()
    if choice == "y":
        a = answer
    else: 
        should_accumulate = False