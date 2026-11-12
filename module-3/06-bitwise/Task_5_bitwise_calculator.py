# ============================================================
# UPPGIFT 35: BITVIS KALKYLATOR
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐⭐⭐ (5/10)
# Krav:
# 1. Fråga användaren om två heltal (a och b).
# 2. Fråga användaren vilken bitvis operation de vill utföra (skriv "AND", "OR", "XOR" eller "NOT").
# 3. Om användaren väljer "AND":
#    - Utför a & b och skriv ut resultatet både som decimaltal och binärt (använd bin()).
# 4. Om användaren väljer "OR":
#    - Utför a | b och skriv ut resultatet både som decimaltal och binärt.
# 5. Om användaren väljer "XOR":
#    - Utför a ^ b och skriv ut resultatet både som decimaltal och binärt.
# 6. Om användaren väljer "NOT":
#    - Utför ~a (och ~b) och skriv ut resultaten både som decimaltal och binärt.
# 7. Om användaren skriver något annat:
#    - Skriv ut "Ogiltigt val. Välj AND, OR, XOR eller NOT.".
# 8. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: FRÅGA OM TVÅ TAL ===

a = int(input("Ange första talet: "))

b = int(input( "Ange andra talet: "))


# === STEG 2: FRÅGA OM OPERATION ===

operation = input("Välj operation: AND, OR, XOR, NOT: ").swapcase()


# === STEG 3-7: UTFÖR RÄTT OPERATION MED IF-ELIF-ELSE ===

if operation == "AND":
    result = a & b # bitvisa operator 'and' som där värdena på binärt behöver matcha värdena för att vara 1

    print("Resultatet av AND är:", result, "som binärt är:", bin(result))
elif operation == "OR":
    result = a | b # bitvisa operator 'or' som där värdena på binärt jämföres och om någon är 1, blir det 1

    print("Resultatet av OR är:", result, "som binärt är:", bin(result))
elif operation == "XOR": # bitvisa operator 'xor' som där värdena på binärt jämföres och om värdenas 1 och 0 är olika så det blir 1
    result = a ^ b
    print("Resultatet av XOR är:", result, "som binärt är:", bin(result))
elif operation == "NOT": # bitvisa operator 'not' som där värdena på binärt inverseras (spegelvänds, 0 till 1)
    result_a = ~a
    result_b = ~b
    print(f"NOT {a}: {result_a} (Binärt: {bin(result_a)})")
    print(f"NOT {b}: {result_b} (Binärt: {bin(result_b)})")
else:
    print("Ogiltigt val. Välj AND, OR, XOR eller NOT.")