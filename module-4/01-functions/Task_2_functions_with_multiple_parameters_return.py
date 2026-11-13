# ============================================================
# UPPGIFT 41: FUNKTIONER MED FLERA PARAMETRAR OCH RETURN
# Modul: 4 | Svårighetsgrad: ⭐⭐ (2/10)
# Krav:
# 1. Skapa en funktion "addera" som tar två parametrar (a, b).
# 2. Inuti funktionen: Returnera summan av a och b (använd return).
# 3. Anropa funktionen med talen 5 och 10, och spara resultatet i en variabel.
# 4. Skriv ut resultatet.
# 5. Skapa en funktion "berakna_area" som tar två parametrar (längd, bredd).
# 6. Inuti funktionen: Returnera arean (längd * bredd).
# 7. Anropa funktionen med 4 och 6, och skriv ut resultatet.
# 8. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1 & 2: SKAPA FUNKTIONEN ADDERA ===
def addera (a, b):
    return a + b



# === STEG 3 & 4: ANROPA OCH SKRIV UT ===

summa = addera(5, 10)

print(f"Summan är: {summa}")


# === STEG 5 & 6: SKAPA FUNKTIONEN BERAKNA_AREA ===
def berakna_area(längd, bredd):
    return längd * bredd



# === STEG 7: ANROPA OCH SKRIV UT ===
    
area = berakna_area(4, 6)
print (f"Area: {area}")