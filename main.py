
import json
import os

if os.path.exists("aufgaben.json"):
    with open("aufgaben.json", "r", encoding="utf-8") as datei:
        aufgaben = json.load(datei)
else:
    aufgaben = []

while True:
    print("==== TASKFLOW ====")

    print("1. Aufgabe hinzufügen")
    print("2. Aufgaben anzeigen")
    print("3. Aufgaben erledigen")
    print("4. beenden")
    print()

    auswahl = input("Wähle eine Option: ")

    if auswahl == "1":
        aufgaben.append(input("Aufgabe hinzufügen: "))
        with open("aufgaben.json", "w", encoding="utf-8") as datei:
            json.dump(aufgaben, datei, ensure_ascii=False, indent=4)

    elif auswahl == "2":
        for nummer, aufgabe in enumerate(aufgaben, start=1):
            print(f"{nummer}.{aufgabe}")

    elif auswahl == "3":
        try:
            nummer = int(input("Welche Aufgabe möchtest du erledigen? "))
        except ValueError:
            print("Bitte gib eine gültige Zahl ein!")
            continue
        if nummer < 1 or nummer > len(aufgaben):
            print("Diese Aufgabe existiert nicht!")
            continue

        if aufgaben[nummer - 1].startswith("[ERLEDIGT]"):
            print("Diese Aufgabe ist bereits erledigt!")
            continue

        aufgaben[nummer - 1] = "[ERLEDIGT] " + aufgaben[nummer - 1]
        with open("aufgaben.json", "w", encoding="utf-8") as datei:
            json.dump(aufgaben, datei, ensure_ascii=False, indent=4)
        print("Aufgabe erfolgreich erledigt!")



    elif auswahl == "4":
        print("TaskFlow beendet!")
        break

    else:
        print("Ungültige Auswahl!")