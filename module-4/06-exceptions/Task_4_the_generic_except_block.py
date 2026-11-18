# ============================================================
# UPPGIFT 69: DEN GENERISKA EXCEPT-BLOCKEN
# Modul: 4 | Svårighetsgrad: ⭐⭐⭐⭐ (4/10)
# Krav:
# 1. Skapa en lista "siffror" = [10, 5, 0, 2, "hej"].
# 2. Skapa en variabel "total" = 0.
# 3. Använd en for-loop för att loopa genom "siffror".
# 4. Inuti loopen, använd ett try-except-block:
#    - Inuti try: Dividera 100 med talet (100 / tal) och lägg till i "total".
#    - Inuti except ZeroDivisionError: Skriv ut "Kan inte dividera med noll. Hoppar över."
#    - Inuti except TypeError: Skriv ut "Fel datatyp. Hoppar över."
#    - Lägg till en generisk except (bara except:) som skriver ut "Ett okänt fel uppstod."
# 5. Skriv ut det totala värdet i slutet.
# 6. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================


# #Varför en generisk except:?
# Ibland vet vi inte exakt vilka fel som kan uppstå 
# (t.ex. om vi läser in data från en fil eller ett nätverk). 
# En generisk except: fungerar som ett "säkerhetsnät" så att programmet inte kraschar, 
# oavsett vad som händer. Men: Man bör alltid försöka fånga specifika fel först, 
# och bara använda den generiska som en sista utväg.
# Man bör alltid försöka fånga specifika fel först, och bara använda den generiska som en sista utväg
# Generiska except bör alltid vara sist och specifika först (t.ex. except TypeError)
# annars den generiska except att fånga upp alla FEL och de specifika felen
# kommer aldrig att köras


# === STEG 1 & 2: SKAPA LISTAN OCH TOTAL ===

siffror = [10, 5, 0, 2, "hej"]

total = 0



# === STEG 3-5: LOOPA OCH HANTERA FEL ===

for tal in siffror:
    try:
        total += 100 / tal # Division av 100 med talet och lägg till i total
    except ZeroDivisionError: # Hårdkodad felhantering för division med noll
        print("Kan inte dividera med noll. Hoppar över.")
    except TypeError: # Fel som uppstår vid fel datatyp (t.ex. 100 / "hej")
        print("Fel datatyp. Hoppar över.")
    except: # Default-except. Om något annat fel uppstår (en "säkerhetsnät" som fångar allt annat) 
        print("Ett okänt fel uppstod.")




# === STEG 6: SKRIV UT TOTAL ===

print("Totalen är:", total)