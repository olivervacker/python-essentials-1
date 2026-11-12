# ============================================================
# UPPGIFT 40: ANALYSERA EN 2D-LISTA (TEMPERATURER)
# Modul: 3 | Svårighetsgrad: ⭐⭐⭐⭐⭐ (5/10)
# Krav:
# 1. Skapa en 2D-lista med namnet "temperaturer" som representerar 2 dagar, med 3 mätningar per dag:
#    [[12, 15, 14], [10, 11, 9]]
# 2. Skriv ut hela listan.
# 3. Skapa en variabel "total_summa" = 0.
# 4. Använd en yttre for-loop för att loopa genom dagarna (day).
# 5. Använd en inre for-loop för att loopa genom mätningarna (temp) i varje dag.
# 6. Lägg till varje temperatur i "total_summa".
# 7. Efter loopen: Räkna ut medeltemperaturen genom att dela total_summa med det totala antalet mätningar (2 dagar * 3 mätningar = 6).
# 8. Skriv ut medeltemperaturen.
# 9. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# === STEG 1 & 2: SKAPA OCH SKRIV UT LISTAN ===

temperaturer = [[12, 15, 14], [10, 11, 9]] # skapar 2 dagar och 3 mätningar i varje lista.
print(temperaturer)



# === STEG 3: SKAPA TOTAL_SUMMA ===

total_summa = 0



# === STEG 4-6: NÄSTLADE LOOPAR FÖR ATT SUMMERA ===

for day in temperaturer: # loop för att iterera över varje dag i "temperaturer". Denna yttre loop går igenom varje dag (som är en lista)

    for temp in day: # loop för att iterera över varje temperatur i "day" (varje våning). Denna inre loop går igenom varje temperatur i den dagen.
        total_summa += temp # lägg till varje temperatur till "total_summa"




# === STEG 7 & 8: BERÄKNA OCH SKRIV UT MEDELTEMPERATUREN ===
antal_mätningar = 2 * 3 # antal mätningar i varje dag (2 dagar * 3 mätningar i varje dag)
medeltemperatur = total_summa / antal_mätningar # beräkna medeltemperatur
print(f"Medeltemperaturen är: {medeltemperatur:.1f} grader") # skriv ut medeltemperatur