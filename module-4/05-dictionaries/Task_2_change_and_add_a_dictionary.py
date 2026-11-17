# ============================================================
# UPPGIFT 62: ÄNDRA OCH LÄGG TILL I EN DICTIONARY
# Modul: 4 | Svårighetsgrad: ⭐⭐ (2/10)
# Krav:
# 1. Skapa en dictionary "bil" med följande par:
#    - "märke": "Volvo"
#    - "modell": "V60"
#    - "år": 2020
# 2. Skriv ut hela dictionaryn.
# 3. Ändra värdet för "år" till 2022.
# 4. Lägg till ett nytt par: "färg": "Blå".
# 5. Skriv ut den uppdaterade dictionaryn.
# 6. Ändra "märke" till "Tesla".
# 7. Skriv ut den uppdaterade dictionaryn igen.
# 8. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1 & 2: SKAPA OCH SKRIV UT DICTIONARYN ===

bil = {"märke": "Volvo", "modell": "V60", "år": 2020} # klammerparanteser indikerar på att det är en dictionary.

print(bil)


# === STEG 3 & 4: ÄNDRA OCH LÄGG TILL ===

bil["år"] = 2022 # Ändra värdet för "år" till 2022.

bil["färg"] = "blå"


# === STEG 5: SKRIV UT DEN UPPDATERADE DICTIONARYN ===

print(bil)


# === STEG 6 & 7: ÄNDRA IGEN OCH SKRIV UT ===

bil["märke"] = "Tesla"

print(bil)