# ============================================================
# UPPGIFT 17: GISSA TALET (WHILE-LOOP)
# Modul: 3 | Svårighetsgrad: ⭐⭐ (2/10)
# Krav:
# 1. Sätt ett hemligt tal till 7 (t.ex. hemligt_tal = 7).
# 2. Skapa en variabel "gissning" som börjar på 0.
# 3. Använd en while-loop som fortsätter så länge "gissning" inte är lika med "hemligt_tal".
# 4. Inuti loopen: Fråga användaren att gissa ett tal (omvandla till heltal).
# 5. Om gissningen är fel, skriv ut "Fel gissning, försök igen!".
# 6. När loopen är slut (rätt gissning), skriv ut "Grattis, du gissade rätt!".
# 7. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SÄTT DET HEMLIGA TALET OCH STARTA GISSNINGEN ===
gissning = 0 # Sätt gissningen till 0 för att börja med en tom gissning.
hemligt_tal = 7 # Sätt hemligt_tal till 7 för att börja med ett hemligt tal.


# === STEG 2: WHILE-LOOP FÖR ATT GISSA ===
while gissning != hemligt_tal: # Låt while-loopen fortsätta så länge gissningen är olika hemligt_tal. 
    gissning = int(input("Gissa ett tal (1-10): ")) # Läs in gissningen från användaren och konvertera till heltal med int och input.

    # Om gissningen inte stämmer, skriv ut felmeddelandet och låt användaren försöka igen.
    if gissning != hemligt_tal:
        print("Fel gissning, försök igen!")

# === STEG 3: SKRIV UT GRATTISMEDDELANDET ===
print("Grattis, du gissade rätt!")

