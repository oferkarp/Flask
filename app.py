from flask import Flask
from sport import sport_bp      
from news import news_bp      


app = Flask(__name__)
app.register_blueprint(sport_bp)
app.register_blueprint(news_bp)

@app.route('/')
def my_start():
    return  "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True, port=3000)