from flask import Flask , render_template,request,redirect, url_for
from sport import sport_bp      
from news import news_bp      


app = Flask(__name__)
app.register_blueprint(sport_bp)
app.register_blueprint(news_bp)

@app.route('/' , methods=['GET','POST'])
def my_start():
    user_name = request.form.get("username")
    password = request.form.get("password")
    number_x = request.form.get("X")
    number_y = request.form.get("Y")
    if user_name == "ofer" and password == "1234":
        return redirect(url_for('news.news', myname=user_name))
    if number_x is not None and number_y is not None:
        number_x = int(number_x)
        number_y = int(number_y)
        result = number_x * number_y
        return str(result) 
    print(f" ***** {user_name}-{password}")
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port=3000)