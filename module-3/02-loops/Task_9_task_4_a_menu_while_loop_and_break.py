# ============================================================
# UPPGIFT 19: MENY MED WHILE TRUE OCH BREAK
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐⭐ (4/10)
# Krav:
# 1. Använd en while True-loop för att visa en meny om och om igen.
# 2. Menyn ska se ut så här:
#    --- MENY ---
#    1. Säg hej
#    2. Säg hejdå
#    3. Avsluta
# 3. Läs in användarens val (1, 2 eller 3).
# 4. Om valet är 1 → skriv ut "Hej på dig!".
# 5. Om valet är 2 → skriv ut "Hejdå!".
# 6. Om valet är 3 → skriv ut "Programmet avslutas." och använd break för att avsluta loopen.
# 7. Om användaren skriver något annat → skriv ut "Ogiltigt val, försök igen.".
# 8. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1: WHILE TRUE-LOOP FÖR MENYN ===


while True: # 1. Använd en while True-loop för att visa en meny om och om igen om användaren väljer ett alternativ.
    print("--- MENY ---")
    print("1. Säg hej")
    print("2. Säg hejdå")
    print("3. Avsluta")


# === STEG 2: LÄS IN ANVÄNDARENS VAL ===
    val = (input("Välj ett alternativ (1-3): ")) # 2. Använd input-funktionen för att läsa in användarens val.



# === STEG 3: HANTERA VALET MED IF-ELIF-ELSE ===
    if val == "1": # 3. Använd if-elif-else för att hantera olika val och utföra olika uppgifter. 
        print("Hej på dig!")
    elif val == "2": # En elif-sats som är bra att använda när det finns flera alternativ som tillhör en uppgift.
        print("Hejdå!")
    elif val == "3":
        print("programmet avslutas.")
        break # Använd break-funktionen för att avsluta while-loopen när användaren väljer att avsluta programmet.
    else: # En else-sats som är bra att använda när det finns ett standardfall. Om inget annat val uppfyller kraven.
        print("Ogiltigt val, försök igen.")