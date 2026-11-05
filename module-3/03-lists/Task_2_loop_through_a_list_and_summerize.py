# ============================================================
# UPPGIFT 12: LOOPA GENOM EN LISTA OCH SUMMERA
# Modul: 3 | Svårighetsgrad: ⭐⭐ (2/10)
# Krav:
# 1. Skapa en lista med namnet "siffror" som innehåller: 10, 20, 30, 40, 50
# 2. Skapa en variabel "summa" som börjar på 0
# 3. Använd en for-loop för att loopa genom listan
# 4. Lägg till varje tal i summan
# 5. Skriv ut summan
# 6. Skriv ut listans längd med len()
# 7. Kommentera koden med # för att förklara vad varje rad gör
# ============================================================

# === STEG 1: SKAPA LISTAN ===
siffror = [10, 20, 30, 40, 50] # Skapar en lista med namnet siffror som innehåller talen 10, 20, 30, 40



# === STEG 2: SKAPA SUMMAN ===
summa = 0 # Skapar en variabel summa som börjar på 0



# === STEG 3: LOOPA OCH SUMMERA ===
for tal in siffror: # Loopar genom varje tal i listan siffror
    summa += tal # Lägger till talet i summan


# === STEG 4: SKRIV UT SUMMAN OCH LÄNGDEN ===
print (len(siffror)) # Skriver ut längden av listan siffror
print (summa) # Skriver ut summan av alla tal i listan siffror