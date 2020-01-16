prog 2 - Projektidee Daria Gloor
Lernufwandrechner f�r das Studium

Ausgangslage
Anfangs Semester wird vorgegeben, welche Module absolviert werden und wie diese gewichtet sind. Nun stellt sich aber immer die Frage, wie viel Zeit man in ein Modul stecken soll?
Hier kann der Lernaufwandrechner helfen! 

Er soll Auskunft darüber geben wie viel Aufwand pro Modul ansteht und wie viel Aufwand nach Abzug der Lernaktivitäten noch verbleibt. Somit soll eine bessere Lernplanung während dem Semester gewährleistet werden, damit man während der Lernphase am Ende des Semesters nicht in den Stress kommt --> zumindest nicht aufgrund der Unwissenheit bezüglich des nötigen Lernaufwands ;)

Funktion/Projektidee:
Die Applikation ist dafür gedacht Studenten bei der Einteilung ihrer Lernzeit zu unterstützen. 
Am Anfang vom Semester sollen die Module und die entsprechenden Credits eingegeben werden und auf der Übersicht angezeigt werden wie hoch die empfohlene Lernzeit, aufgrund der Eingabe, für jedes Modul ist. W�hrend dem Semester sollen Lerneinträge wie Vorlesungen, Zusammenfassungen, Nachbearbeitung usw. erfasst werden. Die verbliebene Lernzeit soll in der Übersicht jederzeit angezeigt werden. Das kann helfen eine bessere Lernplanung vorzunehmen. Am Ende des Semesters bestetht die Möglichkeit die Modulnate einzutragen und so ein persönliches Fazit zu ziehen. 
 
Workflow:


- Dateneingabe
Um ein neues Modul zu erfassen navigiert der User wia Startseite oder Navigation auf die Seite modulerfassen.html und füllt die Pflichtfelder Semester, Modulname und Credits aus. Während des Semesters kann der User die Lernzeiten über die Seite lernzeitdetail.html mit Datum, Lernzeit und optional einem Kommentar erfassen. Am Schluss des Semesters, nach bekanntgabe der Noten, kann diese Information über die Seite modulbearbeiten.html ebenfalls eingegeben werden.


- Datenverarbeitung/Speicherung
Alle Daten werden in der Datei data.json in einem Dictionary gespeichert. Das Modul dient als Key und alle Informationen und Lernzeiteneinträge werden dort gespeichert. Die Gesamtlernzeit und die verbliebene Lernzeit wird aufgrund der Eingaben des Users berechnet. Will man die Moduleingaben verändern, ist dies über die Seite modulbearbeiten.html ebenfalls möglich 

- Datenausgabe

	- W�hrend des Semesters die verbliebenen Stunden f�r den Arbeitsaufwand
	- Aufwand/Ertrag Bilanz am Ende des Semesters

Feinheiten:
- Die Eingabe an Aufwand darf 24h nicht �berschreiten
- Es gibt keine höhere Note als eine 6
- Kommentarfelder haben eine begrenzte Anzahl Zeichen

Benutzeranleitung


