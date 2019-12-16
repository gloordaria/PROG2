from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from libs import datenspeichern_modul
from libs import datenspeichern_lernzeit
from libs import modul_bearbeiten

app = Flask("Lernaufwandrechner")

@app.route("/")
def startseite():
    return render_template('startseite.html')     #Diese Funktion gibt die Startseite zurück


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
    #Diesen Teil brauche ich um die Daten in der html-Datei moduluebersicht.html in die Liste zu speichern
    modul_daten = datenspeichern_modul.load_json()
    return render_template("moduluebersicht.html", daten=modul_daten)


@app.route("/modulbearbeiten", methods=['GET', 'POST'])
def modulbearbeiten():
    #Dieser Teil brauche ich für die Variabelverwendung in der Python-Datei: datenspeichern_modul
    if request.method == 'POST':
        modulname = request.form['modulname']
        credits = request.form['credits']
        semester = request.form['semester']
        vorlesungen = request.form['vorlesungen']
        modulnote = request.form['modulnote']
    return render_template("modulbearbeiten.html")


@app.route("/lernzeitdetail/<modul_name>", methods=['GET', 'POST'])
def lernzeitdetail(modul_name):                   #Parameter um die Lernzeit des richtigen Moduls zu bearbeiten
    #Diesen Teil brauche ich für die Variabelverwendung in der Python-Datei: datenspeichern_lernzeit
    if request.method == 'POST':
        datum = request.form['datum']
        lernzeit = request.form['lernzeit']
        kommentare = request.form['kommentare']
        returned_data = datenspeichern_lernzeit.zeit_speichern(modul_name, datum, lernzeit, kommentare)
        #return returned_data
    
    #Diesen Teil brauche ich um die Daten in der html-Datei moduluebersicht.html in die Liste zu speichern
    lernzeit_daten = datenspeichern_modul.load_json()
    #return lernzeit_daten
    return render_template("lernzeitdetail.html", daten=lernzeit_daten['module'][modul_name])




if __name__ == "__main__":
    app.run(debug=True, port=5000)



