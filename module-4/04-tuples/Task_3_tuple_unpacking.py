# ============================================================
# UPPGIFT 58: TUPLE UNPACKING (PACKA UPP VÄRDEN)
# Modul: 4 | Svårighetsgrad: ⭐⭐⭐ (3/10)
# Krav:
# 1. Skapa en tuple "person" med tre värden: "Anna", 25, "Stockholm".
# 2. Packa upp tuplen i tre variabler: namn, ålder, stad (på en och samma rad).
# 3. Skriv ut variablerna för att se att de fick rätt värden.
# 4. Skapa en tuple "punkt" med två koordinater: (10, 20).
# 5. Packa upp "punkt" i två variabler: x och y.
# 6. Skriv ut "x är [x] och y är [y]".
# 7. Skapa en funktion "returnera_punkt()" som returnerar en tuple (5, 15).
# 8. Anropa funktionen och packa upp resultatet direkt i två variabler: a, b.
# 9. Skriv ut "a = [a], b = [b]".
# 10. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================


# Tuple unpacking (uppackning) innebär att du
# kan tilldela värdena i en tuple till flera variabler på en och samma rad, 
# istället för att göra det en i taget.

# === STEG 1-3: PACKA UPP EN ENKEL TUPLE ===

person = ("Anna", 25, "Stockholm") # En tupel med namn, ålder och stad

# Packa upp i tre variabler

namn, ålder, stad = person
print(f"namn = {namn}, ålder = {ålder}, stad = {stad}")



# === STEG 4-6: PACKA UPP KOORDINATER ===

punkt = (10, 20) # En tupel med x och y koordinater

x, y = punkt
print(f" x = {x}, y = {y}")

# === STEG 7-9: PACKA UPP FRÅN EN FUNKTION ===
def returnera_punkt(): # En funktion som returnerar en tupel med x och y koordinater
    return (5, 15)

a, b = returnera_punkt()
print(f" a = {a}, b = {b}")