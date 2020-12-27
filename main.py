from pass_gen import pass_gen
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    password = pass_gen.generate_pass(10)
    
    return render_template("index.html", genpass=password)

if __name__ == "__main__":
    app.run(debug=True)

