Projektidee Daria Gloor
--> Lernufwandrechner f�r das Studium

Ausgangslage:
Anfangs Semester wird vorgegeben, welche Module absolviert werden und wie diese gewichtet sind. Nun stellt sich aber immer die Frage, wie viel Zeit man in ein Modul stecken soll.
Hier kann der Lernaufwandrechner helfen! Mit diesem können neue Module mit der entsprechenden Anzahl Credits erfasst und somit wird der Gesamtaufwand dargestellt. Während des Semesters können neue Lerneinträge erstellt werden und der verblibene Zeitaufwand wird angezeigt. 

Jedes Modul im Studium ist mit sogenannten Credits gewichtet. Je nach H�he der Credits ist der empfohlene Lernaufwand unterschriedlich.
Damit anfangs Semester klar ist, wie viel Zeit ein Modul beansprucht um die Wochen- und Lernplanung optimal zu gestalten

Funktion/Projektidee:
Die Idee ist es ein Portfolio zu gestalten, worin am Anfang vom Semester die Module und die entsprechenden Credits eingegeben werden können und  angezeigt wird, wie viel Aufwand jedes Modul verursacht. W�hrend dem Semester sollen Lerneinträge, wie Vorlesungen, Zusammenfassungen, Nachbearbeitung usw. erfasst werden. Die verbliebene Lernzeit soll in einer Übersicht jederzeit angezeigt werden, damit man die Wochenplanung besser vornehmen kann. Am Ende des Semesters bestetht die Möglichkeit die Modulnato einzutragen und so ein persönliches Fazit zu ziehen. 

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


