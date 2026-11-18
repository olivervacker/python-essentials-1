# ============================================================
# UPPGIFT 66: TRY-EXCEPT (FÅNGA FEL)
# Modul: 4 | Svårighetsgrad: ⭐ (1/10)
# Krav:
# 1. Använd en try-except-block för att försöka läsa in ett heltal från användaren.
# 2. Inuti try:
#    - Fråga användaren: "Ange ett heltal: "
#    - Konvertera svaret till int() och spara i en variabel (t.ex. tal).
#    - Skriv ut "Du angav talet: [tal]".
# 3. Inuti except ValueError:
#    - Skriv ut "Fel: Du angav inte ett giltigt heltal!".
# 4. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================


# try-except används för att hantera fel (exceptions) utan att programmet kraschar.
# Try är Kod som KAN orsaka fel – här försöker du utföra en operation.
# Except är Kod som körs OM fel uppstår – här hanterar du felet
# ValueError är ett ogiltigt värde – t.ex. när int() får en sträng med bokstäver


# === STEG 1-3: TRY-EXCEPT BLOCK ===

try:
    tal = int(input("Ange ett heltal: "))
    print("Du angav talet: ", tal)
except ValueError:
    print("Fel: Du angav inte ett giltigt heltal!")

# Ordningen spelar roll!

# Om du hade haft en generell except: först, 
# skulle den fånga alla fel och de specifika except-blocken skulle aldrig köras. 
# Därför är regeln: Specifika fel först, generella fel sist.