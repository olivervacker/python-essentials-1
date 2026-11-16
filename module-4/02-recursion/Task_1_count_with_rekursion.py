# ============================================================
# UPPGIFT 45: RÄKNA NER MED REKURSION
# Modul: 4 | Svårighetsgrad: ⭐ (1/10)
# Krav:
# 1. Skapa en funktion "räkna_ned(n)" som tar ett heltal (n).
# 2. Inuti funktionen:
#    - Skriv ut n.
#    - Om n är större än 0, anropa funktionen igen med (n - 1).
#    - Detta kallas för ett rekursivt anrop.
# 3. Anropa funktionen med talet 3.
# 4. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1 & 2: SKAPA FUNKTIONEN ===

def räkna_ned(n):
    # Skriv ut n
    print(n)
    # Om n är större än 0, anropa funktionen igen med (n - 1)
    if n > 0: # Detta kallas för basfall. Detta är ett villkor som stoppar rekursionen. Utan det skulle funktion anropa sig själv med negativa tal för evigt (detta kallas för oändlig rekursion) när n är 0 eller mindre.
        räkna_ned(n - 1) # Detta kallas för ett rekursivt anrop. Denna funktion anropar sig själv med ett mindre problem (t.ex. -1). n - 1 innebär att n går att minska med 1



# === STEG 3: ANROPA FUNKTIONEN ===
räkna_ned(3)  # Anropa funktionen med talet 3
