# ============================================================
# UPPGIFT 20: SUMMERA TAL TILLS ANVÄNDAREN SKRIVER 0
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐⭐⭐ (5/10)
# Krav:
# 1. Skapa en variabel "summa" som börjar på 0.
# 2. Använd en while True-loop för att läsa in tal från användaren.
# 3. Om användaren skriver 0 → avsluta loopen med break.
# 4. Om användaren skriver ett negativt tal → skriv ut "Negativa tal ignoreras." och använd continue för att hoppa över resten av varvet.
# 5. Om användaren skriver ett positivt tal → lägg till talet i summan.
# 6. När loopen är klar, skriv ut summan av alla positiva tal.
# 7. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SKAPA SUMMAN ===

summa = 0


# === STEG 2: WHILE TRUE-LOOP MED BREAK OCH CONTINUE ===

while True:
    tal = int(input("Skriv ett tal (0 för att avsluta): "))
    if tal == 0:
        break
    elif tal < 0:
        print("Negativa tal ignoreras.")
        continue
    else:
        summa += tal


# === STEG 3: SKRIV UT SUMMAN ===
print(f"summan av alla positiva tal är: {summa}")