# UPPGIFT 9: HITTA ETT SPECIFIKT TAL (BREAK)
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐⭐ (4/10)
# Krav:
# 1. Fråga användaren hur många tal de vill mata in
# 2. Läs in talen ett i taget i en loop
# 3. Om användaren matar in talet 42 → avbryt loopen direkt med break
# 4. Om loopen avbryts → skriv ut "Talet 42 hittades! Du matade in X tal."
# 5. Om loopen går igenom alla tal utan att hitta 42 → skriv ut "Talet 42 hittades inte."
# 6. Kommentera koden med # för att förklara vad varje rad gör


# === STEG 1: FRÅGA HUR MÅNGA TAL ===

antal_tal = int(input("Hur många tal vill du mata in? ")) # Frågar användaren hur många tal de vill mata in och sparar svaret i variabeln antal_tal. Detta är antalet gånger loopen kommer att köras.


# === STEG 2: SKAPA EN VARIABEL FÖR ATT HÅLLA KOLL PÅ OM TALET HITTADES ===
hittad = False # En variabel som håller koll på om 42 hittades. Om den blir True, avbryts loopen. Om den inte blir True, fortsätter loopen tills alla tal är inmatade.
antal_inmatade = 0 # Detta är en räknare som håller koll på hur många tal som har matats in. Detta används för att kontrollera om alla tal har matats in. Om alla tal har matats in och 42 inte har hittats, skrivs ett meddelande ut. Om 42 har hittats, skrivs ett meddelande ut och loopen avbryts. Startar på 0 eftersom inga tal har matats in än.



# === STEG 3: LOOPA OCH LETA EFTER 42 ===
for i in range(antal_tal): # Loop som körs så många gånger som använd har angett att de vill mata in tal. Detta görs genom att använda range(antal_tal). Detta gör att loopen körs så många gånger som användaren har an
    tal = int(input(f"Mata in tal {i + 1}: ")) # Läs in talet från användaren. Detta görs för varje tal som användaren matar in. Detta görs i en loop som körs så många gånger som användaren har angett att de vill mata in tal.
    antal_inmatade +=1 # Öka räknaren med 1 för varje inmatat tal.
    
    if tal == 42: # Om talet är 42, sätt hittad till True. Detta gör att loopen avbryts. Om talet inte är 42, fortsätter loopen tills alla tal är inmatade.
        hittad = True # Sätt hittad till True om 42 hittas.
        antal_inmatade += 1 # Öka räknaren med 1 för varje inmatat tal.
        break  # Avbryt loopen om 42 hittas.



# === STEG 4: SKRIV UT RESULTATET ===
if hittad: # Om hittad är True, skriv ut att 42 hittades. Om hittad är False, skriv ut att 42 inte hittades.
    print(f"Talet 42 hittades på plats {antal_inmatade} i listan.")
else:
    print("Talet 42 hittades inte.")


# VARFÖR FUNGERAR INTE i + 1 LIKA BRA?
# Man kan använda i + 1 (eftersom i är loopvariabeln), men det finns en anledning att använda en egen räknare:

# 1. Tydlighet: antal_inmatade säger exakt vad den gör. i + 1 kräver att man tänker efter.

# 2. Säkerhet: Om du ändrar i loopen (t.ex. hoppar över vissa tal) stämmer inte i + 1 längre. En egen räknare är mer pålitlig.

# Men i den här enkla uppgiften fungerar båda lika bra. Du kan välja den du tycker är lättast att förstå.