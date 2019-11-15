import json

def lernzeit_speichern(datum, lernzeit):
    try:
        with open('data/data.json') as open_file:    #Json-Datei öffnen/lesen
            json_daten = json.load(open_file)
    
    except FileNotFoundError:                       #wenn json.datei noch leer ist     
        formular_eingaben = {
            "lernzeit_erfassen": []
        }

    #modul_erfassen  
    liste_aller_module = json_daten["modul_erfassen"]
        
    modul = {
        "modulname": modulname,
        "credits": credits,
        "semester": semester,
        "vorlesungen": vorlesungen
    }
        
    liste_aller_module.append(modul)
        
    formular_eingaben["modul_erfassen"] = liste_aller_module
    return formular_eingaben       #Json-Datei mit neuer Eingabe wird zurückgegeben


    with open('data/data.json', "w") as open_file:
        json.dump(formular_eingaben, open_file)





