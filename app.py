from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression', '')
    
    if not expression:
        return jsonify({'error': 'Empty expression'}), 400
    
    result = safe_eval(expression)
    
    if result is None:
        return jsonify({'error': 'Invalid expression'}), 400
    
    return jsonify({'result': result})

@app.route('/clear', methods=['POST'])
def clear():
    return jsonify({'status': 'cleared'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
