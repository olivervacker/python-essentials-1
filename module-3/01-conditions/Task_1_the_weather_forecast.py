# UPPGIFT 1: VÄDERPROGNOSEN
# Modul: 3 | Svårighetsgrad: ⭐ (1/10)
# Krav:
# 1. Fråga användaren om temperaturen utomhus
# 2. Konvertera svaret till ett decimaltal (float)
# 3. Använd en if-sats för att kolla om temperaturen är över 20
# 4. Skriv ut "Det är varmt ute!" endast om villkoret är sant
# 5. Kommentera koden med # för att förklara vad varje rad gör


# === STEG 1: FRÅGA ANVÄNDAREN OM TEMPERATUREN ===
temperatur = float(input("Vad är temperaturen utomhus? "))  # Frågar användaren om temperaturen och konverterar svaret till ett decimaltal
if temperatur > 20:  # Kontrollerar om temperaturen är över 20 grader
# input() funbktionen input läser användarens svar som en sträng (input ger alltid en sträng)
# float() funktionen float konverterar strängen till ett decimaltal
# variabeln temperatur lagrar det inmatade värdet

# === STEG 2: KOLLA OM TEMPERATUREN ÄR ÖVER 20 === 
    print("Det är varmt ute!")  # Skriver ut meddelandet om temper turen är över 20 grader

# === STEG 3: PROGRAMMET AVSLUTAS ===
# Om temperaturen är 20 eller lägre → inget skrivs ut 