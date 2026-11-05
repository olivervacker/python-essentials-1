# ============================================================
# UPPGIFT 13: LÄGG TILL ELEMENT I EN LISTA
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐ (3/10)
# Krav:
# 1. Skapa en tom lista med namnet "inkopslista"
# 2. Använd en while-loop för att låta användaren lägga till varor
# 3. Fråga användaren: "Vad vill du lägga till? (skriv 'klar' för att avsluta): "
# 4. Om användaren skriver "klar" → avsluta loopen med break
# 5. Annars → lägg till varan i slutet av listan med append()
# 6. Skriv ut hela inköpslistan när loopen är klar
# 7. Skriv ut antalet varor med len()
# 8. Kommentera koden med # för att förklara vad varje rad gör
# ============================================================

# === STEG 1: SKAPA EN TOM LISTA ===

inkopslista = [] # Skapar en tom lista som heter 'inkopslista', som kommer att innehålla alla varor som användaren lägger till.



# === STEG 2: LOOPA OCH LÄGG TILL VAROR (WHILE-LOOP) ===

input("Vad vill du lägga till? (skriv)") # Inbyggd funktion, som tar emot en sträng som argument och skriver ut den i konsolen.
while True: # Startar en oändlig loop som fortsätter tills användaren skriver "klar". 'True' är en boolesk värde som är sant, vilket gör att loopen alltid körs om den inte bryts med t.ex. 'break'.
    vara = input("Vad vill du lägga till? (skriv 'klar' för att avsluta): ") # Tar emot användarens inmatning och lagrar den i variabeln 'vara'. 'input' är en inbyggd funktion som väntar på användarens inmatning och returnerar den som en sträng.    
    if vara == "klar": # if-sats som kontrollerar om användaren har skrivit "klar". Om det är sant, bryts loopen med 'break'.
        break # Avslutar loopen när användaren skriver "klar".   
    else: # Om användaren inte har skrivit "klar", läggs det inmatade värdet till i listan 'inkopslista' med hjälp av metoden 'append'. 'append' är en metod som lägger till ett element i slutet av en lista.   
        inkopslista.append(vara) # Lägger till det inmatade värdet i listan 'inkopslista'. append() är en metod som lägger till ett element i slutet av en lista.



# === STEG 3: SKRIV UT LISTAN OCH ANTALET VAROR ===

print(inkopslista) # Skriver ut hela listan 'inkopslista'.
print (len(inkopslista)) # Skriver ut antalet varor i listan med hjälp av funktionen 'len()'. 'len()' returnerar antalet element i en lista. Detta är en inbyggd funktion i Python som används för att räkna antalet element i en sekvens, som en lista, en sträng eller en tupel.