# coronafaktencheck.ai
Das Projekt coronafaktencheck kontrolliert aktuelle News zu Coronavirus (COVID-19), und evaluiert, ob diese Fake oder Richtig sind. Dies tut es durch einen Abgleich mit bestätigten Quellen und Hilfe des auf Neuronalen Netzen basierte Modell Bert. Dieses Modell ist das aktuelle State Of The Art, der Verabrietung von fast allen Aufgaben der natürlichen Sprachverarbeitung (Natural Language Processing, kurz NLP). Im Frontend des Projekts kann ein News Link (aktuell ein Twitter Tweet Link), in ein Eingabefeld gepostet werden. Durch die eingebaute Künstliche Intelligenz wird im Hintergrund die Wahrscheinlichkeit einer Fake News evaluiert. Im Ausgabebildschirm des Projekts erscheint eine Grafik, die dem User der Anwendung wiedergibt, zu wie viel Prozent es sich um eine richtige oder fake Nachrcht handelt. Außerdem eingeblendet wird, ob das Modell es bei einer Nachricht nicht einschätzen kann, ob diese richtig oder fake ist.
Auf der Hauptseite sieht man unterhalb des Eingabesfeldes eine Karte, welche die aktuelle Verbreitung von Fake News in Deutschland zeigt. Ein sogenanntes "Mein Nachbar hat aber gesagt..." kann dadurch gut erkannt und eingedämmt werden. Wenn man mit der Maus über einen Datenpunkt auf der Karte geht, sieht man ein Popup Window, welches eine kurze Zusammenfassung der Fake Nachricht und die zugehörige Konfidenz, dass es sich um eine Fake Nachricht handelt, anzeigt.

## Schaue dir das Projekt auf CodeSandbox an: [HIER](https://codesandbox.io/embed/github/Social-Developers-Club/coronafaktencheckai-frontend/tree/master/coronafaktencheck?fontsize=14&hidenavigation=1&theme=dark&view=preview)
...und poste den folgenden Link in das Eingabefeld: https://twitter.com/linuscodes/status/1241804756147986432 (Beispiel für Prototypen)
