from flask import Flask,render_template,request
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login",methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "zhangsan" and password=="123":
            return "<h1>welcome, %s !</h1>" %username
        else:
            return "<h1>login Failure !</h1>"    
    else:
        return "<h1>login Failure !</h1>"


if __name__ == '__main__':
    app.run('0.0.0.0',5000)