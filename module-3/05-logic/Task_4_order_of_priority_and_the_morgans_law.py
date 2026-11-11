# ============================================================
# UPPGIFT 29: PRIORITETSORDNING OCH DE MORGANS LAGAR
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐⭐ (4/10)
# Krav:
# 1. Skapa variablerna: "p" = True, "q" = False.
# 2. Skriv ut resultatet av: not p or q (utan parenteser).
# 3. Skriv ut resultatet av: not (p or q) (med parenteser).
# 4. Skapa en variabel "de_morgan_1" som testar lagen: not (p and q).
# 5. Skapa en variabel "de_morgan_2" som testar lagen: (not p) or (not q).
# 6. Skriv ut båda variablerna för att se att de är lika (De Morgans lag).
# 7. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SKAPA VARIABLERNA ===

p = True
q = False


# === STEG 2 & 3: PRIORITETSORDNING ===

print( not p or q) 
print(not (p or q))


# === STEG 4 & 5: DE MORGANS LAGAR ===

de_morgan_1 = not (p and q)
de_morgan_2 = (not p) or (not q)



# === STEG 6: SKRIV UT RESULTATEN ===
print( de_morgan_1, de_morgan_2)  # De Morgans lagarna ska vara lika (True) för att vara korrekt.