# ============================================================
# UPPGIFT 67: FLERA EXCEPT-BLOCK (DIVISION)
# Modul: 4 | Svårighetsgrad: ⭐⭐ (2/10)
# Krav:
# 1. Använd ett try-except-block för att utföra en division.
# 2. Inuti try:
#    - Fråga användaren om två heltal (täljare och nämnare).
#    - Konvertera dem till int().
#    - Utför divisionen: resultat = täljare / nämnare.
#    - Skriv ut resultatet.
# 3. Lägg till ett except ValueError:
#    - Skriv ut "Fel: Du måste ange heltal!".
# 4. Lägg till ett except ZeroDivisionError:
#    - Skriv ut "Fel: Kan inte dividera med noll!".
# 5. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================


# try-except används för att hantera fel (exceptions) utan att programmet kraschar.
# Try är Kod som KAN orsaka fel – här försöker du utföra en operation.
# Except är Kod som körs OM fel uppstår – här hanterar du felet


# === STEG 1-4: TRY-EXCEPT MED FLERA FEL ===

try:
    täljare = int(input("Ange täljare (ange ett tal): "))
    nämnare = int(input("Ange nämnare (ange ett till tal): "))
    resultat = täljare / nämnare # Utför divisionen
    print("Resultatet är:", resultat)
except ValueError:
    print("Fel: Du måste ange heltal!")
except ZeroDivisionError: # ZeroDivisionError är ett fel som kan uppstå när man försöker dividera ett tal med noll.
    print("Fel: Kan inte dividera med noll!")