# ============================================================
# UPPGIFT 34: BEHÖRIGHETSSYSTEM MED BITMASKER
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐⭐ (4/10)
# Krav:
# 1. Skapa följande konstanter/ stora bokstäver (bitmasker):
#    LÄSA = 1     (binärt: 001)
#    SKRIVA = 2   (binärt: 010)
#    EXEKVERA = 4 (binärt: 100)
# 2. Skapa en variabel "behörigheter" som börjar på 0 (inga rättigheter).
# 3. Använd bitvis OR (|) för att ge användaren LÄSA och SKRIVA rättigheter.
#    Skriv ut behörigheterna i binärt format med bin().
# 4. Använd bitvis AND (&) för att kontrollera om användaren har LÄSA-rättigheter.
#    Skriv ut "Du har LÄSA-rättigheter." om det är sant.
# 5. Använd bitvis AND (&) för att kontrollera om användaren har EXEKVERA-rättigheter.
#    Skriv ut "Du har EXEKVERA-rättigheter." om det är sant.
# 6. Ta bort SKRIVA-rättigheterna genom att använda bitvis AND (&) med den inverterade masken (~SKRIVA).
#    Skriv ut de nya behörigheterna i binärt format.
# 7. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SKAPA BITMASKERNA ===

# Skapa masken för LÄSA, SKRIVA och EXEKVERA

LÄSA = 1

SKRIVA = 2

EXEKVERA = 4


# === STEG 2: SKAPA BEHÖRIGHETER ===

behörigheter = 0 # skapar en användare som har inga rättigheter


# === STEG 3: GE LÄSA OCH SKRIVA ===

behörigheter = behörigheter | LÄSA | SKRIVA # skapar en användare som har LÄSA och SKRIVA rättigheter
print(f"Du har LÄSA-rättigheter: {bin(behörigheter)}") # Skriver ut behörigheterna i binärt format



# === STEG 4 & 5: KONTROLLERA RÄTTIGHETER ===


# Kontrollera om du har LÄSA-rättigheter, SKRIVA-rättigheter och EXEKVERA-rättigheter, med att jämföra behörigheter med de rättigheter (SKRIVA, LÄSA, EXEKVERA) som du har

if behörigheter & SKRIVA:
    print("Du har SKRIVA-rättigheter")

if behörigheter & EXEKVERA:
    print("Du har LÄSA-rättigheter")
else:
    print("Du har INTE EXEKVERA-rättigheter")



# === STEG 6: TA BORT SKRIVA ===

# Inverterar behörigheter (spegelvänder på bitarna/ de binära talen) med bitvis NOT (~) och sätter den till 0 (0000)

behörigheter = behörigheter & ~SKRIVA
print(f"Du har LÄSA-rättigheter: {bin(behörigheter)}")
