# ============================================================
# UPPGIFT 24: BUBBLE SORT – FALLANDE ORDNING
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐⭐ (4/10)
# Krav:
# 1. Skapa en lista med namnet "siffror" som innehåller: [8, 10, 6, 2, 4]
# 2. Skriv ut listan före sortering.
# 3. Använd Bubble Sort (while-loop + for-loop) för att sortera listan.
# 4. VIKTIGT: Ändra jämförelsen så att listan sorteras i FALLANDE ordning (största talet först).
#    (Tips: Ändra > till < i if-satsen).
# 5. Skriv ut den färdigsorterade listan.
# 6. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SKAPA LISTAN ===
siffror = [8, 10, 6, 2, 4]



# === STEG 2: SKRIV UT FÖRE SORTERING ===
print("Före sortering", siffror)



# === STEG 3: BUBBLE SORT (FALLANDE) ===
swapped = True # 1. Skapa en variabel "swapped" och sätt den till True. Sätts till True eftersom det finns minst ett tal som måste bytas om det är större än nästa tal. While-loopen körs bara om villkoret är True.
while swapped: # 2. Skapa en while-loop som kör så länge "swapped" är True.
    swapped = False # 3. Sätt "swapped" till False för att förhindra att while-loopen kör igen om det inte finns fler tal att byta om det är större än nästa tal.
    for i in range(len(siffror) - 1): # 4. Använd en for-loop för att jämföra och byta om det är större än nästa tal. -1 används för att hindra att det går utanför listan och för att undvika out-of-bounds error. 
        if siffror[i] < siffror[1 + i]: # 5. Om det mindre talet är större än det större talet, byt dem om (spegelvänd).
            siffror[i], siffror[1 + i] = siffror[1 + i], siffror[i] # 6. Spegelvänder på det mindre talet och det större talet.
            swapped = True # 7. Sätt "swapped" till True för att indikera att det har blivit bytt om.



# === STEG 4: SKRIV UT EFTER SORTERING ===
print("Efter sortering", siffror)