from flask import Flask, render_template, redirect,request, flash, session
from flask_session import Session
from cs50 import *
from Modulos.helpers import login_required
from Modulos.usuarios import *
from werkzeug.security import generate_password_hash
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route("/login",methods = ["GET","POST"])
def login():
    error = None
    session.clear()
    if request.method == "GET":
        return render_template("login.html")
    elif request.method=="POST":
        username = request.form.get("user")
        password = request.form.get("pass")
        if not username or not password:
            error = "Error en las credenciales"
            return render_template("login.html",error = error)
        if UserLogin(username,password):
            session["userName"] = username
        else:
            error = "Error en las credenciales"
            return render_template("login.html",error = error)
        return redirect("/")

@app.route("/register", methods= ["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        username = request.form.get("user")
        correo = request.form.get("correo")
        pass1 = request.form.get("pass1")
        pass2 = request.form.get("pass2")
        if not username or not correo or not pass1 or not pass2 or (pass1 != pass2):
            error = "Todos los datos son necesarios"
            return render_template("register.html",error=error)
        UserRegister(username,generate_password_hash(pass1),correo)
        session["userName"] = username
        return redirect("/")

@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect("/login")