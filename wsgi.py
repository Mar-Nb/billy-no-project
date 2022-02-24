from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

from bibiConsole import bibiQuestion
import json

appF = Flask(__name__)
CORS(appF, support_credentials=True)

@appF.route("/hello/")
@appF.route("/hello/<name>")
def hello_world(name = None):
    return render_template("hello.html", name = name)

@appF.route("/bibi")
def bibi():
    return render_template("api-flask-template.html")

@appF.route("/bibi-reponse", methods = ["POST"])
@cross_origin(supports_credentials=True)
def bibiReponse():
    jsondata = {"reponse": bibiQuestion(request.form["question"])}
    print(json.dumps(jsondata))
    return json.dumps(jsondata)