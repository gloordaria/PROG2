from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for

app = Flask("Lernaufwandrechner")

@app.route("/")
def startseite():
    return render_template('startseite.html')


@app.route("/modulerfassen")
def modulerfassen():
    return render_template("modulerfassen.html")

@app.route("/moduluebersicht")
def moduluebersicht():
    return render_template("moduluebersicht.html")

@app.route("/lernzeit")
def lernzeit():
    return render_template("lernzeit.html")

@app.route("/lernzeitdetail")
def lernzeitdetail():
    return render_template("lernzeitdetail.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)



