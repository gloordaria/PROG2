import json
from libs import datenspeichern_modul
from datetime import datetime

def zeit_speichern(modul_name, datum, lernzeit, kommentare):
    modul_daten = datenspeichern_modul.load_json()
    json_daten = load_json()
    #liste_lernzeiten = json_daten.get("lernzeiten", {})
    
    lerneintrag = {
        "datum": datum,
        "lernzeit": lernzeit, 
        "kommentare": kommentare 
    }

    zeitstempel = str(datetime.now())
    modul_daten["module"][modul_name]["lernzeiten"][zeitstempel] = lerneintrag

    lernzeit_gesamt = int(modul_daten["module"][modul_name]["lernzeit_gesamt"]) + int(lernzeit)
    modul_daten["module"][modul_name]["lernzeit_gesamt"] = lernzeit_gesamt

    # liste_lernzeiten[datum] = lerneintrag                  #--> fraglich ob das Sinn macht, da Datum als Key gelten würde
    #json_daten["lernzeiten"] = liste_lernzeiten

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
