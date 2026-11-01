import random

opnieuw1 = "ja"
while opnieuw1 =="ja" :
    moeilijkheid = int(input("Hoe moeilijk wil je het? (1,2 of 3) "))

    if moeilijkheid == 1 :
        maximum = 10
        print("kies een getal van 1 tot 10")
    elif moeilijkheid == 2 :
        maximum = 50
        print("kies een getal van 1 tot 50")
    elif moeilijkheid == 3 :
        maximum = 100
        print("kies een getal van 1 tot 100")
    else :
        print("Ongeldige keuze")
        exit()

    getal1 = random.randint(1,maximum)

    getal2 = int(input("Kies een getal:"))

    pogingen = 1

    if getal2 == getal1 :
        print("Juist!")
    else:
        print(f"Fout!")

    while getal2 != getal1:
        if getal2 > getal1:
            print("Te groot")
        elif getal2 < getal1:
            print("Te klein")

        getal2 = int(input("Probeer opnieuw: "))

        pogingen = pogingen + 1
    print(f"Je hebt het getal geraden in {pogingen} pogingen")

    opnieuw1 = input("Wil je opnieuw? (ja/nee)")
print("Bedankt om te spelen!")
