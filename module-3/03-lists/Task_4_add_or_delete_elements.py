# ============================================================
# UPPGIFT 14: SÄTT IN OCH TA BORT ELEMENT
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐⭐ (4/10)
# Krav:
# 1. Skapa en lista med namnet "kö" som innehåller: "Anna", "Erik", "Sofia"
# 2. Skriv ut listan
# 3. Använd insert() för att sätta in "Johan" på plats 1 (mellan Anna och Erik)
# 4. Skriv ut listan igen
# 5. Använd del för att ta bort den första personen i kön (Anna)
# 6. Skriv ut listan igen
# 7. Använd pop() för att ta bort den sista personen i kön
# 8. Skriv ut listan igen
# 9. Kommentera koden med # för att förklara vad varje rad gör
# ============================================================

# === STEG 1: SKAPA LISTAN ===
kö = ["Anna", "Erik", "Sofia"]  # Skapar en lista med namnen Anna, Erik och Sofia.



# === STEG 2: SKRIV UT LISTAN ===
print(kö) # Skriver ut listan med namnen Anna, Erik och Sofia.



# === STEG 3: SÄTT IN "JOHAN" PÅ PLATS 1 ===
kö.insert(1, "Johan")  # Insert är en funktion som lägger till ett element på en specifik plats i listan. Här lägger vi till "Johan" på plats 1.



# === STEG 4: SKRIV UT LISTAN IGEN ===
print(kö) # Skriver ut listan med ändringarna.



# === STEG 5: TA BORT FÖRSTA PERSONEN ===
del kö[0]  #  del = delete. Tar bort "Anna" från listan. 



# === STEG 6: SKRIV UT LISTAN IGEN ===
print(kö)



# === STEG 7: TA BORT SISTA PERSONEN MED POP() ===
kö.pop(2) #  



# === STEG 8: SKRIV UT LISTAN IGEN ===
print(kö)