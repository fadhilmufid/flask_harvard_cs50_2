from flask import Flask, render_template, request, redirect
import os
import csv
#configure app
app = Flask(__name__)

#Registered Students
WORDS=[]
with open("words.txt","r") as file:
    for line in file.readlines():
        WORDS.append(line.rstrip())

@app.route("/")
def index():
    render_template("index.html")

@app.route("/search")
def search():
    #Notes For Loop Example
    """
    words=[]
    q = request.args.get("q")
    for word in WORDS:
        if word.startswith(q):
            words.append(word)
    """
    words = [word for word in WORDS if word.startswith(request.args.get("q"))]
    render_template("search.html", words=words)


if __name__ == "__main__":
    app.run()

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, '/templates')
app = Flask(__name__, template_folder=template_path)