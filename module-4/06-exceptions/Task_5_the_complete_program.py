# ============================================================
# UPPGIFT 70: DET KOMPLETTA PROGRAMMET (BETYGSHANTERARE)
# Modul: 4 | Svårighetsgrad: ⭐⭐⭐⭐⭐ (5/10)
# Krav:
# 1. Skapa en tom dictionary "betyg" = {}.
# 2. Skapa en while True-loop för att fråga användaren om ett namn.
# 3. Om användaren skriver "avsluta" → break.
# 4. Om användaren skriver ett namn, fråga efter deras betyg (A-F).
#    - Använd try-except för att se till att betyget är en giltig bokstav (A, B, C, D, E, F).
#    - Om betyget är giltigt: Spara i dictionaryn (betyg[namn] = betyg).
#    - Om betyget är ogiltigt: Skriv ut "Ogiltigt betyg!" (använd ValueError).
# 5. När loopen är klar: Loopa genom dictionaryn med .items() och skriv ut alla elever och deras betyg.
# 6. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================


# Hur fungerar raise?
# raise ValueError("Ogiltigt betyg") skapar ett eget fel och kastar det.
# Detta fångas direkt av except ValueError as e:.
# as e gör att vi kan skriva ut felmeddelandet (som är "Ogiltigt betyg").



# === STEG 1: SKAPA DICTIONARY ===

betyg = {}  # Skapa en tom dictionary "betyg" = {}



# === STEG 2-4: WHILE-LOOP MED FELHANTERING ===
while True:
    namn = input("Ange elvens namn (eller avsluta): ")


    if namn == "avsluta":
        break

    try:
        betyg_input = input(f"Ange betyg för {namn} (A-F): ").swapcase()

        if betyg_input not in ["A", "B", "C", "D", "E", "F"]:
            raise ValueError("Ogiltigt betyg!")
    except ValueError as e:
        print(f"Fel: {e}. Försök igen.")



# === STEG 5: SKRIV UT RESULTATET ===

print( "Alla elever och deras betyg: ")
for elev, betyg_i_dict in betyg.items():
    print(f"{elev}: {betyg_i_dict}")