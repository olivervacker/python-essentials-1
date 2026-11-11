# ============================================================
# UPPGIFT 27: LOGISKA OPERATORER I PRAKTIKEN (ÅLDERSKONTROLL)
# Modul: 3 | Svårighetsgrad: ⭐⭐ (2/10)
# Krav:
# 1. Fråga användaren om deras ålder (heltal).
# 2. Fråga användaren om de har en bil (ja/nej).
# 3. Omvandla bil-svaret till gemener (lower()) för att hantera "Ja" och "ja".
# 4. Använd en if-sats med operatorn "and" för att kolla:
#    - Om åldern är 18 eller mer OCH användaren har en bil ("ja").
#    - Om båda är sanna, skriv ut "Du får köra bil!".
# 5. Använd en if-sats med operatorn "or" för att kolla:
#    - Om åldern är under 18 ELLER användaren inte har en bil ("nej").
#    - Om något av detta är sant, skriv ut "Du får inte köra bil.".
# 6. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1 & 2 & 3: FRÅGA ANVÄNDAREN ===

ålder = int(input("Vad är din ålder? ")) # Användarinput för ålder
bil_svar = input("Har du en bil? (skriv ja eller nej)").lower()  # Omvandlar svar till små bokstäver (gemener)



# === STEG 4: KONTROLLERA MED "AND" ===

if ålder >= 18 and bil_svar == "ja": # Om ålder är över 18 och bil_svar är "ja", skriv ut "Du får köra bil."
    print("Du får köra bil.")


# === STEG 5: KONTROLLERA MED "OR" ===

if ålder < 18 or bil_svar == "nej":
    print("Du får inte köra bil.") # Om ålder är under 18 eller bil_svar är "nej", skriv ut "Du får inte köra bil."