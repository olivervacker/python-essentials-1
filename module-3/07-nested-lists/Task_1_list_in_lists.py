# ============================================================
# UPPGIFT 36: LISTOR I LISTOR (2D-ARRAY)
# Modul: 3 | Svårighetsgrad: ⭐ (1/10)
# Krav:
# 1. Skapa en nästlad lista (en lista i listan) som heter "matris" och ser ut så här: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 2. Skriv ut hela matrisen.
# 3. Skriv ut det första elementet i den första raden (index 0, 0) -> Ska bli 1.
# 4. Skriv ut det sista elementet i den sista raden (index -1, -1) -> Ska bli 9.
# 5. Skriv ut hela den andra raden (index 1) -> Ska bli [4, 5, 6].
# 6. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SKAPA MATRISEN ===
matris = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# === STEG 2: SKRIV UT HELA MATRISEN ===
print(matris)



# === STEG 3: SKRIV UT FÖRSTA ELEMENTET (0,0) ===
print(matris[0][0])




# === STEG 4: SKRIV UT SISTA ELEMENTET (-1,-1) ===
print(matris[-1][-1])



# === STEG 5: SKRIV UT ANDRA RADEN ===
print(matris[1])