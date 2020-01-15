import json

def modul_speichern(modulname, credit, semester ):    # Diese Funktion speichert einen neuen Eintrag
    
    json_daten = load_json()                          
    liste_aller_module = json_daten.get("module", {})    #Hier hole ich die Daten aus dem Dictionary ''module'' und weise sie der Variable zu 
        
    modul = {
        "modulname": modulname,
        "credits": int(credit),
        "semester": int(semester),
        "lernzeit_gesamt": int(0),
        "modulnote": "",
        "lernzeiten": {}
    }
        
    liste_aller_module[modulname] = modul               #Modulname als Key vom Verschachtelten-Dictionary
        
    json_daten["module"] = liste_aller_module

    save_to_json(json_daten)
    return json_daten                        #Json-Datei mit neuer Eingabe wird zurückgegeben

def modul_bearbeiten(modul_key, modulname, credit, semester, modulnote):   #Funktion zum Bearbeiten eines Moduls
    json_daten = load_json()
    liste_aller_module = json_daten.get("module", {})

    if modul_key == modulname:                                   #Wenn der Modulname nicht geändert wird aber etwas anderes muss der Key nicht verändert werden nur die Inhalte des Dictionaries   
        liste_aller_module[modulname]['credits'] = int(credit)
        liste_aller_module[modulname]['semester'] = int(semester)
        liste_aller_module[modulname]['modulnote'] = modulnote
    else:                                                           
        liste_aller_module[modulname] = liste_aller_module[modul_key]  #Wenn der Modulname geändert wird, verändert sich der Key des Dictionaries darum wird hier der Key überschireben mit der neuen Eingabe
        liste_aller_module.pop(modul_key)                               #Bisheriger Key wird gelöscht 
        liste_aller_module[modulname]['modulname'] = modulname
        liste_aller_module[modulname]['credits'] = int(credit)
        liste_aller_module[modulname]['semester'] = int(semester)
        liste_aller_module[modulname]['modulnote'] = modulnote
    
    json_daten["module"] = liste_aller_module

    save_to_json(json_daten)
    return json_daten
    

def load_json():   #Funktion dient dazu die Einträge vom Dictionary (Json-Datei) zu laden und mit deisen zu arbeiten
    json_daten = {}
    try:
        with open('data/data.json') as open_file:    #Json-Datei öffnen/lesen
            json_daten = json.load(open_file)
    
    except FileNotFoundError:                       #wenn json.datei noch leer ist     
        print("File not found")

    return json_daten                               #Alle Einträge in der Json-Datei werden ausgegeben


def save_to_json(daten):                #Neue Einträge in die Json-Datei speichern / hinzufügen
    with open('data/data.json', "w") as open_file:
        json.dump(daten, open_file)




