# UPPGIFT 3: VÄDERPROGNOSEN – DEL 3
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐ (3/10)
# Krav:
# 1. Fråga användaren om temperaturen utomhus
# 2. Konvertera svaret till ett decimaltal (float)
# 3. Använd en if-elif-else-sats för att kolla temperaturen
# 4. Om temperaturen är över 25 → skriv ut "Det är mycket varmt ute!"
# 5. Om temperaturen är mellan 15 och 25 → skriv ut "Det är lagom varmt ute!"
# 6. Om temperaturen är under 15 → skriv ut "Det är kallt ute!"
# 7. Kommentera koden med # för att förklara vad varje rad gör

# === STEG 1: FRÅGA ANVÄNDAREN OM TEMPERATUREN ===
temperatur = float(input("Vad är temperaturen utomhus? "))  # En användarfunktion. Frågar användaren om temperaturen och konverterar svaret till ett decimaltal.
# input() funbktionen input läser användarens svar som en sträng (input ger alltid en sträng).
# float() funktionen float konverterar strängen till ett decimaltal som sedan lagras i variabeln temperatur.
# if-elif-else satsen används för att kontrollera olika villkor och utföra olika åtgärder baserat på vilka villkor som är sanna.

if temperatur > 25: # Villkortsats som är 'if' och efter det är villkoret som ska kontrolleras. Kontrollerar om temperaturen är över 25 grader.
    print("Det är mycket varmt ute!") # Om villkoret är sant, skriv ut "Det är väldigt varmt ute!"
    # print() funktionen print skriver ut texten i terminalen.

# === STEG 2: KOLLA TEMPERATUREN MED IF-ELIF-ELSE ===

elif temperatur > 20: # En if-elif-else sats. Kontrollerar om temperaturen är över 20 grader (elif är förkortning av else if, det är samma som att skriva else if).
    print("Det är varmt ute!") # Om villkoret är sant, skriv ut "Det är varmt ute!"

    # elif används för att kontrollera flera villkor. Om det första villkoret inte är sant, går programmet vidare till nästa elif.


# === STEG 3: SKRIV UT RÄTT MEDDELANDE ===

elif temperatur >= 15: # >= som betyder större än eller lika med. Kontrollerar om temperaturen är över 15 grader men inte över 20 grader.
    print("Det är lagom varmt ute!") # Om villkoret är sant, skriv ut "Det är lite varmt ute!"

else:
    temperatur < 15 # Om ingen av de tidigare villkoren är sanna, körs else-satsen. Det betyder att temperaturen är 1 < 15: # Kontrollerar om temperaturen är över 15 grader.
    print ("Det är kallt ute!") # Om villkoret är sant, skriv ut "Det är lite kallt ute!"










