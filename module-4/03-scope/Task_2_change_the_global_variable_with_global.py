# ============================================================
# UPPGIFT 52: ÄNDRA GLOBAL VARIABEL MED "GLOBAL"
# Modul: 4 | Svårighetsgrad: ⭐⭐ (2/10)
# Krav:
# 1. Skapa en global variabel "räknare" och sätt den till 0.
# 2. Skapa en funktion "öka_räknare()".
# 3. Inuti funktionen:
#    - Använd nyckelordet "global" för att tala om att vi vill ändra den globala variabeln.
#    - Öka "räknare" med 1 (räknare += 1).
# 4. Anropa funktionen tre gånger.
# 5. Skriv ut värdet på "räknare" utanför funktionen.
# 6. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SKAPA GLOBAL VARIABEL ===

räknare = 0 



# === STEG 2 & 3: SKAPA FUNKTIONEN ===

def öka_räknare():
    global räknare # Använd nyckelordet "global" för att tala om att vi vill ändra den globala variabeln.
    räknare += 1 # Öka "räknare" med 1 (räknare += 1).


# === STEG 4: ANROPA FUNKTIONEN TRE GÅNGER ===

öka_räknare()
öka_räknare()
öka_räknare()


# === STEG 5: SKRIV UT RÄKNAREN ===

print("Räknaren är nu: ", räknare) # Skriv ut den uppdaterade "räknaren".

# Det anses ofta som "dålig praxis" att använda för många globala variabler, 
# eftersom det gör koden svårare att felsöka (vem ändrade variabeln?). 
# Men i små skript eller för att hålla koll på ett globalt tillstånd (som en räknare) är det helt okej.