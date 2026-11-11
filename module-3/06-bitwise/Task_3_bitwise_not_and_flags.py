# ============================================================
# UPPGIFT 33: BITVIS NOT (~) OCH FLAGGANDE
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐ (3/10)
# Krav:
# 1. Skapa en variabel "x" = 5.
# 2. Använd bitvis NOT (~) på x. Spara resultatet i en variabel.
# 3. Skriv ut resultatet. (Vad tror du det blir? Testa dig fram!)
# 4. Skapa en variabel "flaggor" = 0b1010 (binärt för 10).
# 5. Använd bitvis OR (|) för att sätta på den första biten (lägg till 0b0001).
#    Spara i en ny variabel och skriv ut resultatet.
# 6. Använd bitvis AND (&) för att nolla den tredje biten (använd en mask).
#    Spara i en ny variabel och skriv ut resultatet.
# 7. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1 & 2 & 3: BITVIS NOT ===

x = 5 
not_x = ~x
print(f"Bitvis NOT av 5: {not_x}")


# === STEG 4: SKAPA FLAGGOR ===

flaggor = 0b1010



# === STEG 5: SÄTT PÅ EN BIT (OR) ===

nya_flaggor = flaggor | 0b0001
print(f"Efter OR: {bin(nya_flaggor)}")


# === STEG 6: NOLLA EN BIT (AND) ===

nollade_flaggor = flaggor & ~0b0100
print(f"Efter AND: {bin(nollade_flaggor)}")
