# ============================================================
# UPPGIFT 16: RÄKNA NER MED WHILE-LOOP
# Modul: 3 | Svårighetsgrad: ⭐ (1/10)
# Krav:
# 1. Skapa en variabel "räknare" som börjar på 5.
# 2. Använd en while-loop för att skriva ut räknarens värde.
# 3. Minska räknaren med 1 för varje varv.
# 4. Loopen ska fortsätta så länge räknaren är större än 0.
# 5. När loopen är klar, skriv ut "Start!".
# 6. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SKAPA RÄKNAREN ===
räknare = 5  # Sätter räknaren till 5.

# === STEG 2: WHILE-LOOP ===
while räknare > 0:  # While-loop funktion. Fortsätter så länge räknaren är större än 0.
    print(räknare)  # Skriver ut räknarens aktuella värde.
    räknare -= 1  # Minskar räknaren med 1.

# === STEG 3: SKRIV UT MEDDELANDET EFTER LOOPEN ===
print("Start!")  # Skriver ut meddelandet när nedräkningen är klar.