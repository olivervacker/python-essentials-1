# UPPGIFT 10: HOPPA ÖVER VISSA TAL (CONTINUE)
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐⭐⭐ (5/10)
# Krav:
# 1. Läs in 10 heltal från användaren (använd en for-loop)
# 2. Om talet är negativt (mindre än 0) → hoppa över det med continue
# 3. Om talet är 0 → avbryt hela loopen med break
# 4. Summera alla positiva tal som matas in
# 5. Skriv ut summan i slutet
# 6. Kommentera koden med # för att förklara vad varje rad gör

# === STEG 1: SKAPA EN VARIABEL FÖR SUMMAN ===

total_summan = 0 

print ("Skriv in 10 heltal (0 hoppar över och avbryter loopen och negativa tal hoppas över)")

# === STEG 2: LOOPA 10 GÅNGER OCH LÄS IN TAL ===
for i in range(10): # for-loop som räknar från 1 till 10 med hjälp av range(1, 11). 'i' är ett variabel som representerar det aktuella talet i loop som börjar på 1 och fortsätter till 10. 
    
    ange_tio_tal = int(input(f"tal {1+i}: ")) # användaren matar in tio tal som sedan lagras i variabeln ange_tio_tal som sedan konverteras till en heltal med hjälp av int(). Detta görs genom att använda en for-loop som räknar från 1 till 10. 'i' är ett variabel som representerar det aktuella talet i loopen. 'in' står för att loopen ska iterera över en sekvens. 'range' är en funktion som genererar en sekvens av tal. I detta fall genererar den talen från 1 till 10. 1-10 är det intervall som loopen ska räkna över.
    
    if ange_tio_tal < 0: 
        print("negativa tal är inte tillåtna")
        break
    if ange_tio_tal == 0:
        print("noll är inte tillåtet, hoppar över")
        continue

    total_summan += ange_tio_tal  # Lägger till det inmatade talet till summan.         

# === STEG 3: SKRIV UT SUMMAN ===
print(f"Summan av alla tal är: {total_summan}")  # Skriver ut summan av alla tal som användaren matade in. 