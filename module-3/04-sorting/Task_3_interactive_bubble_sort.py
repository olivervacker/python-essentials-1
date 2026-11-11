# UPPGIFT 23: INTERAKTIV BUBBLE SORT
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐ (3/10)
# Krav:
# 1. Skapa en tom lista med namnet "siffror".
# 2. Fråga användaren hur många tal de vill sortera (heltal).
# 3. Använd en for-loop för att läsa in så många tal som användaren angav, och lägg till dem i listan.
# 4. Skriv ut listan före sortering.
# 5. Skapa en variabel "swapped" och sätt den till True.
# 6. Använd en while-loop som fortsätter så länge "swapped" är True:
#    - Sätt "swapped" till False.
#    - Använd en for-loop för att jämföra intilliggande element (i och i+1).
#    - Om det vänstra elementet är större än det högra → byt plats och sätt "swapped" till True.
# 7. Skriv ut den färdigsorterade listan.
# 8. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: SKAPA EN TOM LISTA ===
siffror = [] # 1. Skapa en tom lista med namnet "siffror" som innehåller t.ex. [8, 10, 6, 2, 4]


# === STEG 2: FRÅGA HUR MÅNGA TAL OCH LÄS IN DEM ===
antal = int(input("Hur många tal vill du sortera? ")) # 2. Fråga användaren hur många tal de vill mata in


for i in range(antal): # Skapar en talsekvens, t.ex. om användaren anger att hen vill lagra 5 tal, så skapar den en talsekvens med 5 element i den tomma listan, t.ex. [8, 10, 6, 2, 4]
    heltal = int(input(f"Ange heltal {i + 1}: "))
    siffror.append(heltal)


# === STEG 3: SKRIV UT FÖRE SORTERING ===
print(siffror)


# === STEG 4: SORTERA MED BUBBLE SORT ===
swapped = True # 1. Skapa en variabel "swapped" och sätt den till True. Sätts till True eftersom det finns minst ett tal som måste bytas om det är större än nästa tal. While-loopen körs bara om villkoret är True.
while swapped: # 2. Skapa en while-loop som kör så länge "swapped" är True.
    swapped = False # 3. Sätt "swapped" till False för att förhindra att while-loopen kör igen om det inte finns fler tal att byta om det är större än nästa tal.
    for i in range(len(siffror) - 1): # 4. Använd en for-loop för att jämföra och byta om det är större än nästa tal. -1 används för att hindra att det går utanför listan och för att undvika out-of-bounds error. 
        if siffror[i] > siffror[i + 1]: # 5. Om det är större än nästa tal, byt dem om. Sätt "swapped" till True för att indikera att det har blivit bytt (om vänstra siffran är högre än den högra siffran).) 
            siffror[i], siffror[i + 1] = siffror[i + 1], siffror[i] # 6. Byt siffran om det är större än nästa tal (byter siffran och nästa siffran).
            swapped = True # 7. Sätt "swapped" till True för att indikera att det har blivit bytt (om vänstra siffran är högre än den högra siffran).) 

# === STEG 5: SKRIV UT EFTER SORTERING ===
print("Efter sortering", siffror)  # Skriver ut den sorterade listan