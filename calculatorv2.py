
from flask import Flask, request, render_template_string

app = Flask(__name__)

def add(x, y):
		return x + y

def subtract(x, y):
		return x - y

def multiply(x, y):
		return x * y

def divide(x, y):
		if y == 0:
				return "Error: Cannot divide by zero!"
		return x / y

TEMPLATE = """
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Calculator UI</title>
		<link rel="stylesheet" href="/static/style.css">
	</head>
	<body>
		<div class="card">
			<h2>Python Calculator</h2>
			<form method="post">
				<label>First number:<br><input name="num1" required></label><br>
				<label>Second number:<br><input name="num2" required></label><br>
				<label>Operation:</label>
				<div class="operation-group">
					<button type="submit" name="op" value="add" class="op-btn">Add +</button>
					<button type="submit" name="op" value="sub" class="op-btn">Subtract -</button>
					<button type="submit" name="op" value="mul" class="op-btn">Multiply ×</button>
					<button type="submit" name="op" value="div" class="op-btn">Divide ÷</button>
				</div><br>
			</form>
			{% if result is not none %}
				<div class="result">Result: {{ result }}</div>
			{% endif %}
		</div>
	</body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def index():
		result = None
		if request.method == 'POST':
				try:
						num1 = float(request.form['num1'])
						num2 = float(request.form['num2'])
						op = request.form['op']
				except (ValueError, KeyError):
						result = 'Invalid input!'
				else:
						if op == 'add':
								result = add(num1, num2)
						elif op == 'sub':
								result = subtract(num1, num2)
						elif op == 'mul':
								result = multiply(num1, num2)
						elif op == 'div':
								result = divide(num1, num2)
		return render_template_string(TEMPLATE, result=result)


if __name__ == '__main__':
		app.run(host='0.0.0.0', port=5000, debug=True)

