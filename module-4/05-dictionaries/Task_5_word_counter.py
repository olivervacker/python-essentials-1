# ============================================================
# UPPGIFT 65: ORDRÄKNARE (DICTIONARY I PRAKTIKEN)
# Modul: 4 | Svårighetsgrad: ⭐⭐⭐⭐⭐ (5/10)
# Krav:
# 1. Fråga användaren att skriva in en mening (text).
# 2. Skapa en tom dictionary "ordräknare" = {}.
# 3. Dela upp meningen i enskilda ord med metoden .split().
#    (Spara orden i en lista, t.ex. ord_lista = mening.split()).
# 4. Loopa genom ord_lista:
#    - Om ordet redan finns i "ordräknare" → öka värdet med 1.
#    - Om ordet inte finns → lägg till det med värdet 1.
# 5. Skriv ut hela "ordräknare" för att se hur många gånger varje ord förekom.
# 6. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: FRÅGA EFTER EN MENING ===

mening = input("Skriv in en mening: ").swapcase()



# === STEG 2: SKAPA TOM DICTIONARY ===

ordräknare = {}



# === STEG 3: DELA UPP I ORD ===

ord_lista = mening.split() # Om mening = "hej på dig hej" blir ord_lista = ["hej", "på", "dig", "hej"]



# === STEG 4: RÄKNA ORDEN ===

for ord in ord_lista:
    if ord in ordräknare:
        ordräknare[ord] += 1
    else:
        ordräknare[ord] = 1



# === STEG 5: SKRIV UT RESULTATET ===

print(ordräknare)
