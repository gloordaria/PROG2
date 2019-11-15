from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for

app = Flask("Lernaufwandrechner")

@app.route("/")
def startseite():
    return render_template('startseite.html')


@app.route("/modulerfassen", methods=['GET', 'POST'])
def modulerfassen():
    if request.method == 'POST':
        modulname = request.form['modulname']
        credits = request.form['credits']
        semester = request.form['semester']
        vorlesungen = request.form['vorlesungen']
    return render_template("modulerfassen.html")


@app.route("/moduluebersicht")
def moduluebersicht():
    return render_template("moduluebersicht.html")


@app.route("/lernzeit_erfassen")
def lernzeit_erfassen():
    if request.method == 'POST':
        datum = request.form['datum']
        lernzeit = request.form['lernzeit']
    return render_template("lernzeit.html")


@app.route("/lernzeitdetail")
def lernzeitdetail():
    return render_template("lernzeitdetail.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)



