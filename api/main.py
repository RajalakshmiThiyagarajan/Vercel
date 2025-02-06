import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data: marks of 100 imaginary students
students_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 75,
    "David": 60,
    "Eva": 95,
    # Add more students as needed
}

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [students_marks.get(name, None) for name in names]
    return jsonify(marks=marks)

if __name__ == '__main__':
    app.run()