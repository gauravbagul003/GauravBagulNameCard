from flask import Flask,request,render_template
from flask_cors import cross_origin
app = Flask(__name__)

@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")

if __name__== "__main__":
    app.run(debug=True)