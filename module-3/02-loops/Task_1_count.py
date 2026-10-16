# UPPGIFT 6: RÄKNA FRÅN 1 TILL 10
# Modul: 3 | Svårighetsgrad: ⭐ (1/10)
# Krav:
# 1. Skapa en for-loop som räknar från 1 till 10
# 2. Skriv ut varje tal på en egen rad
# 3. Skapa en while-loop som räknar från 10 till 1
# 4. Skriv ut varje tal på en egen rad
# 5. Kommentera koden med # för att förklara vad varje rad gör


# === STEG 1: FOR-LOOP – RÄKNA FRÅN 1 TILL 10 ===

count = [] # Skapa en tom lista (variabel) för att lagra talen 1-10.

# range(start, stop) inkluderar start men exkluderar stop

for i in range(1,11): # Skapa en for-loop som räknar från 1 till 10 (11 är exkluderat).
    print(i) # Skriv ut varje tal på en egen rad.



# === STEG 2: WHILE-LOOP – RÄKNA FRÅN 10 TILL 1 ===

start = 10 # Skapa en variabel för att lagra startvärdet 10.

while start >= 1: # Skapa en while-loop som körs så länge count är lika med eller större än 1.
    
    start -= 1 # Minska count med 1 i varje iteration.
    print(start) # Skriv ut varje tal på en egen rad.
    
# INGÅR EJ I UPPGITFEN  - fore-loop för att räkna ner från 10 till 1

for i in range(10, 0, -1):  # 10, 9, 8, ..., 1
    print(i)
# range(start, stop, step)
# step = -1 betyder "minska med 1"