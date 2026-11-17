# ============================================================
# UPPGIFT 64: SÖKA OCH BYGGA UPP EN DICTIONARY
# Modul: 4 | Svårighetsgrad: ⭐⭐⭐⭐ (4/10)
# Krav:
# 1. Skapa en dictionary "lager" med följande par:
#    - "äpple": 10
#    - "banan": 5
# 2. Fråga användaren vilken frukt de vill söka efter (t.ex. "äpple", "päron").
# 3. Använd en if-sats och operatorn "in" för att kontrollera om frukten finns i dictionaryn.
# 4. Om den finns: Skriv ut hur många som finns i lager.
# 5. Om den inte finns: Skriv ut "Frukten finns inte i lagret." och lägg till den automatiskt med värdet 0.
# 6. Skriv ut hela dictionaryn för att se resultatet.
# 7. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SKAPA DICTIONARYN ===

lager = {"äpple": 10, "banan": 5}


# === STEG 2 & 3: FRÅGA OCH SÖK ===

vilken_frukt = input("Vilken frukt vill du söka efter? ").swapcase()


# === STEG 4 & 5: HANTERA RESULTATET ===

if vilken_frukt in lager: 

# kontrollerar om frukten finns i dictionaryn
# in letar efter nycklar i dictionaryn. Om frukt finns som nyckel, returneras True.
# Varför in är viktigt
# Om du försöker hämta ett värde med lager["päron"] innan det finns, 
# kraschar programmet (KeyError). Genom att först kolla if "päron" in lager: undviker du kraschen.

    print(f"Antal av {vilken_frukt} i lager: {lager[vilken_frukt]}")
else:
    print(f"Frukten finns inte i lagret.")
    lager[vilken_frukt] = 0


# === STEG 6: SKRIV UT RESULTATET ===

print("Uppdaterad lager: ", lager) # skriver ut uppdaterad dictionaryn
