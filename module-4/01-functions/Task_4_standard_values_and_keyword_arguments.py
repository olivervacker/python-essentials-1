# ============================================================
# UPPGIFT 43: STANDARDVÄRDEN OCH KEYWORD-ARGUMENT
# Modul: 4 | Svårighetsgrad: ⭐⭐⭐⭐ (4/10)
# Krav:
# 1. Skapa en funktion "halsa" som tar två parametrar: "namn" och "hälsning".
# 2. Ge parametern "hälsning" ett standardvärde: "Hej".
# 3. Inuti funktionen: Returnera en sträng som säger "[hälsning], [namn]!".
# 4. Anropa funktionen med bara ett argument ("Anna") och skriv ut resultatet.
# 5. Anropa funktionen med två argument ("Erik", "God morgon") och skriv ut resultatet.
# 6. Anropa funktionen med keyword-argument: halsa(namn="Sofia", hälsning="Välkommen") och skriv ut resultatet.
# 7. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1, 2 & 3: SKAPA FUNKTIONEN ===

def halsa(namn, hälsning = "Hej"):
    return f"{hälsning}, {namn}!"



# === STEG 4: ANROPA MED ETT ARGUMENT ===


resultat1 = halsa("Anna") # anropar funktionen halsa med ett argument ("Anna") och skriver ut resultatet.
print(resultat1)




# === STEG 5: ANROPA MED TVÅ ARGUMENT ===


resultat2 = halsa("Erik", "God morgon") # anropar funktionen halsa med två positionella argument ("Erik" och "God morgon") och skriver ut resultatet, ersätter standardvärde för hälsning = "Hej"
print(resultat2)


halsa("Erik", "God morgon")




# === STEG 6: ANROPA MED KEYWORD-ARGUMENT ===

resultat3 = halsa(hälsning = "Välkommen", namn = "Sofia") # anropar funktionen halsa med keyword-argument, ersätter standardvärde för hälsning = "Hej"
print(resultat3)