# ============================================================
# UPPGIFT 26: LOGISKA OPERATORER (AND, OR, NOT)
# Modul: 3 | Svårighetsgrad: ⭐ (1/10)
# Krav:
# 1. Skapa tre variabler: "ålder" (sätt till 25), "har_körkort" (sätt till True), "är_nykter" (sätt till False).
# 2. Använd en if-sats med operatorn "and" för att kolla om personen får köra bil.
#    (Villkor: ålder >= 18 AND har_körkort == True AND är_nykter == True)
# 3. Om personen får köra, skriv ut "Du får köra bil.".
# 4. Skapa en if-sats med operatorn "or" för att kolla om personen är "under 18" OR "inte har körkort".
#    Om detta är sant, skriv ut "Du får inte köra bil.".
# 5. Använd operatorn "not" för att skriva ut det motsatta värdet av "är_nykter" (dvs. om personen är onykter).
# 6. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SKAPA VARIABLERNA ===
ålder = 25
har_körkort = True
är_nykter = False


# === STEG 2: KONTROLLERA MED "AND" ===
if ålder >= 18 and har_körkort and är_nykter:
    print("Du får köra bil.")


# === STEG 3: KONTROLLERA MED "OR" ===
if ålder <= 18 or not har_körkort: 
    print("Du får inte köra bil.")



# === STEG 4: ANVÄND "NOT" ===
print("Är personen onykter", not är_nykter)