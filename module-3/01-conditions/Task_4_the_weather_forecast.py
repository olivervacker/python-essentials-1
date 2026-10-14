# UPPGIFT 4: VÄDERPROGNOSEN – DEL 4 (NÄSTLADE IF-SATSER)
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐⭐ (4/10)
# Krav:
# 1. Fråga användaren om temperaturen utomhus
# 2. Fråga användaren om det regnar (ja/nej)
# 3. Konvertera temperaturen till ett decimaltal (float)
# 4. Använd NÄSTLADE if-satser för att ge rätt råd:
#    - Om temperaturen är över 20:
#        - Om det regnar → "Varmt men regnigt. Ta med paraply!"
#        - Om det inte regnar → "Varmt och soligt. Njut av dagen!"
#    - Om temperaturen är 20 eller lägre:
#        - Om det regnar → "Kallt och regnigt. Stanna inne!"
#        - Om det inte regnar → "Kallt men torrt. Ta på dig jackan!"
# 5. Kommentera koden med # för att förklara vad varje rad gör


# === STEG 1: FRÅGA ANVÄNDAREN OM TEMPERATUREN ===

temperatur = float(input("Vad är temperaturen utomhus? ")) # temperatur lagrar det inmatade värdet som ett decimaltal
# input() läser användarens svar som en sträng
# float() konverterar strängen till ett decimaltal
# temperatur lagrar det inmatade värdet

# === STEG 2: FRÅGA ANVÄNDAREN OM DET REGNAR ===

regnar = input("Regnar det? (ja/nej) ").lower()
# input() läser användarens svar som en sträng
# .lower() gör om "Ja" och "JA" till "ja" (hanterar stora/små bokstäver). Utan .lower() skulle "Ja" och "ja" behandlas olika och ge felaktigt resultat
# .lower() gör om alla bokstäver till gemener/ små bokstäver (ska inte användas på siffror), namn.lower() = "anna"
# .upper() gör om alla bokstäver till versaler/ stora bokstäver (ska inte användas på siffror), namn.upper() =  "ANNA"
# .find(x)	Hittar första positionen av x
# .strip()	Rensar bort mellanslag i början och slutet av strängen
# .replace(x, y)	Ersätter x med y i strängen 
# .count(x)	Räknar antal förekomster av x i strängen
# regnar lagrar användarens svar ("ja" eller "nej")


# EXTRA INFO

# .swapcase() = Byter stora ↔ små
# .capitalize()	Första bokstaven stor, resten små
# .title()	Första bokstaven i varje ord stor

# Viktigt: Strängar är oföränderliga – metoderna ändrar inte originalsträngen, de returnerar en ny sträng.


# === STEG 3: KONTROLLERA MED NÄSTLADE IF-SATSER ===

# Nästlade if-satser är if-satser inuti andra if-satser. Används för att hantera flera villkor.

if temperatur > 20:
    # Yttre if: temperaturen är över 20 (varmt)
    
    if regnar == "ja": # Nästlade if-sats, == jämför två värden
        # Inre if: det regnar
        print("Varmt men regnigt. Ta med paraply!")
    else: # Nästlade else-sats, körs om villkoret inte är sant 
        # Inre else: det regnar inte
        print("Varmt och soligt. Njut av dagen!")

else: # Yttre else-sats, körs om villkoret inte är sant 
    # Yttre else: temperaturen är 20 eller lägre (kallt)
    
    if regnar == "ja": # Nästlade if-sats, == jämför två värden 
        # Inre if: det regnar
        print("Kallt och regnigt. Stanna inne!")
    else: # Nästlade else-sats, körs om villkoret inte är sant 
        # Inre else: det regnar inte
        print("Kallt men torrt. Ta på dig jackan!")