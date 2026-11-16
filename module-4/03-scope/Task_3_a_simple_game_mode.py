# ============================================================
# UPPGIFT 53: ETT ENKELT SPELTILLSTÅND (GLOBAL SCOPE I PRAKTIKEN)
# Modul: 4 | Svårighetsgrad: ⭐⭐⭐ (3/10)
# Krav:
# 1. Skapa två globala variabler: "hälsa" (sätt till 100) och "poäng" (sätt till 0).
# 2. Skapa en funktion "ta_skada(mängd)".
#    - Inuti funktionen: Använd "global" för att minska "hälsa" med "mängd".
#    - Om hälsa blir 0 eller mindre, sätt hälsa till 0 och skriv ut "Game Over!".
# 3. Skapa en funktion "lägg_till_poäng(p)".
#    - Inuti funktionen: Använd "global" för att öka "poäng" med "p".
# 4. Anropa "ta_skada(30)", "lägg_till_poäng(50)" och "ta_skada(80)".
# 5. Skriv ut det slutgiltiga värdet på "hälsa" och "poäng" utanför funktionerna.
# 6. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SKAPA GLOBALA VARIABLER ===

hälsa = 100
poäng = 0

# === STEG 2: SKAPA FUNKTIONEN TA_SKADA ===

def ta_skada(mängd): # 'mängd' är en parameter som skickas till funktionen när den anropas. Representerar antalet skada som händer.
    global hälsa
    hälsa -= mängd # sammansatt tilldelningsoperator. hälsam -= mängd är samma sak som hälsa = hälsa - mängd
    
    if hälsa <= 0:
        hälsa = 0
        print("Game Over!")



# === STEG 3: SKAPA FUNKTIONEN LÄGG_TILL_POÄNG ===

def lägg_till_poäng(p):
    global poäng
    poäng += p # En sammansatt tilldelningsoperator (compound assignment operator). poäng += p är samma sak som poäng = poäng + p



# === STEG 4: ANROPA FUNKTIONERNA ===

ta_skada(30)
lägg_till_poäng(50)
ta_skada(80)



# === STEG 5: SKRIV UT SLUTRESULTATET ===

print("Du har " + str(hälsa) + " poäng och " + str(poäng) + " totalt.") 

# str() gör att poäng blir en sträng, så det kan skrivas ut som en sträng. 
# Det är också ett exempel på att använda "+" för att lägga till en sträng och en int. 
# Det är också ett exempel på att använda "+" för att lägga till en int och en int. 