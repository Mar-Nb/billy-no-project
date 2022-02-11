from flask import Flask, render_template, request
from bibiConsole import bibiQuestion

appF = Flask(__name__)

@appF.route("/hello/")
@appF.route("/hello/<name>")
def hello_world(name = None):
    return render_template("hello.html", name = name)

@appF.route("/bibi")
def bibi():
    return render_template("api-flask-template.html")

@appF.route("/bibi-reponse", methods = ["POST"])
def bibiReponse():
    return "<p>" + bibiQuestion(request.form["question"]) + "</p><br><a href='/bibi'>Retour à la page de demande</a>"