# ============================================================
# UPPGIFT 38: SKAPA EN 2D-LISTA MED LIST COMPREHENSION
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐ (3/10)
# Krav:
# 1. Skapa en 2D-lista (en matris) med namnet "matris" som är 3x3 (3 rader, 3 kolumner).
# 2. Använd en NÄSTLAD List Comprehension för att fylla matrisen med nollor (0).
#    (Tips: [[0 for j in range(3)] for i in range(3)])
# 3. Skriv ut matrisen för att se resultatet.
# 4. Skapa en ny 2D-lista "multiplikationstabell" som är 3x3.
# 5. Använd en nästlad List Comprehension för att fylla den med värdet (i * j).
#    (Där i är radnummer 0-2 och j är kolumnnummer 0-2).
# 6. Skriv ut multiplikationstabellen.
# 7. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1 & 2: SKAPA EN 3x3 MATRIS MED NOLLOR ===

matris = [[0 for j in range(3)] for i in range(3)] # Skapar en 3x3 matris (en yttre list och en inre lista) med bara nollor




# === STEG 3: SKRIV UT MATRISEN ===

print(matris) # Skriver ut elementet



# === STEG 4 & 5: SKAPA MULTIPLIKATIONSTABELL ===

multiplikationstabell = [[i * j for j in range(3)] for i in range(3)] 


# === STEG 6: SKRIV UT MULTIPLIKATIONSTABELLEN ===

print(multiplikationstabell) # Skriver ut elementet