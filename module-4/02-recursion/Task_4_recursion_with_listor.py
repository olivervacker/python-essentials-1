# ============================================================
# UPPGIFT 48: REKURSION MED LISTOR (NEDRÄKNINGSLISTA)
# Modul: 4 | Svårighetsgrad: ⭐⭐⭐⭐ (4/10)
# Krav:
# 1. Skapa en funktion "bygg_nedat(n)" som tar ett heltal (n).
# 2. Funktionen ska returnera en LISTA med tal från n ned till 1.
#    (Exempel: bygg_nedat(3) ska returnera [3, 2, 1]).
# 3. Funktionen MÅSTE använda rekursion.
#    - Basfall: Om n <= 0, returnera en tom lista [].
#    - Rekursivt steg: Returnera [n] + bygg_nedat(n - 1).
#    (Detta kallas för list-konkatenering: att slå ihop två listor med +).
# 4. Anropa funktionen med talet 4 och skriv ut resultatet.
# 5. Anropa funktionen med talet 1 och skriv ut resultatet.
# 6. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1, 2 & 3: SKAPA DEN REKURSIVA FUNKTIONEN ===

# Rekursion med listor är en funktion som returnerar en lista med tal från n ned till 1.



def bygg_nedat(n):
    if n <= 0: # Basfall: Om n <= 0, returnera en tom lista []. 
        return [] # returnera en tom lista []. 
    else:
        return [n] + bygg_nedat(n - 1) # Rekursivt steg: Returnera [n] + bygg_nedat(n - 1). Plusset innebär att konkatinera n och n-1 till listan. 


# === STEG 4 & 5: TESTA FUNKTIONEN ===
print(bygg_nedat(4)) # Skriv ut [4, 3, 2, 1].
print(bygg_nedat(1)) # Skriv ut [1].