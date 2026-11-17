# ============================================================
# UPPGIFT 61: SKAPA OCH HÄMTA FRÅN EN DICTIONARY
# Modul: 4 | Svårighetsgrad: ⭐ (1/10)
# Krav:
# 1. Skapa en dictionary "person" med följande nyckel-värde-par:
#    - "namn": "Anna"
#    - "ålder": 25
#    - "stad": "Stockholm"
# 2. Skriv ut hela dictionaryn.
# 3. Hämta och skriv ut värdet för nyckeln "namn".
# 4. Hämta och skriv ut värdet för nyckeln "ålder".
# 5. Försök att hämta ett värde med en nyckel som inte finns (t.ex. "yrke") med hakparenteser. (Detta ger KeyError, kommentera ut det).
# 6. Använd metoden .get() för att försöka hämta "yrke". Skriv ut resultatet (blir None).
# 7. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# En dictionary är som en vanlig ordbok: du slår upp ett ord (nyckeln) för att få dess betydelse (värdet). 
# Skillnaden är att en Python-dictionary kan lagra vilka datatyper som helst som värden.
# Tänk dig att du har en massa information om en person. 
# Istället för att ha separata variabler (person_namn, person_ålder, person_stad) 
# kan du samla allt i en enda dictionary. Detta är mycket mer organiserat och skalbart.

# Dictionaries är "muterbara" (föränderliga)
# Till skillnad från tupler (som du inte kan ändra) kan du fritt ändra,
# lägga till och ta bort nycklar i en dictionary. 
# Detta gör dem extremt flexibla.


# === STEG 1 & 2: SKAPA OCH SKRIV UT DICTIONARYN ===

person = {
    "namn":"Anna", 
    "ålder":25,
    "stad":"Stockholm"}

print(person)


# === STEG 3 & 4: HÄMTA VÄRDEN ===

print(person["namn"])
print(person["ålder"])


# === STEG 5: FÖRSÖK HÄMTA MED FEL NYCKEL (KOMMENTERAD) ===

yrke = person["yrke"]

# person["yrke"] → Kraschar med KeyError om nyckeln inte finns.
# person.get("yrke") → Returnerar None (eller ett standardvärde) om nyckeln inte finns. 
# Detta är mycket säkrare!

# === STEG 6: HÄMTA MED .GET() ===

print(person.get("yrke"))

# Varför är .get() bättre än []?
# Om du är osäker på om en nyckel finns är .get() säkrare. 
# Du kan till och med ge ett standardvärde: person.get("yrke", "Inget yrke angivet").