# UPPGIFT 7: SUMMERA TAL MED LOOP
# Modul: 3 | Svårighetsgrad: ⭐⭐ (2/10)
# Krav:
# 1. Fråga användaren hur många tal de vill summera
# 2. Läs in så många tal från användaren
# 3. Summera alla tal med hjälp av en for-loop
# 4. Skriv ut summan
# 5. Kommentera koden med # för att förklara vad varje rad gör

# === STEG 1: FRÅGA HUR MÅNGA TAL ===

antal_tal = int(input("Hur många tal vill du summera? ")) # Läs in antalet tal som användaren vill summera och konvertera det till ett heltal (int). Spara värdet i variabeln antal_tal.

tal_lista = [] # Skapa en tom lista som ska innehålla de tal som användaren matar in.
for i in range(antal_tal): # Starta en for-loop som körs så många gånger som användaren angav i variabeln antal tal.
    tal = float(input(f"Ange tal {i + 1}: ")) # För varje iteration i loopen, fråga användaren om ett tal och konvertera det till ett decimaltal (float). Spara värdet i variabeln tal. F-strängen (formatted string) f"Ange tal {i + 1}: " tillåter att skriva variabeln i inuti strängen. Här används för att visa vilket talnummer som användaren matar in. När ett tal matas in så sparas det i variabeln tal och loopvariabeln i ökar med 1.
    tal_lista.append(tal) # En metod som används för att lägga till det inmatade talet i slutet av listan tal_lista.
    
    



# === STEG 2: LÄS IN TALEN OCH SUMMERA ===
summa = sum(tal_lista) # Beräkna summan av alla tal i listan tal_lista och spara resultatet i variabeln summa. Sum() är en inbyggd funktion i Python som adderar alla element i en iterabel (t.ex. en lista). 



# === STEG 3: SKRIV UT SUMMAN ===
print(f"Summan av talen är: {summa}") # Skriv ut summan av talen med hjälp av en f-sträng (formatted string). Detta gör det enkelt att inkludera variabeln summa i utdata. F-strängar är en modern och lättläst metod för att formatera strängar i Python. För att använda en f-sträng, placerar du en f före öppningscitationstecknet, och sedan kan du inkludera variabler direkt inom måsvingar {} i strängen.


# En annan version att skriva koden på:

# # === STEG 1: FRÅGA HUR MÅNGA TAL ===
# antal_tal = int(input("Hur många tal vill du summera? "))
# # input() läser användarens svar som en sträng
# # int() konverterar strängen till ett heltal
# # antal_tal lagrar antalet tal som användaren vill summera

# # === STEG 2: SUMMERA TALEN MED EN LOOP ===
# summa = 0  # Startvärde för summan

# for i in range(antal_tal):
#     # range(antal_tal) skapar talen 0, 1, 2, ..., antal_tal - 1
#     # Loopen körs antal_tal gånger
    
#     tal = float(input(f"Ange tal {i + 1}: "))
#     # f"Ange tal {i + 1}: " visar "Ange tal 1: ", "Ange tal 2: ", etc.
#     # float() konverterar användarens svar till ett decimaltal
#     # tal lagrar det inmatade talet
    
#     summa += tal
#     # Lägger till talet i summan
#     # Samma som: summa = summa + tal

# # === STEG 3: SKRIV UT SUMMAN ===
# print(f"Summan av talen är: {summa}")
# # Skriver ut summan med 2 decimaler
# # Output: "Summan av talen är: 60.0"