# ============================================================
# UPPGIFT 18: GISSA TALET MED RÄKNARE
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐ (3/10)
# Krav:
# 1. Sätt ett hemligt tal till 7 (hemligt_tal = 7).
# 2. Skapa en variabel "gissning" som börjar på 0.
# 3. Skapa en variabel "försök" som börjar på 0 (för att räkna antalet gissningar).
# 4. Använd en while-loop som fortsätter så länge "gissning" inte är lika med "hemligt_tal".
# 5. Inuti loopen: 
#    - Öka "försök" med 1 (försök += 1).
#    - Fråga användaren att gissa ett tal.
#    - Om gissningen är fel, skriv ut "Fel gissning, försök igen!".
# 6. När loopen är slut, skriv ut "Grattis! Du gissade rätt på X försök." (där X är antalet försök).
# 7. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SÄTT STARTVÄRDEN ===
gissning = 0 # En variabel för att hålla koll på gissningen
hemligt_tal = 7 # Hemligt tal som användaren ska gissa 
försök = 0 # En variabel för att hålla koll på antalet försök


# === STEG 2: WHILE-LOOP MED RÄKNARE ===
while gissning != hemligt_tal: # While-loop som fortsätter så länge gissningen inte är lika med hemligt_tal
    gissning = int(input("Gissa ett tal från 0-10: ")) # Använd input-funktionen för att få input från användaren och konvertera det till en int
    försök += 1 # Lägg till 1 till försök varje gång while-loop körs

    if gissning != hemligt_tal: # Om gissningen inte är rätt, skriv ut fel meddelande och öka försök
        print("Fel gissning, försök igen!") # Skriv ut fel meddelande



# === STEG 3: SKRIV UT RESULTATET ===
print(f"Grattis! Du gissade rätt på talet efter försök {försök}")