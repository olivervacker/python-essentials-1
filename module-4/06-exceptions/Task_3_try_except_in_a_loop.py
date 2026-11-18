# ============================================================
# UPPGIFT 68: TRY-EXCEPT I EN LOOP (FÖRSÖK IGEN)
# Modul: 4 | Svårighetsgrad: ⭐⭐⭐ (3/10)
# Krav:
# 1. Skapa en while True-loop.
# 2. Inuti loopen:
#    - Använd ett try-except-block.
#    - Inuti try: Fråga användaren om deras ålder (int).
#    - Om det lyckas: Skriv ut "Din ålder är [ålder] år." och använd break för att avsluta loopen.
#    - Inuti except ValueError: Skriv ut "Fel: Ange ett heltal, försök igen!".
# 3. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1-2: WHILE-LOOP MED TRY-EXCEPT ===

while True:
    try:
        # Fråga användaren om deras ålder
        ålder = int(input("Ange din ålder: "))
        if ålder >= 0:
            print(f"Din ålder är: {ålder} år.")
            break  # Avsluta loopen om det lyckas, annars börjar loopen om och man får ange åldern på nytt igen.
    except ValueError:
        # Om det lyckas inte: Skriv ut felmeddelande och fortsätt loopen
        print("Fel: Ange ett heltal, försök igen!")