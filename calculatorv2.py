
from flask import Flask, request, render_template_string, url_for
from converter import UnitConverter

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
from home import HOME_TEMPLATE

# Initialize converter
unit_converter = UnitConverter()

CALCULATOR_TEMPLATE = """
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>{{ title }}</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="card">
            <h2>{{ title }}</h2>
            <form method="post">
                <div class="input-group">
                    <label>First number:<br><input name="num1" required></label>
                    <button type="button" class="ans-btn" onclick="fillAns('num1')">ans</button>
                </div><br>
                <div class="input-group">
                    <label>Second number:<br><input name="num2" required></label>
                    <button type="button" class="ans-btn" onclick="fillAns('num2')">ans</button>
                </div><br>
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
                <script>localStorage.setItem('lastAnswer', '{{ result }}');</script>
            {% endif %}
            <a class="back-link" href="{{ url_for('home') }}">← Back to Home</a>
        </div>
        <script>
            function fillAns(fieldName) {
                const lastAns = localStorage.getItem('lastAnswer');
                if (lastAns) {
                    document.querySelector('input[name="' + fieldName + '"]').value = lastAns;
                }
            }
        </script>
    </body>
</html>
"""


CONVERTER_TEMPLATE = """
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Unit Converter</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="card">
            <h2>Unit Converter</h2>
            <form method="post">
                <label>Conversion Type:</label>
                <select name="conversion_type" required onchange="updateUnits()">
                    <option value="">-- Select Type --</option>
                    <option value="speed">Speed (km/h ↔ mph)</option>
                    <option value="temperature">Temperature (°C ↔ °F ↔ K)</option>
                    <option value="length">Length (m, km, cm, mm, mi, yd, ft, in)</option>
                    <option value="weight">Weight (g, kg, mg, lb, oz)</option>
                </select><br><br>
                
                <div class="input-group">
                    <label>Value:</label>
                    <input type="number" name="value" required step="any">
                    <button type="button" class="ans-btn" onclick="fillAns('value')">ans</button>
                </div><br>
                
                <label>From Unit:</label>
                <select name="from_unit" id="from_unit" required>
                    <option value="">-- Select Unit --</option>
                </select><br><br>
                
                <label>To Unit:</label>
                <select name="to_unit" id="to_unit" required>
                    <option value="">-- Select Unit --</option>
                </select><br><br>
                
                <button type="submit" class="op-btn">Convert</button>
            </form>
            
            {% if result is not none %}
                <div class="result">
                    {{ value }} {{ from_unit }} = <strong>{{ result }}</strong> {{ to_unit }}
                </div>
                <script>localStorage.setItem('lastAnswer', '{{ result }}');</script>
            {% endif %}
            
            {% if error %}
                <div class="error">{{ error }}</div>
            {% endif %}
            
            <a class="back-link" href="{{ url_for('home') }}">← Back to Home</a>
        </div>
        
        <script>
            const units = {
                speed: ['km/h', 'mph'],
                temperature: ['celsius', 'fahrenheit', 'kelvin'],
                length: ['meters', 'kilometers', 'centimeters', 'millimeters', 'miles', 'yards', 'feet', 'inches'],
                weight: ['grams', 'kilograms', 'milligrams', 'pounds', 'ounces']
            };
            
            function updateUnits() {
                const type = document.querySelector('select[name="conversion_type"]').value;
                const fromUnit = document.getElementById('from_unit');
                const toUnit = document.getElementById('to_unit');
                
                fromUnit.innerHTML = '<option value="">-- Select Unit --</option>';
                toUnit.innerHTML = '<option value="">-- Select Unit --</option>';
                
                if (type && units[type]) {
                    units[type].forEach(unit => {
                        fromUnit.innerHTML += `<option value="${unit}">${unit}</option>`;
                        toUnit.innerHTML += `<option value="${unit}">${unit}</option>`;
                    });
                }
            }
            
            function fillAns(fieldName) {
                const lastAns = localStorage.getItem('lastAnswer');
                if (lastAns) {
                    document.querySelector('input[name="' + fieldName + '"]').value = lastAns;
                }
            }
        </script>
    </body>
</html>
"""


@app.route('/')
def home():
    return render_template_string(HOME_TEMPLATE)


@app.route('/converter', methods=['GET', 'POST'])
def converter():
    result = None
    error = None
    value = None
    from_unit = None
    to_unit = None
    
    if request.method == 'POST':
        try:
            conversion_type = request.form.get('conversion_type', '')
            value = float(request.form.get('value', 0))
            from_unit = request.form.get('from_unit', '').lower()
            to_unit = request.form.get('to_unit', '').lower()
            
            if not all([conversion_type, from_unit, to_unit]):
                error = "Please select all fields"
            elif from_unit == to_unit:
                result = value
            else:
                if conversion_type == 'speed':
                    # Convert speed using the conversion formulas
                    if from_unit == 'km/h' and to_unit == 'mph':
                        result = round(value * 0.621371, 4)
                    elif from_unit == 'mph' and to_unit == 'km/h':
                        result = round(value * 1.60934, 4)
                    else:
                        error = "Invalid speed units"
                elif conversion_type == 'temperature':
                    result = unit_converter.convert_temperature(value, from_unit, to_unit)
                elif conversion_type == 'length':
                    result = unit_converter.convert_length(value, from_unit, to_unit)
                elif conversion_type == 'weight':
                    result = unit_converter.convert_weight(value, from_unit, to_unit)
                else:
                    error = "Invalid conversion type"
                    
                if isinstance(result, str):
                    error = result
                    result = None
        except ValueError:
            error = "Please enter a valid number"
        except Exception as e:
            error = f"Error: {str(e)}"
    
    return render_template_string(CONVERTER_TEMPLATE, result=result, error=error, value=value, from_unit=from_unit, to_unit=to_unit)


@app.route('/calculator/<version>', methods=['GET', 'POST'])
def calculator(version):
    result = None
    title = 'Calculator'

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

    return render_template_string(CALCULATOR_TEMPLATE, result=result, title=title)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

