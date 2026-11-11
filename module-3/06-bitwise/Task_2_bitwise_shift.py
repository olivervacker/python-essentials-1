# ============================================================
# UPPGIFT 32: BITVISA SKIFT (VÄNSTER OCH HÖGER)
# Modul: 3 | Svårighetsgrad: ⭐⭐ (2/10)
# Krav:
# 1. Skapa en variabel "x" = 5.
# 2. Använd vänsterskift (<<) för att skifta x 1 steg åt vänster. Spara i en variabel.
# 3. Använd högerskift (>>) för att skifta x 1 steg åt höger. Spara i en variabel.
# 4. Skriv ut resultaten av båda operationerna.
# 5. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SKAPA VARIABELN ===

x = 5

# === STEG 2 & 3: UTFÖR SKIFT ===

vänster = x<<1
höger = x>>1


# === STEG 4: SKRIV UT RESULTATEN ===

print(f"Vänsterskift: {vänster}")
print(f"Högerskift: {höger}")
