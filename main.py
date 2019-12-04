from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from libs import datenspeichern_modul

app = Flask("Lernaufwandrechner")

@app.route("/")
def startseite():
    return render_template('startseite.html')


@app.route("/modulerfassen", methods=['GET', 'POST'])
def modulerfassen():
    if request.method == 'POST':
        print(request.form)
        modulname = request.form['modulname']
        credit = request.form['credits']
        semester = request.form['semester']
        vorlesungen = request.form['vorlesungen']
        returned_data = datenspeichern_modul.modul_speichern(modulname, credit, semester, vorlesungen)
    return render_template("modulerfassen.html")


@app.route("/moduluebersicht")
def moduluebersicht():
    modul_daten = datenspeichern_modul.load_json()
    return render_template("moduluebersicht.html", daten=modul_daten)


@app.route("/modulbearbeiten", methods=['GET', 'POST'])
def modulbearbeiten():
    if request.method == 'POST':
        modulname = request.form['modulname']
        credits = request.form['credits']
        semester = request.form['semester']
        vorlesungen = request.form['vorlesungen']
        modulnote = request.form['modulnote']
    return render_template("modulbearbeiten.html")


@app.route("/lernzeitdetail/<modul_name>")
def lernzeitdetail(modul_name):          #Parameter um die Lernzeit des richtigen Moduls zu bearbeiten
    print(modul_name)
    if request.method == 'POST':
        datum = request.form['datum']
        lernzeit = request.form['lernzeit']
    return render_template("lernzeitdetail.html")




if __name__ == "__main__":
    app.run(debug=True, port=5000)



