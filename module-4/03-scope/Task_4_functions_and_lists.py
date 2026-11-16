# ============================================================
# UPPGIFT 54: FUNKTIONER OCH LISTOR (REFERENSER)
# Modul: 4 | Svårighetsgrad: ⭐⭐⭐⭐ (4/10)
# Krav:
# 1. Skapa en lista "mina_siffror" = [1, 2, 3].
# 2. Skapa en funktion "andra_i_listan(lista)".
# 3. Inuti funktionen:
#    - Ändra det första elementet i listan till 99 (lista[0] = 99).
#    - Skriv ut listan inuti funktionen.
# 4. Anropa funktionen med "mina_siffror".
# 5. Skriv ut "mina_siffror" utanför funktionen (blev den ändrad?).
# 6. Skapa en funktion "byt_ut_hela_listan(lista)".
# 7. Inuti funktionen:
#    - Tilldela en helt ny lista: lista = [10, 20, 30].
#    - Skriv ut listan inuti funktionen.
# 8. Anropa funktionen med "mina_siffror".
# 9. Skriv ut "mina_siffror" utanför funktionen (blev den ändrad nu?).
# 10. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SKAPA LISTAN ===

mina_siffror = [1, 2, 3]

# === STEG 2 & 3: FUNKTIONEN SOM ÄNDRAR ELEMENT ===

def andra_i_listan(lista):
    lista[0] = 99 # Ändrar första elementet i listan som heter mina_siffror
    print("Inuti", lista)



# === STEG 4 & 5: ANROPA OCH TESTA ===

andra_i_listan(mina_siffror) # Skapar en referens till listan och ändrar den först elementet
print("Utanför", mina_siffror)


# === STEG 6 & 7: FUNKTIONEN SOM BYTER UT HELA LISTAN ===

def byt_ut_hela_listan(lista):
    lista = [10, 20, 30] # Ändrar listan till en ny lista
    print("Inuti", lista)


# === STEG 8 & 9: ANROPA OCH TESTA IGEN ===

byt_ut_hela_listan(mina_siffror) # Skapar en referens till listan och ändrar den först elementet
print("Utanför", mina_siffror)