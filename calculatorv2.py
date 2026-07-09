
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
		<style>
			body { font-family: Arial, sans-serif; padding: 2rem; background-color: #216643; }
			input { padding: .5rem; margin: .25rem 0; }
			button { padding: .5rem 1rem; }
			.result { margin-top: 1rem; font-weight: bold; }
		</style>
	</head>
	<body>
		<h2 style="color: #d9622b;">Python Calculator</h2>
		<form method="post">
			<label>First number:<br><input name="num1" required></label><br>
			<label>Second number:<br><input name="num2" required></label><br>
			<label>Operation:<br>
				<select name="op">
					<option value="add">Add (+)</option>
					<option value="sub">Subtract (-)</option>
					<option value="mul">Multiply (*)</option>
					<option value="div">Divide (/)</option>
				</select>
			</label><br><br>
			<button type="submit">Calculate</button>
		</form>
		{% if result is not none %}
			<div class="result">Result: {{ result }}</div>
		{% endif %}
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

