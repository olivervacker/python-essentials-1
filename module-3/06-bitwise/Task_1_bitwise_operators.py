# ============================================================
# UPPGIFT 31: BITVISA OPERATORER (AND, OR, XOR)
# Modul: 3 | Svårighetsgrad: ⭐ (1/10)
# Krav:
# 1. Skapa två variabler: "a" = 5 (binärt: 0101) och "b" = 3 (binärt: 0011).
# 2. Använd bitvis AND (&) på a och b. Spara resultatet i en variabel.
# 3. Använd bitvis OR (|) på a och b. Spara resultatet i en variabel.
# 4. Använd bitvis XOR (^) på a och b. Spara resultatet i en variabel.
# 5. Skriv ut alla tre resultaten.
# 6. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SKAPA VARIABLERNA ===

a = 5
b = 3


# === STEG 2, 3 & 4: UTFÖR BITVISA OPERATIONER ===

Bitvis_and = a & b
Bitvis_or = a | b
Bitvis_xor = a ^ b


# === STEG 5: SKRIV UT RESULTATEN ===
print(Bitvis_and)
print(Bitvis_or)
print(Bitvis_xor)
