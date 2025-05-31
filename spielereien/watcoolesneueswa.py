print("Hello World")
import os 
import subprocess
optionen = ["coolerTaschenrechner","andere Sachen"]
global letztesprogramm
def nochetwas():
    wahl = input("Willst du noch etwas machen? (j/n/e): ").lower()
    if wahl == "j":
        meunue()
    elif wahl == "n":
        print("Okay, dann bis zum nächsten Mal!")
        os.system("cls")
    elif wahl == "e":
        print("Programm wird beendet.")
        exit()
    else:
        print("Ungültige Eingabe! Bitte gib 'j', 'n' oder 'e' ein.")
        nochetwas()
def coolerTaschenrechner():
    os.system("cls")
    print("Willkommen zu Leon's cooler Taschenrechner")
    print("Hier kannst du verschiedene Rechnungen durchführen")
    print("Starte anderes Programm...")
    subprocess.run(["python", "spielereien/coolerTaschenrechner1.2.py"])
    print(f"Das was {letztesprogramm}, du bist nun zurück im Hauptmenü.")
    nochetwas()
def meunue(): 
    os.system("cls")
    print("Willkommen zu Leon's Bibliothek")
    for nummera, taska in enumerate(optionen, 1):
        print(f"{nummera}. {taska}")  
    Tasks = {
        float("1"): coolerTaschenrechner,
    }
    while True:
        operation = float(input("was soll gemacht werden?(gib die Zahl ein)"))
        if operation in Tasks:
            Tasks[operation]()
            letztesprogramm = operation
            break
        else:print(f"Bist du dumm? Gib eine von diesen ein: 1-9 Sonst tschüss...")

#start des Programms
meunue()