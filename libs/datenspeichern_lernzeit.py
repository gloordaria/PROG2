import json

def zeit_speichern(datum, lernzeit, kommentare):

    json_daten = load_json()
    liste_lernzeiten = json_daten.get("lernzeiten", {})
        
    lerneintrag = {
        "datum": datum,
        "lernzeit": lernzeit, 
        "kommentare": kommentare 
    }

    liste_lernzeiten[datum] = lerneintrag                  #--> fraglich ob das Sinn macht, da Datum als Key gelten würde
    json_daten["lernzeiten"] = liste_lernzeiten

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
