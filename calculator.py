# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVIDE

print("select an operation to preform: ")

print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == "1":
    # code for add
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print(f"result is {int(num1) + int(num2)}")
elif operation == "2":
    # code for subtract
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print(f"result is {int(num1) - int(num2)}")
elif operation == "3":
    # code for multiply
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print(f"result is {int(num1) * int(num2)}")
elif operation == "4":
    # code for divide
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print(f"result is {int(num1) / int(num2)}")
else:
    print("Invalid Entry")