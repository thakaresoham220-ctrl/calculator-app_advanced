from flask import Flask, jsonify, request
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route("/")
def home():
    return "Calculator CI/CD app is running!"

@app.route("/add")
def addition():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify(result=add(a, b))

@app.route("/subtract")
def subtraction():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify(result=subtract(a, b))

@app.route("/multiply")
def multiplication():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify(result=multiply(a, b))

@app.route("/divide")
def division():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 1))
    try:
        return jsonify(result=divide(a, b))
    except ValueError as e:
        return jsonify(error=str(e)), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)