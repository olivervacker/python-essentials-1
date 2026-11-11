# ============================================================
# UPPGIFT 21: BUBBLE SORT – ETT PASS
# Modul: 3 | Svårighetsgrad: ⭐ (1/10)
# Krav:
# 1. Skapa en lista med namnet "siffror" som innehåller: [8, 10, 6, 2, 4]
# 2. Skriv ut listan före sortering.
# 3. Använd en for-loop för att jämföra intilliggande element (i och i+1).
# 4. Om det vänstra elementet är större än det högra → byt plats på dem.
# 5. Skriv ut listan efter att loopen har kört ett pass.
# 6. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================


# === STEG 1: SKAPA LISTAN ===

siffror = [8, 10, 6, 2, 4]

# === STEG 2: SKRIV UT FÖRE SORTERING ===
print("Före:", siffror)

# === STEG 3: ETT PASS MED FOR-LOOP ===

# Vi loopar igenom listan och jämför intilliggande element
for i in range(len(siffror) - 1):

    # Om det vänstra elementet är större än det högra -> byt plats
    if siffror[i] > siffror[i + 1]:

        # Byt plats med Pythons smarta swap
        siffror[i], siffror[i + 1] = siffror[i + 1], siffror[i]

# === STEG 4: SKRIV UT EFTER ETT PASS ===
print("Efter ett pass:", siffror)


