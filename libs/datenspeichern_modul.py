import json

def modul_speichern(modulname, credit, semester ):
    
    json_daten = load_json()
    liste_aller_module = json_daten.get("module", {})
        
    modul = {
        "modulname": modulname,
        "credits": int(credit),
        "semester": int(semester),
        "lernzeit_gesamt": int(0),
        "lernzeiten": {}
    }
        
    liste_aller_module[modulname] = modul
        
    json_daten["module"] = liste_aller_module

    save_to_json(json_daten)
    return json_daten                        #Json-Datei mit neuer Eingabe wird zurückgegeben

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




# youtube-Tutorial dazu: https://www.youtube.com/watch?v=drord9gbr3Y