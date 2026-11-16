# ============================================================
# UPPGIFT 57: LOOPS OCH KONVERTERING AV TUPLER
# Modul: 4 | Svårighetsgrad: ⭐⭐ (2/10)
# Krav:
# 1. Skapa en tuple "frukter" med tre element: "äpple", "banan", "apelsin".
# 2. Använd en for-loop för att skriva ut varje frukt i tuplen.
# 3. Skapa en lista "grönsaker" med tre element: "morot", "potatis", "lök".
# 4. Konvertera listan "grönsaker" till en tuple med funktionen tuple(). Spara i variabeln "grönsaker_tuple".
# 5. Skriv ut "grönsaker_tuple" och använd type() för att bekräfta att det är en tuple.
# 6. Konvertera tuplen "frukter" till en lista med funktionen list(). Spara i variabeln "frukter_lista".
# 7. Skriv ut "frukter_lista" och använd type() för att bekräfta att det är en lista.
# 8. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1 & 2: SKAPA TUPLE OCH LOOPS ===

frukter =("äpple", "banan", "aplesin")
for frukt in frukter:
    print(frukt)


# === STEG 3: SKAPA LISTA ===

grönsaker = ["morot", "potatis", "lök"]




# === STEG 4 & 5: KONVERTERA LISTA TILL TUPLE ===

grönsaker_tuple = tuple(grönsaker)
print(grönsaker_tuple)
print(type(grönsaker_tuple))



# === STEG 6 & 7: KONVERTERA TUPLE TILL LISTA ===

frukter_lista = list(frukter)
print(frukter_lista)
print(type(frukter_lista))