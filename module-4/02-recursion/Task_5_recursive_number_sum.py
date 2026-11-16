# ============================================================
# UPPGIFT 49: REKURSIV SIFFersUMMA (DIGITAL SUM)
# Modul: 4 | Svårighetsgrad: ⭐⭐⭐⭐⭐ (5/10)
# Krav:
# 1. Skapa en funktion "siffer_summa(n)" som tar ett positivt heltal (n).
# 2. Funktionen ska returnera summan av alla siffror i talet med hjälp av REKURSION.
#    - Exempel: siffer_summa(123) ska bli 1 + 2 + 3 = 6.
# 3. Basfall: Om n < 10, returnera n (eftersom en enskild siffra är sin egen summa).
# 4. Rekursivt steg:
#    - Ta reda på den sista siffran med modulus: n % 10.
#    - Ta reda på resten av talet med heltalsdivision: n // 10.
#    - Returnera: (n % 10) + siffer_summa(n // 10).
# 5. Anropa funktionen med 123 och skriv ut resultatet.
# 6. Anropa funktionen med 9875 och skriv ut resultatet.
# 7. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1, 2, 3 & 4: SKAPA DEN REKURSIVA FUNKTIONEN ===

def siffer_summa(n):
    if n < 10: # Basfall: Om n är mindre än 10, returnera n (eftersom en enskild siffra är sin egen summa).
        return n
    else:
        return (n % 10) + siffer_summa(n // 10) # Returnera summan av sista siffran och resten av talet.


# === STEG 5 & 6: TESTA FUNKTIONEN ===
print(f"Summan av siffrorna i 123 är: {siffer_summa(123)}")  # Ska returnera 6
print(f"Summan av siffrorna i 9875 är: {siffer_summa(9875)}")  # Ska returnera 29
