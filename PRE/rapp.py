from flask import Flask, render_template, request
import random




def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"


def generate_problem(operation, difficulty_level='easy'):
    if difficulty_level == 'easy':
        x, y = random.randint(1, 10), random.randint(1, 10)
    else:  
        x, y = random.randint(1, 100), random.randint(1, 100)
    
    
    if operation == 'add':
        return f"{x} + {y}"
    elif operation == 'subtract':
        return f"{x} - {y}"
    elif operation == 'multiply':
        return f"{x} * {y}"
    elif operation == 'divide':
        while y == 0:  
            y = random.randint(1, 10)
        return f"{x} / {y}"


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    problem = None
    number1 = ""
    number2 = ""
 

    if request.method == 'POST':
        if 'calculate' in request.form:
            number1 = request.form['number1']  
            number2 = request.form['number2']  
            operation = request.form['operation']
            
            try:
                number1 = float(number1)  
                number2 = float(number2) 

                if operation == 'add':
                    result = add(number1, number2)
                elif operation == 'subtract':
                    result = subtract(number1, number2)
                elif operation == 'multiply':
                    result = multiply(number1, number2)
                elif operation == 'divide':
                    result = divide(number1, number2)
            except ValueError:
                result = "Invalid input"

        
        if 'generate_problem' in request.form:
            operation = request.form['operation']
            difficulty = request.form['difficulty']
            problem = generate_problem(operation, difficulty)

       

    return render_template('index.html', result=result, problem=problem, number1=number1, number2=number2)

if __name__ == '__main__':
    app.run(debug=True)
