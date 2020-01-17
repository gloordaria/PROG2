from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from libs import datenspeichern_modul
from libs import datenspeichern_lernzeit

app = Flask("Lernaufwandrechner")

@app.route("/")
def startseite():
    """
    Zeigt die Startseite, wenn die  url/route '/' ist.
    
    Returns:
        template: Das template startseite.html wird übertragen 
    """
    return render_template('startseite.html')        #Diese Funktion gibt die Startseite zurück


@app.route("/modulerfassen", methods=['GET', 'POST'])   #Mit Get holt man die Formulareingaben vom Broser auf der seite /modulerfassen, mit Post schickt man die Formulardaten weiter an den Server
def modulerfassen():
    """
    Ein neues Modul kann erfasst werden
    Returns:
        template: Das template modulerfassen.html wird übertragen
    """

    #Diesen Teil brauche ich für die Variabelverwendung in der Python-Datei: datenspeichern_modul
    if request.method == 'POST':
        modulname = request.form['modulname']
        credit = request.form['credits']
        semester = request.form['semester']
        returned_data = datenspeichern_modul.modul_speichern(modulname, credit, semester)  
    
    return render_template("modulerfassen.html")    #User bleibt auf der gleichen Seite --> kein redirect


@app.route("/moduluebersicht")
def moduluebersicht():
    """
    Zeigt die Übersicht über alle erfassten Module
    Returns:
        template: Das template moduluebersicht.html wird übertragen
    """

    #Diesen Teil brauche ich um die Daten in der html-Datei moduluebersicht.html in die Liste zu speichern
    modul_daten = datenspeichern_modul.load_json()
    return render_template("moduluebersicht.html", daten=modul_daten)


@app.route("/modulbearbeiten/<modul_name>", methods=['GET', 'POST'])
def modulbearbeiten(modul_name):
    """
    Ein bestehendes Modul kann bearbeitet werden
    Args:
    modul_name: Daten aus Dictionary mit dem Key Modulname
    
    Returns:
        redirect: Nach bestätigung wir man auf die Seite moduluebersicht.html redirected
    """

    #Diesen Teil brauche ich für die Variabelverwendung in der Python-Datei: datenspeichern_modul
    if request.method == 'POST':
        modulname = request.form['modulname']
        credit = request.form['credits']
        semester = request.form['semester']
        modulnote = request.form['modulnote']
        modul_key = request.form['modul_key']
        returned_data = datenspeichern_modul.modul_bearbeiten(modul_key, modulname, credit, semester, modulnote)

        return redirect(url_for('moduluebersicht'))  #Direkte weiterleitung an die Modulübersicht

    modul_daten = datenspeichern_modul.load_json()
    return render_template("modulbearbeiten.html", daten=modul_daten['module'][modul_name], modul_key=modul_name) #Damit ich die Parameter im html verwenden kann hier die Variabeldefinidion


@app.route("/lernzeitdetail/<modul_name>", methods=['GET', 'POST'])
def lernzeitdetail(modul_name):                   #modul_name: Argument um die Lernzeit des richtigen Moduls zu bearbeiten
    """
    Ein bestehendes Modul kann bearbeitet werden
    Args:
    modul_name: Modulname als Key um die richtigen Daten für die Lernzeiterfassung aus dem Dictionary zu laden
    Returns:
        template: Das template lernzeitdetail.html wird übertragen
    """
    #Diesen Teil brauche ich für die Variabelverwendung in der Python-Datei: datenspeichern_lernzeit
    if request.method == 'POST':
        datum = request.form['datum']
        lernzeit = request.form['lernzeit']
        kommentare = request.form['kommentare']
        returned_data = datenspeichern_lernzeit.zeit_speichern(modul_name, datum, lernzeit, kommentare)
        
    
    #Diesen Teil brauche ich um die Formulardaten der erfassten Lernzeiten in der html-Datei lernzeitdetail.html zu verwenden
    lernzeit_daten = datenspeichern_modul.load_json()
    return render_template("lernzeitdetail.html", daten=lernzeit_daten['module'][modul_name])



if __name__ == "__main__":
    app.run(debug=True, port=5000)



