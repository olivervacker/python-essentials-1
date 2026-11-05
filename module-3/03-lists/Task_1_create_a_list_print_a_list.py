# ============================================================
# UPPGIFT 11: SKAPA OCH SKRIV UT EN LISTA
# Modul: 3 | Svårighetsgrad: ⭐ (1/10)
# Krav:
# 1. Skapa en lista med namnet "frukter" som innehåller: "äpple", "banan", "apelsin"
# 2. Skriv ut hela listan
# 3. Skriv ut det första elementet i listan (använd index)
# 4. Skriv ut det sista elementet i listan (använd negativt index)
# 5. Ändra det andra elementet i listan till "päron"
# 6. Skriv ut hela listan igen för att se ändringen
# 7. Kommentera koden med # för att förklara vad varje rad gör
# ============================================================

# === STEG 1: SKAPA LISTAN ===

frukter = ["äpple", "banan", "apelsin"] # Skapar en lista med namnet "Frukter" som innehåller tre element: "äpple", "banan" och " apelsin".

# === STEG 2: SKRIV UT HELA LISTAN ===
print(frukter) # Slice-funktiom (:) används för att skriva ut hela listan (alla element i listan). 



# === STEG 3: SKRIV UT FÖRSTA OCH SISTA ELEMENTET ===

print(frukter[0]) # Skriver ut sista elementet i listan.
frukter[1] = "päron" # Ändrar det andra elementet i listan till "päron".
print(frukter[1]) # Skriver ut de två första elementen i listan.
print (frukter) # Skriver ut hela listan igen för att se ändringarna som gjorts.