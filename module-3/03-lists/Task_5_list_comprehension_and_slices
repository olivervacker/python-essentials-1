# ============================================================
# UPPGIFT 15: LIST COMPREHENSION OCH SLICES
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐⭐⭐ (5/10)
# Krav:
# 1. Skapa en lista med namnet "tal" som innehåller talen 1 till 10.
# 2. Använd en List Comprehension för att skapa en NY lista "kvadrater" som innehåller kvadraten på alla tal i "tal".
# 3. Använd en List Comprehension för att skapa en NY lista "jämna_tal" som bara innehåller de jämna talen från "tal".
# 4. Skriv ut "kvadrater" och "jämna_tal".
# 5. Använd en slice för att skriva ut de 3 första elementen från "kvadrater".
# 6. Använd en slice för att skriva ut de 3 sista elementen från "tal".
# 7. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SKAPA LISTAN (1-10) ===
# Tips: Använd list(range(1, 11)) eller skriv ut alla tal manuellt.
tal = list(range(1, 11))  # Skapar en lista med talen 1 till 10. Exkluderar 11 eftersom range inte inkluderar det sista talet.
print("Lista med tal:", tal)  # Skriver ut listan med talen


# === STEG 2: SKAPA KVADRATER MED LIST COMPREHENSION ===
kvadrater = [x ** 2 for x in tal]  # Skapar en ny lista där varje tal i "tal" upphöjs till kvadrat.
print("Kvadrater:", kvadrater)  # Skriver ut listan med kvadrater som skapades ovan.

# === STEG 3: SKAPA JÄMNA TAL MED LIST COMPREHENSION ===
jämna_tal = [x for x in tal if x % 2 == 0]  # Skapar en ny lista med endast jämna tal från "tal".



# === STEG 4: SKRIV UT LISTORNA ===
print("Kvadrater:", kvadrater)  # Skriver ut listan med kvadrater.
print("jämna_tal", jämna_tal) # Skriver ut listan med jämna tal



# === STEG 5 & 6: ANVÄND SLICES ===
första_tre_kvadrater = kvadrater[:3] # Tar de första tre elementen från "kvadrater" och sparar dem i en ny lista. 
print("3 första kvadrater", första_tre_kvadrater) 

första_tre_jämna_tal = jämna_tal[:3]
print("3 första jämna_tal", första_tre_jämna_tal)

sista_tre_tal = tal[-3:]
print("3 sista tal", sista_tre_tal)