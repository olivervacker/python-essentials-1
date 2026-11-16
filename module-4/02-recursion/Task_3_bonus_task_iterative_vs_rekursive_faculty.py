# ============================================================
# BONUSUPPGIFT: ITERATIV VS REKURSIV FAKULTET
# Modul: 4 | Svårighetsgrad: ⭐⭐⭐ (3/10)
# Krav:
# 1. Skapa en funktion "fakultet_iterativ(n)" som använder en for-loop för att räkna ut fakultet.
# 2. Skapa en funktion "fakultet_rekursiv(n)" som anropar sig själv för att räkna ut fakultet.
# 3. Båda funktionerna ska hantera om n < 0 (returnera None).
# 4. Skriv ut resultaten för båda funktionerna med talen 5 och 7.
# 5. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SKAPA DEN ITERATIVA FUNKTIONEN ===

def fakultet_iterativ(n): # skaparen funktion som anropar sig själv för att räkna ut fakultet.
    if n < 0: # om n är mindre än 0, returnera None
        return None
    result = 1
    for i in range(2, n + 1): # for-loop som räknar ut fakultet. 2 är för att starta från 2, och n + 1 är för att inkludera n i räkningen.
        result *= i # result *= i är samma sak som --> result * 1
    return result
print(fakultet_iterativ(5))




# === STEG 2 & 3: SKAPA DEN REKURSIVA FUNKTIONEN ===

def fakultet_rekursiv(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    
    return n * fakultet_rekursiv(n - 1)


# === STEG 4: SKRIV UT RESULTATEN ===
print(f"Iterativ 5! = {fakultet_iterativ(5)}")
print(f"Rekursiv 5! = {fakultet_rekursiv(5)}")
print(f"Iterativ 7! = {fakultet_iterativ(7)}")
print(f"Rekursiv 7! = {fakultet_rekursiv(7)}")