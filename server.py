from flask import Flask, render_template, url_for
app = Flask(__name__) #This instantiates the server app
print(__name__)

# decorator -  every time we type and run the / sign (called route as well) it defines the below function and runs it
@app.route("/index.html")
def index_p():
    return render_template("index.html")