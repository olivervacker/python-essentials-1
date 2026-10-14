# UPPGIFT 2: VÄDERPROGNOSEN – DEL 2
# Modul: 3 | Svårighetsgrad: ⭐⭐ (2/10)
# Krav:
# 1. Fråga användaren om temperaturen utomhus
# 2. Konvertera svaret till ett decimaltal (float)
# 3. Använd en if-else-sats för att kolla temperaturen
# 4. Om temperaturen är över 20 → skriv ut "Det är varmt ute!"
# 5. Om temperaturen är 20 eller lägre → skriv ut "Det är kallt ute!"
# 6. Kommentera koden med # för att förklara vad varje rad gör

# === STEG 1: FRÅGA ANVÄNDAREN OM TEMPERATUREN ===

# input() funbktionen input läser användarens svar som en sträng (input ger alltid en sträng).
# float() funktionen float konverterar strängen till ett decimaltal.
# : avslutar en rad kod. Det är inte nödvändigt men det är bra att ha det för att göra koden mer läsbar.

temperatur = float(input("Hur många grader är det utomhus? "))  # Användarfunktion. Konvertera svaret till float för att hantera temperaturer med decimaler.

# === STEG 2: KOLLA TEMPERATUREN MED IF-ELSE ===
if temperatur > 20: # En villkorsats. Om temperaturen är större än 20, körs koden under.
        print("Det är varmt ute") # Skriv ut meddelande om det är varmt.

# === STEG 3: SKRIV UT RÄTT MEDDELANDE ===
else: # En if-else sats. Om temperaturen inte är större än 20, körs koden under.
        print("Det är kallt ute") # Skriv ut meddelande om det är kallt.