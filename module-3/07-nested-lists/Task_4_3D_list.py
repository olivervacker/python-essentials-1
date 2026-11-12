# ============================================================
# UPPGIFT 39: 3D-LISTA (HOTELLET)
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐⭐ (4/10)
# Krav:
# 1. Skapa en 3D-lista med namnet "hotell".
#    - Hotellet har 2 byggnader.
#    - Varje byggnad har 3 våningar.
#    - Varje våning har 4 rum.
# 2. Använd en NÄSTLAD List Comprehension för att skapa hotellet.
#    Alla rum ska initialt vara lediga (sätt dem till False).
#    (Tips: [[[False for r in range(4)] for f in range(3)] for b in range(2)])
# 3. Skriv ut hela hotellet.
# 4. Boka rum nummer 2 (index 1) på våning 3 (index 2) i byggnad 1 (index 0).
#    Ändra värdet till True.
# 5. Skriv ut byggnad 1 för att se ändringen.
# 6. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1 & 2: SKAPA 3D-LISTAN ===
hotell = [[[False for r in range(4)] for f in range(3)] for b in range(2)] # List comprehension lista som loopar 4 rum, 3 byggnader och 2 våningar
# r = 4 = 4 rum
# f = 3 = 3 våningar
# b = 2 = 2 byggnader



# === STEG 3: SKRIV UT HELA HOTELLET ===
print(hotell)



# === STEG 4: BOKA ETT RUM ===
hotell[0][2][1] = True # Boka rum 1 i byggnad 1, våning 2, rum 1
print(hotell) # Skriv ut hotell igen för att se ändringen




# === STEG 5: SKRIV UT BYGGNAD 1 ===
print(hotell[1]) # Skriv ut byggnad 1

