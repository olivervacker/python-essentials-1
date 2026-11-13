# ============================================================
# UPPGIFT 42: FUNKTIONER MED LISTOR OCH BOOLEANS
# Modul: 4 | Svårighetsgrad: ⭐⭐⭐ (3/10)
# Krav:
# 1. Skapa en funktion "hitta_storsta" som tar en lista som parameter (lista).
# 2. Inuti funktionen: Returnera det största talet i listan.
#    (Tips: Anta att det första talet är störst och loopa igenom listan).
# 3. Skapa en lista "siffror" = [10, 5, 20, 8, 15].
# 4. Anropa funktionen med listan och skriv ut resultatet.
# 5. Skapa en funktion "ar_jamnt" som tar ett tal som parameter (tal).
# 6. Inuti funktionen: Returnera True om talet är jämnt, annars False.
# 7. Använd funktionen i en if-sats för att kolla om 10 är jämnt.
# 8. Skriv ut "10 är jämnt!" om det är sant.
# 9. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1 & 2: FUNKTIONEN HITTA_STORSTA ===

# FÖRSTA FUNKTIONEN SKAPAD

def hitta_storsta(lista): # skapar en funktion som heter "hitta_storsta" och tar en lista som parameter (variabel som lagrar listan)
    största = lista[0] # Anta att "första talet" är störst
    for num in lista:
        if num > största:
            största = num
    return största # Returnera det största talet i listan


# === STEG 3 & 4: TESTA FUNKTIONEN ===

siffror = [10, 5, 20, 8, 15] # skapar en lista med siffror (variabel som lagrar siffror)
resultat = hitta_storsta(siffror) # använder funktionen (som har skapats ovanför) för att hitta största talet i listan
print(f"Största talet är: {resultat}")




# === STEG 5 & 6: FUNKTIONEN AR_JAMNT ===

# ANDRA FUNKTIONEN SKAPAD

def ar_jamnt(tal): # skapar en funktion som tar ett tal som parameter. Denna funktion kontrollerar om ett tal är jämnt eller udda
    if tal % 2 == 0: # om talet är jämnt (eller jämt) 
        return True # returnera True
    else: # annars (om talet är udda)
        return False # returnera False



# === STEG 7 & 8: TESTA AR_JAMNT ===

if ar_jamnt(10): # om talet är jämnt
    print("10 är jämnt!") # skriv ut "Talet är jämnt!"
else: # annars (om talet är udda)
    print("10 är udda!") # skriv ut "Talet är udda!"