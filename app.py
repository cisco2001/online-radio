from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home() -> str:
    return "hello"

app.run(debug = True, port = 3000)
