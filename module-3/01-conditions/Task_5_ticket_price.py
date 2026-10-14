# UPPGIFT 5: BILJETTPRISET (KOMBINATION AV ALLT)
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐⭐⭐ (5/10)
# Krav:
# 1. Fråga användaren om deras ålder (heltal)
# 2. Fråga användaren om de är student (ja/nej)
# 3. Fråga användaren om det är helg (ja/nej)
# 4. Beräkna biljettpriset baserat på följande regler:
#    - Grundpris: 100 kr
#    - Om åldern är under 18 → 50% rabatt
#    - Om åldern är 65 eller över → 30% rabatt
#    - Om användaren är student → 20% rabatt (utöver åldersrabatt)
#    - Om det är helg → 10% påslag (dyrare på helgen)
# 5. Skriv ut biljettpriset med 2 decimaler
# 6. Kommentera koden med # för att förklara vad varje rad gör

# === STEG 1: FRÅGA ANVÄNDAREN OM ÅLDER ===

# input() läser användarens svar som en sträng
# int() konverterar strängen till ett heltal
# alder lagrar det inmatade värdet

alder = int(input( "Hur gammal är du? ")) # Fråga användaren om ålder och konvertera till heltal



# === STEG 2: FRÅGA ANVÄNDAREN OM STUDENT ===
student = input("Är du student? (ja/nej)").lower() # .lower() gör att både "Ja", "JA" och "ja" blir "ja"



# === STEG 3: FRÅGA ANVÄNDAREN OM HELG ===
helg = input( "Är det helg idag? (ja/nej)").lower() # .lower() gör att både "Ja", "JA" och "ja" blir "ja"


# === STEG 4: BERÄKNA BILJETTPRISET ===

# använda separat if-satser istället för elif-satser. 
# if-elif-else-satser (en gren körs) är bra när du har flera villkor som är kopplade till varandra, men här är de olika villkoren oberoende av varandra.
# if-satser (flera grenar körs) är bra när du har flera villkor som kan vara sanna samtidigt.
# i det här fallet kan en person vara både student och barn, eller student och pensionär, eller bara student, eller bara barn, eller bara pensionär, eller ingen av dem.
# det är därför vi använder if-satser istället för elif-satser.
# det är också därför vi inte använder else
# else-satsen är bara en förkortning för "om inget av de tidigare villkoren är sanna"
# i det här fallet är det inte nödvändigt att använda else, eftersom vi inte har några villkor som är beroende av varandra.
# vi kan också använda elif-satser, men det skulle göra koden mer komplex och svårare att läsa.


biljetpris = 100 # baspriset för en biljett
if alder < 18: # bara barn under 18 år får rabatt
    biljetpris = biljetpris * 0.5 # 50% rabatt för barn under 18 år
if student == "ja":
        biljetpris = biljetpris * 0.8 # 20% rabatt för studenter
if alder >= 65: # bara pensionärer 65 år eller äldre får rabatt
    biljetpris = biljetpris * 0.7 # 30% rabatt för pensionärer
if helg == "ja":
    biljetpris = biljetpris * 1.1 # 10% högre pris på helg



# === STEG 5: SKRIV UT BILJETTPRISET ===

print(f"Ditt biljettpris är: {biljetpris:.2f} kr") # f = formaterad sträng, kr = kronor. Skriver ut biljettpriset med texten "Din biljettpris är: " och biljettpriset i kronor.
# .2f visar talet med 2 decimaler