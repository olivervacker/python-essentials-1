# ============================================================
# UPPGIFT 25: OPTIMERAD BUBBLE SORT (INTERAKTIV)
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐⭐⭐ (5/10)
# Krav:
# 1. Skapa en tom lista med namnet "siffror".
# 2. Fråga användaren hur många tal de vill sortera (heltal).
# 3. Använd en for-loop för att läsa in så många tal som användaren angav och lägg till dem i listan.
# 4. Skriv ut listan före sortering.
# 5. Skapa en variabel "swapped" och sätt den till True.
# 6. Använd en while-loop som fortsätter så länge "swapped" är True:
#    - Sätt "swapped" till False (anta att listan redan är sorterad).
#    - Använd en for-loop för att jämföra intilliggande element (i och i+1).
#    - Om det vänstra elementet är större än det högra → byt plats och sätt "swapped" till True.
# 7. Skriv ut den färdigsorterade listan.
# 8. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SKAPA EN TOM LISTA ===
siffror = [] # 1. Skapa en tom lista med namnet "siffror" som innehåller t.ex. [8, 10, 6, 2, 4]


# === STEG 2: FRÅGA HUR MÅNGA TAL OCH LÄS IN DEM ===
antal = int(input("Hur många tal vill du sortera? ")) # 2. Fråga användaren hur många tal de vill mata in


for i in range(antal): # Skapar en talsekvens, en sekvens av siffror(t.ex. [8, 10, 6, 2, 4])
    heltal = int(input(f"Ange heltal {i + 1}: "))
    siffror.append(heltal) # Läser in och lägger till talet i slutet av listan


# === STEG 3: SKRIV UT FÖRE SORTERING ===
print("Före sortering", siffror)


# === STEG 4: OPTIMERAD BUBBLE SORT ===

swapped = True # True sätts för att sätta igång while loopen ska fortsätta.

while swapped:
        swapped = False # Sätter swapped till False för att börja om sorteringen inte har skett något ändringar.

        for i in range(len(siffror) - 1): 
            if siffror[i] > siffror[i + 1]:
                swapped = True
                siffror[i], siffror[i + 1] = siffror[i + 1], siffror[i] 


# === STEG 5: SKRIV UT EFTER SORTERING ===
print("Efter sortering: ", siffror) 