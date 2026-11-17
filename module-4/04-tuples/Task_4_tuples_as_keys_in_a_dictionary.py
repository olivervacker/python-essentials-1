# ============================================================
# UPPGIFT 59: TUPLER SOM NYCKLAR I EN DICTIONARY
# Modul: 4 | Svårighetsgrad: ⭐⭐⭐⭐ (4/10)
# Krav:
# 1. Skapa en dictionary med namnet "bokinventering".
# 2. Använd tupler som nycklar för att lagra information om böcker. 
#    Formatet ska vara: (Titel, Författare) : Antal_i_lager.
#    Exempel: ("Sagan om ringen", "Tolkien") : 3
# 3. Lägg till två böcker:
#    - ("Python Crash Course", "Eric Matthes") : 5
#    - ("Clean Code", "Robert C. Martin") : 2
# 4. Skriv ut hela dictionaryn.
# 5. Hämta och skriv ut antalet i lager för ("Python Crash Course", "Eric Matthes").
# 6. Loopa genom dictionaryn med en for-loop och .items().
#    Skriv ut titel, författare och antal för varje bok.
# 7. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1-3: SKAPA DICTIONARY MED TUPLE-NYCKLAR ===

# Skapa en tuple som innehåller en dictionary med tupel-nycklarna

bokinventering = {("Python Crash Course", "Eric Matthes"): 5, ("Clean Code", "Robert C. Martin"): 2}



# === STEG 4: SKRIV UT HELA DICTIONARYN ===

print(bokinventering)



# === STEG 5: HÄMTA ETT SPECIFIKT VÄRDE ===

print (bokinventering[("Clean Code", "Robert C. Martin")]) # använd klammerparanteser för att hämta ett specifikt värde


# === STEG 6: LOOPA GENOM DICTIONARYN ===

for (titel, författare) in bokinventering.items(): # Items ger en tupel av både nyckeln och värdena i dictionaryn, som vi kan skriva ut med titel och författare i variabeln titel och författare respestivt. 
    print(f"Titel: {titel}, Författare: {författare}") # använd items() för att loopa genom alla tupel-nycklarna i dictionaryn


# Förutom items() så finns values() att använda för att loopa genom alla värden i dictionaryn.
# Sen finns också keys() för att loopa genom alla nycklar i dictionaryn. 


# Listor kan ändras (mutable), så Python kan inte garantera att de förblir desamma. 
# Tupler är oföränderliga (immutable), så de är "hashable" och kan användas som nycklar.

