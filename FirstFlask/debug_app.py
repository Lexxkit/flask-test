from flask import Flask

app = Flask(__name__)


@app.route("/divide/<int:x>/<int:y>/")
def divider(x, y):
    result = 0
    for i in range(x, y + 1):
        result += 1 / (x - i + 42)
    return str(result)


app.run('0.0.0.0', 8000, debug=True)