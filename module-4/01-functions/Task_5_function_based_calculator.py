# ============================================================
# UPPGIFT 44: FUNKTIONSBASERAD MINIRÄKNARE
# Modul: 4 | Svårighetsgrad: ⭐⭐⭐⭐⭐ (5/10)
# Krav:
# 1. Skapa en funktion "addera(a, b)" som returnerar a + b.
# 2. Skapa en funktion "subtrahera(a, b)" som returnerar a - b.
# 3. Skapa en funktion "multiplicera(a, b)" som returnerar a * b.
# 4. Skapa en funktion "dividera(a, b)" som returnerar a / b.
#    (Tips: Lägg till en kontroll med if för att undvika division med noll!).
# 5. Skapa ett huvudprogram (utanför funktionerna) som:
#    - Frågar användaren om två tal (flyttal).
#    - Frågar användaren vilken operation de vill utföra (+, -, *, /).
#    - Använder en if-elif-else-sats för att anropa rätt funktion baserat på valet.
#    - Skriver ut resultatet.
# 6. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1-4: SKAPA FUNKTIONERNA ===



# FÖRSTA FUNKTION: ADDERA

def addera(a, b):
    return a + b


# ANDRA FUNKTION: SUBTRAHERA

def subtrahera(a, b): 
    return a - b


# TREDJE FUNKTION: MULTIPLICERA

def multiplicera(a, b):
    return a * b


# FJÄRDE FUNKTION: DIVIDERA
# if-sats för att kontrollera att b inte är noll för att förhindra division med noll.

def dividera(a, b):
    if b == 0:
        return "Divisjon med noll är inte tillåtet!"
    return a / b





# === STEG 5: HUVUDPROGRAMMET ===



# Två input som frågar användare att ange två flyttala och en operation (+, -, *, /). 

tal_1 = float(input("Ange det första flyttalet: "))
tal_2 = float(input("Ange det andra flyttalet: "))
operation = input("Vilken operation vill du utföra? (+, -, *, /): ")



# if-elif-else sats. Om operationen är +, -, *, eller /, anropar den respektive funktion och skriver ut resultatet. Om operationen är annat, skriver den "Ogiltig operation!" och avslutar programmet. 

if operation == "+":
    resultat = addera(tal_1, tal_2)
elif operation == "-":
    resultat = subtrahera(tal_1, tal_2)
elif operation == "*":
    resultat = multiplicera(tal_1, tal_2)
elif operation == "/":
    resultat = dividera(tal_1, tal_2)
else:
    print("Ogiltig operation!")
print("Resultatet är:", resultat)