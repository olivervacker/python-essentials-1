# ============================================================
# UPPGIFT 63: LOOPS I DICTIONARIES (KEYS, VALUES, ITEMS)
# Modul: 4 | Svårighetsgrad: ⭐⭐⭐ (3/10)
# Krav:
# 1. Skapa en dictionary "betyg" med följande par:
#    - "Anna": "A"
#    - "Erik": "B"
#    - "Sofia": "C"
# 2. Loopa genom dictionaryn med .keys() och skriv ut alla namn (nycklar).
# 3. Loopa genom dictionaryn med .values() och skriv ut alla betyg (värden).
# 4. Loopa genom dictionaryn med .items() och skriv ut både namn och betyg snyggt formaterat (t.ex. "Anna fick betyget A").
# 5. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SKAPA DICTIONARYN ===

betyg = {"Anna": "A", "Erik": "B", "Sofia": "C"}


# === STEG 2: LOOPS MED .KEYS() ===

for namn in betyg.keys(): # Loopar genom alla namn med .keys (nycklar) i dictionaryn
    print(namn)


# === STEG 3: LOOPS MED .VALUES() ===

for betygsvar in betyg.values(): # Loopar genom alla betyg med .values (värden) i dictionaryn
    print(betygsvar)



# === STEG 4: LOOPS MED .ITEMS() ===

for namn, betygsvar in betyg.items(): # Loopar igenom .items() för att få både namn och betyg (nycklar och värden)
    print(f"{namn} fick betyget {betygsvar}")