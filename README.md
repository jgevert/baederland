# Crawler um freie Schwimmkurse zu finden

Wir hatten das Problem, dass wir keine freien Schwimmkurse beim Bädeland Hamburg finden konnten.
Immer wenn wir auf der Webseite nachschauten, waren die Kurse ausgebucht.

Aus diesem Grund habe ich dieses Crawler gebaut. Das Skript checkt auf einer Obwrseite, ob das gewünschte Schwimmbad grundsätzlich einen Schwimmkurs abnietet.
Falls dies der Fall sein sollte, wird auf der Landingpage nach freien Slots gesucht. Sollten solche Slots gefunden werden, wird eine eMail an eine definirte Empfängerliste versendet.

## Koordination des Skripts
Das Skript wird über ein ini File gesteuert. Erklärungen wurden unter config.ini.exmaple hinterlegt. Sobald die korrekten Daten hinterlegt sind, muss die Datei unter >> config.ini << hinterlegt werden.

## Weiterentwicklung des Skripts
Fühlt Euch frei dieses Skript weiterzuentwickeln.

## Starten des Skripts
Es gibt unterschiedliche Möglichkeiten das Skript zu starten. Über das Crontab ist eine des einfachsten Möglichkeiten ohne viel Overhead.
