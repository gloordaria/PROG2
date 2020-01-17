import json

def modul_speichern(modulname, credit, semester ):    
    """
    Erfassung eines neuen Modul  
    Args:
        modulname: Input Modulname von Formular in modulerfassen.html
        credit: Input Anzahl Credits von Formular in modulerfassen.html
        semester: Input welches Semester von Formular in modulerfassen.html
        modulnote: Input Modulnote von Formular in modulerfassen.html 
    Returns:
        dict: Alle Module aus dem dictionary in data.json
    """

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
    """
    Moduleingaben können bearbeitet weren  
    Args:
        modul_key: Falls der Modulname geändert wrid, wird dieser zum neuen Key im dictionary in json
        modulname: Bisheriger Modulname aus data.json
        credit: Anzahl Credits aus data.json
        semester: Semester aus data.json
        modulnote: Modulnote aus data.json 
    Returns:
        dict: Alle Module aus dem dictionary in data.json
    """ 
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
    

def load_json():  
    """
    Ladet alle Module vom json file  
    Args:
        json_path: path to json file
    Returns:
        dict: Ein dictionary welches alle Module enthält, wenn das File nicht exisitert wird "File not found" zurückgegeben
    """ 

    json_daten = {}
    try:
        with open('data/data.json') as open_file:    #Json-Datei öffnen/lesen
            json_daten = json.load(open_file)
    
    except FileNotFoundError:                       #wenn json.datei noch leer ist     
        print("File not found")

    return json_daten                               #Alle Einträge in der Json-Datei werden ausgegeben


def save_to_json(daten):                
    """
     Speichert alle Module in the json-datei 
   
    Args:
        json_path: path to json file
        daten: alle Module
    """ 
    with open('data/data.json', "w") as open_file:
        json.dump(daten, open_file)




