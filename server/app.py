#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text

@app.route('/count/<int:num>')
def count(num):
    numbers = [str(i) for i in range(num)]
    # Join with newline characters and add a trailing newline
    return "\n".join(numbers) + "\n"

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            result = "Error: Division by zero"
        else:
            result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            result = "Error: Modulus by zero"
        else:
            result = num1 % num2
    else:
        result = "Invalid operation"
    return str(result)

if __name__ == '__main__':
    app.run(port=5555)
