# ============================================================
# UPPGIFT 37: SKRIV UT EN 2D-LISTA MED NÄSTLADE LOOPAR
# Modul: 3 | Svårighetsgrad: ⭐⭐ (2/10)
# Krav:
# 1. Skapa en nästlad lista "matris" = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 2. Använd en yttre for-loop för att loopa genom raderna (row).
# 3. Använd en inre for-loop för att loopa genom kolumnerna (col) i varje rad.
# 4. Skriv ut varje element på samma rad, separerade med mellanslag.
#    (Tips: Använd print(element, end=" ") i den inre loopen).
# 5. Efter den inre loopen (men inuti den yttre), gör en tom print() för att byta rad.
# 6. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SKAPA MATRISEN ===
matris = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]



# === STEG 2-5: NÄSTLADE LOOPAR ===

for row in matris: # Loopar genom raderna, row blir först [1, 2, 3], sedan [4, 5, 6], sedan [7, 8, 9]
    for col in row: # Loopar genom kolumnerna i varje rad
        
        # col blir 1, 2, 3 (första varvet)
        # col blir 4, 5, 6 (andra varvet)
        # col blir 7, 8, 9 (tredje varvet)


        print(col, end=" ") # Skriver ut elementet på samma rad, separerade med mellanslag
    print() # Skriver ut en tom rad efter att alla element i raden har skrivits ut