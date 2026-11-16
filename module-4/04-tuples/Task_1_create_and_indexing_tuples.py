# ============================================================
# UPPGIFT 56: SKAPA OCH INDEXERA TUPLER
# Modul: 4 | Svårighetsgrad: ⭐ (1/10)
# Krav:
# 1. Skapa en tuple "koordinater" med två värden: 10 och 20.
# 2. Skriv ut hela tuplen.
# 3. Skriv ut det första värdet (index 0).
# 4. Skriv ut det sista värdet (använd negativt index, -1).
# 5. Skapa en tuple "en_sak" med bara ett element: "äpple" (glöm inte kommatecknet!).
# 6. Skriv ut "en_sak" och använd type() för att bekräfta att det är en tuple.
# 7. Försök att ändra det första värdet i "koordinater" till 99 (detta kommer att ge ett TypeError, vilket är meningen! Kommentera ut raden).
# 8. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1 & 2: SKAPA OCH SKRIV UT TUPLEN ===

koordinater = (10, 20) # En tuple är en immutable (oförenderlig) lista av värden, vilket betyder att du inte kan ändra det efter det du har skapat den.
print(koordinater) # Skriv ut tuplen.


# === STEG 3 & 4: INDEXERA ===

print(koordinater[0]) # Första indexet i listan. Det första värdet i tuplen är 10.
print(koordinater[1]) # Den sista indexen i listan. Det andra värdet i tuplen är 20.


# === STEG 5 & 6: EN-ELEMENT TUPLE ===

en_sak = ("äpple",) # En tuple kan innehålla en element.
print(en_sak) # Skriv ut tuplen.
print(type(en_sak)) # Skriver ut datatypenen. Detta är en tuple.


# === STEG 7: FÖRSÖK ÄNDRA (KOMMENTERAD) ===
# ny_koordinater = koordinater[0] = 99 # Detta är felaktig. Du kan inte ändra en tupel. Du kan bara lägga till eller ta bort element.