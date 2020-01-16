# PROG2 - Projektidee Daria Gloor
# Lernufwandrechner für das Studium

## Ausgangslage
Anfangs Semester wird vorgegeben, welche Module absolviert werden und wie diese gewichtet sind. Nun stellt sich aber immer die Frage, wie viel Zeit man in ein Modul stecken soll?

Hier kann der Lernaufwandrechner helfen! 

Er soll Auskunft darüber geben wie viel Aufwand pro Modul ansteht und wie viel Aufwand nach Abzug der Lernaktivitäten noch verbleibt. Somit soll eine bessere Lernplanung während dem Semester gewährleistet werden, damit man während der Lernphase am Ende des Semesters nicht in den Stress kommt --> zumindest nicht aufgrund der Unwissenheit bezüglich des nötigen Lernaufwands ;)

## Funktion/Projektidee:
Die Applikation ist dafür gedacht Studenten bei der Einteilung ihrer Lernzeit zu unterstützen. Am Anfang vom Semester sollen die Module und die entsprechenden Credits eingegeben werden und auf der Übersicht angezeigt werden wie hoch die empfohlene Lernzeit, aufgrund der Eingabe, für jedes Modul ist. Während dem Semester sollen Lerneinträge wie Vorlesungen, Zusammenfassungen, Nachbearbeitung usw. erfasst werden. Die verbliebene Lernzeit soll in der Übersicht jederzeit angezeigt werden, was dazu helfen kann eine bessere Lernplanung vorzunehmen. Am Ende des Semesters bestetht die Möglichkeit die Modulnate einzutragen und so ein persönliches Fazit zu ziehen. 
 
## Workflow

### Ablaufdiagramm
![Bildtext](C:\Users\daria\prog2\lar\static\Ablaufdiagramm_Screens.jpg "Ablaufdiagramm")

### Wireframe

### Dateneingabe
Um ein neues Modul zu erfassen navigiert der User wia Startseite oder Navigation auf die Seite modulerfassen.html und füllt die Pflichtfelder Semester, Modulname und Credits aus. Während des Semesters kann der User die Lernzeiten über die Seite lernzeitdetail.html mit Datum, Lernzeit und optional einem Kommentar erfassen. Am Schluss des Semesters, nach Bekanntgabe der Noten, kann diese Information über die Seite modulbearbeiten.html ebenfalls eingegeben werden.

### Datenverarbeitung/Speicherung
Alle Daten werden in der Datei data.json in einem Dictionary gespeichert. Das Modul dient als Key und alle Informationen zum Modul und alle Lernzeiteneinträge werden dort gespeichert. Die Gesamtlernzeit und die verbliebene Lernzeit wird aufgrund der Eingaben des Users berechnet. Will man die Moduleingaben verändern, ist dies über die Seite modulbearbeiten.html ebenfalls möglich. 

### Datenausgabe
Die eingegebenen Formulardaten von der Erfassung der Module, Lernzeiten und Modulnoten können in der Modulübersicht eingesehen werden. Die Auflistung der Lernzeiten wird separat auf lernzeitdetail.html ausgegeben. Die Berechnungen des Gesamtlernaufwandes und des verbliebenen Lernaufwands werden ebenfalls ausgegeben. 

### Feinheiten
- Die Eingabe an Lernaufwand darf 24h nicht überschreiten.
- Es gibt keine höhere Note als eine 6.
- Texteingabefelder haben eine begrenzte Anzahl Zeichen.
- Einzele Felder sind Pflicht und ohne eine entsprechende Eingabe läuft das Programm nicht weiter. 

## Benutzeranleitung

### Am Anfang des Semesters - Ein neues Modul erfassen 
1. Man startet auf der Startseite und hat die Möglichkeit ein Modul zu erfassen oder in die Modulübersicht zu wechseln.
	a. Wenn noch keine Module erfasst sind, ist die Übersicht leer. 
	
2. Um ein neues Modul zu erfassen auf den Button "Ein neues Modul erfassen" klicken. 

3. Eingaben entsprechend vornehmn: 
	a. Semester wia Dropdown auswählen
	b. Modulnamen eingeben
	c. Anzahl Credits via Dropdown auswählen

4. Mit dem Button "Bestätigen" das Modul erfassen
	
4. Um die Einträge zu sehen nun via Button "Zur Modulübersicht" auf die Modulübersicht navigieren

5. Hier sind die eingegebenen Modulinformationen einsehbar und zusätzlich wurde der Gesamtlernaufwand in der Spalte "Aufwand insgesammt (min)" berechnet

### Während des Semesters - Lerneinträge erfassen 
1. Modulübersicht wia Startseite oder Navigation öffnen

2. In der Spalte Lernaufwand auf die unterstrichene Zahl klicken
	a. Ist noch kein Aufwand erfasst, auf die unterstrichene Null klicken
	
3. Nun kann der Lernaufwand erfasst werden mit den Eingaben:
	a. Datum
	b. Lernzeit (in Minuten)
	c. Optional einen Kommentar erfassen
	
4. Der erfasste Eintrag wird der Liste unterhalb hinzugefügt

5. Navigiert man zurück auf die Modulübersicht, ist die erfasste Lernzeit ersichtlich und es wird angezeigt, wie viel Lernaufwand noch übrig bleibt
	a. Nach jeder weiteren Erfassung der Lernzeit werden sich diese beiden Zahlen entsprechend verändern

### Änderungen der Modulinformationen
1. Modulübersicht wia Startseite oder Navigation öffnen

2. In der Spalte Modulname auf den unterstrichenen Modulnamen klicken

3. Hier hat man die Möglichkeit Änderungen zu den eingegebenen Modulinformationen vorzunehmen:
	a. Semester
	b. Modulname
	c. Credits
	
4. Für die erfolgreiche Änderung auf den Button "Bestätigen" klicken

5. Direkte Weiterleitung an die Modulübersicht 

### Am Ende des Semesters - Modulnote erfassen
1. Modulübersicht wia Startseite oder Navigation öffnen

2. In der Spalte Modulnote auf das unterstrichene Wort "erfassen" klicken 

3. Modulnote im entsprechenden Feld eintragen und auf den Button "Bestätigen" klicken

4. Direkte Weiterleitung an die Modulübersicht 





