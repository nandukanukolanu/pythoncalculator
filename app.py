from flask import Flask, render_template, request, jsonify
import math
from collections import deque
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)

# Store calculation history (last 5 calculations)
calculation_history = deque(maxlen=5)

# Background color configuration from environment variables
DEFAULT_BG_COLOR = "linear-gradient(135deg, #FF6B9D 0%, #C44569 100%)"
BG_COLOR = os.getenv('BG_COLOR', DEFAULT_BG_COLOR)

def safe_eval(expression):
    """Safely evaluate mathematical expressions"""
    try:
        # Remove spaces
        expression = expression.replace(" ", "")
        # Allow only safe mathematical operations
        allowed_chars = set("0123456789+-*/.()%")
        if not all(c in allowed_chars for c in expression):
            return None
        # Evaluate the expression
        result = eval(expression)
        return round(result, 10)  # Round to avoid floating point errors
    except:
        return None

def calculate_percentage(value, percentage=None):
    """Calculate percentage. If percentage is None, return value as percentage (value/100)
    Otherwise return percentage% of value"""
    try:
        value = float(value)
        if percentage is None:
            # Return value as percentage (divide by 100)
            return round(value / 100, 10)
        else:
            # Return percentage% of value
            percentage = float(percentage)
            return round((percentage / 100) * value, 10)
    except:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/config', methods=['GET'])
def get_config():
    """Return background color configuration"""
    return jsonify({'backgroundColor': BG_COLOR})

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression', '')
    
    if not expression:
        return jsonify({'error': 'Empty expression'}), 400
    
    result = safe_eval(expression)
    
    if result is None:
        return jsonify({'error': 'Invalid expression'}), 400
    
    # Add to history
    history_item = {
        'expression': expression,
        'result': result
    }
    calculation_history.append(history_item)
    
    return jsonify({'result': result})

@app.route('/percentage', methods=['POST'])
def percentage():
    data = request.get_json()
    value = data.get('value', '')
    percentage = data.get('percentage')
    
    if not value:
        return jsonify({'error': 'Empty value'}), 400
    
    result = calculate_percentage(value, percentage)
    
    if result is None:
        return jsonify({'error': 'Invalid calculation'}), 400
    
    return jsonify({'result': result})

@app.route('/history', methods=['GET'])
def get_history():
    # Return history in reverse order (most recent first)
    history_list = list(reversed(calculation_history))
    return jsonify({'history': history_list})

@app.route('/clear', methods=['POST'])
def clear():
    return jsonify({'status': 'cleared'})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
