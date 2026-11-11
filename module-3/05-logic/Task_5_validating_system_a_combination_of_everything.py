# ============================================================
# UPPGIFT 30: VALIDERINGSYSTEM (KOMBINATION AV ALLT)
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐⭐⭐ (5/10)
# Krav:
# 1. Fråga användaren om ett användarnamn (text).
# 2. Fråga användaren om ett lösenord (text).
# 3. Fråga användaren om deras ålder (heltal).
# 4. Skapa följande valideringsregler:
#    - Användarnamnet måste vara minst 3 tecken långt (använd len()).
#    - Lösenordet måste vara minst 8 tecken långt.
#    - Åldern måste vara 18 eller äldre.
# 5. Kontrollera reglerna med en if-sats:
#    - Om användarnamnet är för kort ELLER lösenordet är för kort ELLER åldern är under 18 → skriv ut "Registrering misslyckades. Kontrollera dina uppgifter.".
#    - Annars (om ALLA regler är uppfyllda) → skriv ut "Välkommen! Registreringen lyckades.".
# 6. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1, 2 & 3: FRÅGA ANVÄNDAREN ===
namn = input("Ange ditt användarnamn: ")
lösenord = input("Ange ditt lösenord: ")
ålder = int(input("Ange din ålder: "))


# === STEG 4 & 5: VALIDERA MED LOGISKA OPERATORER ===
if len(namn) < 3 or len(lösenord) < 8 or ålder < 18:
    print("Registreringen misslyckades. Kontrollera dina uppgifter")
else:
    print("Välkommen! Registreringen lyckades")