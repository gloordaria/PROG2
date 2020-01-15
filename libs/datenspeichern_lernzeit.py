import json
from libs import datenspeichern_modul  #Damit ich die Funktionen nutzen kann
from datetime import datetime          #Damit ich mit den Datum arbeiten kann

def zeit_speichern(modul_name, datum, lernzeit, kommentare):  #Funktion eine erfasste Lernzeit in der Liste zu speichern
    modul_daten = datenspeichern_modul.load_json()
    json_daten = load_json()                            #Die Lerneinträge sollen zu einem Mdoul zugeweisen werden und deswegen betrifft es dasselbe Dictionary 
    
    lerneintrag = {
        "datum": datum,
        "lernzeit": lernzeit, 
        "kommentare": kommentare 
    }

    zeitstempel = str(datetime.now())                                         #Damit jeder Eintrag einen eindeutigen Key hat
    modul_daten["module"][modul_name]["lernzeiten"][zeitstempel] = lerneintrag

    lernzeit_gesamt = int(modul_daten["module"][modul_name]["lernzeit_gesamt"]) + int(lernzeit)   #Die gesammte Lernzeit errechnet sich aus der lernzeit plus dem neuen Eintrag
    modul_daten["module"][modul_name]["lernzeit_gesamt"] = lernzeit_gesamt


    json_daten["module"] = modul_daten["module"]
    save_to_json(json_daten)

    return json_daten


def load_json():
    json_daten = {}
    try:
        with open('data/data.json') as open_file:    #Json-Datei öffnen/lesen
            json_daten = json.load(open_file)

    except FileNotFoundError:                       #wenn json.datei noch leer ist     
        print("File not found")

    return json_daten


def save_to_json(daten):
    with open('data/data.json', "w") as open_file:
        json.dump(daten, open_file)
