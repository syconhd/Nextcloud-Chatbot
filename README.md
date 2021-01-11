# Nextcloud Chatbot
Mit diesem bot könnt ihr automatisch Nachrichten via Nextcloud verschicken.

Installiert dazu Python 3.
Öffnet eure Kommandozeile und gebt folgende Befehle ein:

$ pip3 install selenium <br>
$ pip3 install webdriver_manager<br>

(Beim Windows das "$" einfach weglassen)

Nun öffnet ihr die nccbot.py Datei mit einem Texteditor und gebt euren Usernamen, Passwort, Nachricht und Sendezeit für die Nextcloud ein.
Zusätzlich müsst Ihr die Chat URL für den jeweiligen Tag abgeben. Dieser Bot läuft lokal auf eurem Rechner, dieser muss demnach an bleiben.

Anschließend führt ihr folgende Befehle in eure Komamandozeile aus:

$ cd [Hier das Verzeichnis in dem ihr die Python Datei gespeichert habt] <br>
$ python3 nccbot.py

(Beim Windows das "$" einfach weglassen)

Diese Befehle kopiert in die nccbot.bat Datei um diese immer ausführen zu können.
