# ============================================================
# UPPGIFT 28: KOMBINERA NOT MED AND/OR (INLOGGNINGSSYSTEM)
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐ (3/10)
# Krav:
# 1. Skapa två variabler: "är_inloggad" (sätt till False) och "är_admin" (sätt till False).
# 2. Använd en if-sats med "not" för att kolla om användaren INTE är inloggad.
#    - Om sant, skriv ut "Du måste logga in först.".
# 3. Ändra "är_inloggad" till True.
# 4. Använd en if-sats med "not" och "or" för att kolla:
#    - Om användaren INTE är inloggad ELLER INTE är admin.
#    - Om detta är sant, skriv ut "Du har begränsad åtkomst.".
# 5. Ändra "är_admin" till True.
# 6. Använd en if-sats med "and" för att kolla om användaren är inloggad OCH är admin.
#    - Om sant, skriv ut "Välkommen, administratör!".
# 7. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SKAPA VARIABLERNA ===
är_inloggad = False
är_admin = False




# === STEG 2: ANVÄND "NOT" ===

if not är_inloggad:
    print("Du måste logga in först.")



# === STEG 3: ÄNDRA ÄR_INLOGGAD ===

är_inloggad = True



# === STEG 4: ANVÄND "NOT" OCH "OR" ===

if not är_inloggad or not är_admin: 
    print("Du har begränsad åtkomst!")




# === STEG 5: ÄNDRA ÄR_ADMIN ===

är_admin = True



# === STEG 6: ANVÄND "AND" ===

if är_inloggad and är_admin: 
    print("Välkommen Administratör!")
