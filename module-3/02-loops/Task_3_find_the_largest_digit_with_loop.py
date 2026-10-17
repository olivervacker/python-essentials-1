# UPPGIFT 8: HITTA STÖRSTA TALET MED LOOP
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐ (3/10)
# Krav:
# 1. Fråga användaren hur många tal de vill mata in
# 2. Läs in så många tal från användaren
# 3. Använd en loop för att hitta det STÖRSTA talet
# 4. Skriv ut det största talet
# 5. Kommentera koden med # för att förklara vad varje rad gör

# === STEG 1: FRÅGA HUR MÅNGA TAL ===

antal_tal = int(input("Hur många tal vill du mata in? ")) # Användaren matar in hur många tal de vill mata in
tal_lista = [] # Skapar en tom lista för att lagra tal
for i in range(antal_tal): # Loopar genom antalet tal användaren vill mata in
    tal = float(input("Ange ett tal: ")) # Användaren matar in ett tal som konverteras till float
    tal_lista.append(tal) # Lägger till talet i listan 


# === STEG 2: LÄS IN TALEN OCH HITTA STÖRSTA ===

största_tal = tal_lista[0] # Index 0 ([0]) är det första talet i listan. Antager att det första talet är det största
for tal in tal_lista: # Loopar genom alla tal (tal_lista) och jämför med största_tal (det första talet ) i listan och lagrar det största talet i största_tal-variabeln. Om talet är större än största_tal så uppdateras största_tal med det nya talet.
    if tal > största_tal: # Om talet är större än största_tal så uppdateras största_tal med det nya talet 
        största_tal = tal # Uppdaterar största_tal med det nya största talet som hittats i listan 


# === STEG 3: SKRIV UT DET STÖRSTA TALET ===

print(f"Det största talet är: {största_tal}") # Skriver ut det största talet som hittats i listan. F-sträng (formmated-string) tillåter att man kan skriva ut variabler direkt i strängen.
