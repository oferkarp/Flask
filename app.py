from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("hello")
    return "<p>Hello, World!</p>"

@app.route("/news")
def news():
    return "<p>This is the NEWS</p>"

@app.route("/sport")
def sport():
    return "<p>This is the SPORT section</p>"

if __name__ == '__main__':
    app.run(debug=True, port=9000)