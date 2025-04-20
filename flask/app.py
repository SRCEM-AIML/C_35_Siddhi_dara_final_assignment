from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        try:
            name = request.form['name']
            age = int(request.form['age'])
            return f"Hello, {name}! You are {age} years old."
        except ValueError:
            return "Invalid input for age. Please enter a number."
    return '''
        <form method="POST">
            Name: <input type="text" name="name"><br>
            Age: <input type="text" name="age"><br>
            <input type="submit" value="Submit">
        </form>
    '''
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
