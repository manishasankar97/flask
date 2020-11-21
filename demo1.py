from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route("/")
def about():
    return "<h1> style='color: red'>About!!!!</h1>"

@app.route("/sign_up")
def sign_up():
    return render_template("public/demo1.html")

if __name__ == "__main__":
    app.run(debug = True)