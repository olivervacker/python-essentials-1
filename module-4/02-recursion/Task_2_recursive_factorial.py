# ============================================================
# UPPGIFT 46: REKURSIV FAKULTET
# Modul: 4 | Svårighetsgrad: ⭐⭐ (2/10)
# Krav:
# 1. Skapa en funktion "fakultet(n)" som tar ett heltal (n).
# 2. Funktionen ska beräkna n! (n-fakultet) med hjälp av REKURSION.
#    - Kom ihåg basfallet: 0! = 1 och 1! = 1.
#    - Det rekursiva anropet: n! = n * (n-1)!
# 3. Om n är mindre än 0, returnera None (eller 0) och skriv ut ett felmeddelande (valfritt).
# 4. Anropa funktionen med talet 5 och skriv ut resultatet.
# 5. Anropa funktionen med talet 3 och skriv ut resultatet.
# 6. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1, 2 & 3: SKAPA DEN REKURSIVA FUNKTIONEN ===

def fakultet(n):
    # Basfallet: n! = 1 om n <= 0

    if n < 0:
        return None  # Returnera None om n är mindre än 0
    if n == 0 or n == 1:  # Basefall: 0! = 1 och 1! = 1
        return 1
    return n * fakultet(n - 1)  # Rekursiv anropet: n! = n * (n-1)!


# === STEG 4 & 5: TESTA FUNKTIONEN ===

print(f"5! = {fakultet(5)}")  # Anropa funktionen med talet 5 och skriv ut resultatet
print(f"3! = {fakultet(3)}")  # Anropa funktionen med talet 3 och skriv ut resultatet