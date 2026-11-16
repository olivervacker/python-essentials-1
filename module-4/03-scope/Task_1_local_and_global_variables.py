# ============================================================
# UPPGIFT 50: LOKALA OCH GLOBALA VARIABLER
# Modul: 4 | Svårighetsgrad: ⭐ (1/10)
# Krav:
# 1. Skapa en global variabel "global_x" och sätt den till 10.
# 2. Skapa en funktion "test_scope()" utan parametrar.
# 3. Inuti funktionen:
#    - Skapa en lokal variabel "lokal_y" och sätt den till 20.
#    - Skriv ut både "global_x" och "lokal_y".
# 4. Anropa funktionen.
# 5. Skriv ut "global_x" utanför funktionen.
# 6. Försök att skriva ut "lokal_y" utanför funktionen.
#    (Detta kommer att ge ett NameError, vilket är meningen!).
# 7. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================


# Scope (omfattning) bestämmer var i koden en variabel är synlig. 
# Tänk dig att variabler har olika "rum" där de bor
# Globala variabler bor i det stora "vardagsrummet" – alla kan se dem
# Lokala variabler bor i ett "låst rum" inuti en funktion – bara koden inuti funktionen kan se dem


# === STEG 1: SKAPA GLOBAL VARIABEL ===

global_x = 10 # En global variabel är en variabel som syns överallt i koden


# === STEG 2 & 3: SKAPA FUNKTIONEN ===

def test_scope():
    lokal_y = 20 # En lokal variabel är en variabel som syns bara i funktionen. Efter att funktionen har  och är klar, så "försvinner" den lokala variabel från koden. 
    print("inuti funktionen: ")
    print("global_x = ", global_x)
    print("lokal_y = ", lokal_y)



# === STEG 4: ANROPA FUNKTIONEN ===

print(test_scope())



# === STEG 5: SKRIV UT GLOBAL VARIABEL ===

print ("utanför funktionen: ")
print("global_x = ", global_x)



# === STEG 6: FÖRSÖK SKRIVA UT LOKAL VARIABEL (KOMMENTERAD) ===
# print(lokal_y) # (men kommentera ut den för att undvika krasch)