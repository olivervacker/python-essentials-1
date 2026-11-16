# ============================================================
# UPPGIFT 55: GLOBAL RÄKNARE I EN LOOP
# Modul: 4 | Svårighetsgrad: ⭐⭐⭐⭐⭐ (5/10)
# Krav:
# 1. Skapa en global variabel "antal_anrop" = 0.
# 2. Skapa en funktion "spara_ärende(ärende)".
#    - Inuti funktionen:
#      - Använd "global" för att öka "antal_anrop" med 1.
#      - Skriv ut "Ärende sparat: [ärende]".
# 3. Skapa en tom lista "logg" = [].
# 4. Skapa ett huvudprogram (en while-loop) som:
#    - Frågar användaren att skriva in ett ärende (text).
#    - Om användaren skriver "avsluta" → break.
#    - Annars: Anropa funktionen "spara_ärende(ärende)".
#    - Lägg till ärendet i listan "logg" (använd append).
# 5. När loopen är klar: Skriv ut "Totalt antal anrop: [antal_anrop]" och "Logg: [logg]".
# 6. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SKAPA GLOBAL VARIABEL ===
antal_anrop = 0



# === STEG 2: SKAPA FUNKTIONEN ===

def spara_ärende(ärende):
    global antal_anrop # Använd global för att ändra global variabeln "antal_anrop"
    antal_anrop += 1 # Du behöver först göra global variabeln "antal_anrop" för att kunna ändra den med 'antal_anrop += 1'
    print("Antal anrop: " + str(antal_anrop)) # Skriv ut antal anrop för att se vad som händer
    logg.append(ärende)
    print(f"Ärende sparat: {ärende}")
    
    

# === STEG 3: SKAPA LISTAN ===
logg = []



# === STEG 4: HUVUDPROGRAM (WHILE-LOOP) ===

while True: # Huvudprogram (while-loop), körs så länge True är sant
    ärende = input("Ange ett ärende (eller avsluta): ")
    if ärende == "avsluta":
        break

    spara_ärende(ärende)
    logg.append(ärende)


# === STEG 5: SKRIV UT RESULTATET ===
print(f"Total antal anrop: {antal_anrop}")
print(f"Logg: {logg}")