from flask import Flask
app = Flask(__name__)

@app.route('/')
def calc():
    while True:
        question = input("Input the operation (+, -, /, *, exit): ")
        result = 0
        if question == "exit":
            break

        num1 = int(input("Input first number: "))
        num2 = int(input("Input second number: "))

        if question == "+":
            result = num1 + num2
        elif question == "-":
            result = num1 - num2
        elif question == "/":
            if num2 == 0:
                print("You can't divide by zero")
            else:
                result = num1 / num2
        elif question == "*":
            result = num1 * num2
        else:
            print("Incorrect data was entered")

        print("Result: ", result)
