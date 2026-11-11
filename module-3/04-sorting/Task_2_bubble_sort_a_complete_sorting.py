# ============================================================
# UPPGIFT 22: BUBBLE SORT – FULLSTÄNDIG SORTERING
# Modul: 3 | Svårighetsgrad: ⭐⭐ (2/10)
# Krav:
# 1. Skapa en lista med namnet "siffror" som innehåller: [8, 10, 6, 2, 4]
# 2. Skriv ut listan före sortering.
# 3. Skapa en variabel "swapped" och sätt den till True.
# 4. Använd en while-loop som fortsätter så länge "swapped" är True.
# 5. Inuti while-loopen: 
#    - Sätt "swapped" till False (vi antar att inga byten sker).
#    - Använd en for-loop för att jämföra intilliggande element (i och i+1).
#    - Om det vänstra elementet är större än det högra → byt plats och sätt "swapped" till True.
# 6. Skriv ut listan efter att while-loopen är klar (listan ska nu vara helt sorterad).
# 7. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SKAPA LISTAN ===
siffror = [8, 10, 6, 2, 4]


# === STEG 2: SKRIV UT FÖRE SORTERING ===
print(siffror)



# === STEG 3: WHILE-LOOP FÖR ATT SORTERA ===
swapped = True
while swapped:
    swapped = False

    for i in range(len(siffror) - 1):
            if siffror[i] > siffror[i + 1]:
                swapped = True
                siffror[i], siffror[i + 1] = siffror[i + 1], siffror[i]




# === STEG 4: SKRIV UT EFTER SORTERING ===
print("Efter sortering:", siffror)