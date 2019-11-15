import json

def modul_speichern(modulname, credits, semester, vorlesungen ):
    try:
        with open('data/data.json') as open_file:    #Json-Datei öffnen/lesen
            json_daten = json.load(open_file)
    
    except FileNotFoundError:                       #wenn json.datei noch leer ist     
        formular_eingaben = {
            "modul_erfassen": [],
            "lernzeit_erfassen": []
        }
        
        liste_aller_module = json_daten["modul_erfassen"]
        
        modul = {
            "modulname": modulname,
            "credits": credits,
            "semester": semester,
            "vorlesungen": vorlesungen
        }
        
        liste_aller_module.append(modul)
        
        formular_eingaben["modul_erfassen"] = liste_aller_module
        return formular_eingaben      #Json-Datei mit neuer Eingabe wird zurückgegeben


    with open('data/data.json', "w") as open_file:
        json.dump(json_daten, open_file)









# youtube-Tutorial dazu: https://www.youtube.com/watch?v=drord9gbr3Y