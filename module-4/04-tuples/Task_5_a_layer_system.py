# ============================================================
# UPPGIFT 60: LAGERSYSTEM (LISTOR MED TUPLER)
# Modul: 4 | Svårighetsgrad: ⭐⭐⭐⭐⭐ (5/10)
# Krav:
# 1. Skapa en lista "lager" som innehåller tupler.
#    Varje tuple ska representera en vara: (VaruID, Produktnamn, Antal_i_lager).
# 2. Lägg till följande tre varor i listan "lager":
#    - (101, "Skruvmejsel", 25)
#    - (102, "Hammare", 10)
#    - (103, "Spik", 500)
# 3. Skriv ut hela listan.
# 4. Använd en for-loop för att loopa genom listan "lager".
# 5. Packa upp varje tuple i variablerna: id, namn, antal (i loopen).
# 6. Om antalet är mindre än 15, skriv ut: "VARNING: [namn] har lågt lager ([antal] st)!".
# 7. Annars, skriv ut: "[namn] finns i lager: [antal] st.".
# 8. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1 & 2: SKAPA LISTAN MED TUPLER ===

lager = (
    (101, "Skruvmejsel", 25),
    (102, "Hammare", 10),
    (103, "Spik", 500))


# === STEG 3: SKRIV UT HELA LISTAN ===

print(lager)



# === STEG 4-7: LOOPA OCH KONTROLLERA LAGRET ===

for id, namn, antal in lager:
    if antal < 15:
        print(f"VARNING: {namn} har lågt lager ({antal} st.)!")
    else:
        print(f"{namn} finns i lager: {antal} st.")
