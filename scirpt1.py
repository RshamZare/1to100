# Simple Calculator
# Build a calculator that asks for two numbers and an operation (+, -, *, /), then prints the result.


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print(num1 + num2)

if operation == "-":
    print(num1 - num2)

if operation == "*":
    print(num1*num2)

if operation == "/":
    print(num1/num2)