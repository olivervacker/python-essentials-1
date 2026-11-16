# ============================================================
# UPPGIFT 47: REKURSIV FIBONACCI
# Modul: 4 | Svårighetsgrad: ⭐⭐⭐ (3/10)
# Krav:
# 1. Skapa en funktion "fibonacci(n)" som tar ett heltal (n).
# 2. Funktionen ska beräkna det n:te Fibonacci-talet med hjälp av REKURSION.
#    - Kom ihåg basfallen: Fibonacci(0) = 0, Fibonacci(1) = 1.
#    - Det rekursiva anropet: Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2).
# 3. Om n är mindre än 0, returnera None (eller 0).
# 4. Använd en for-loop för att skriva ut de 10 första Fibonacci-talen (från 0 till 9).
# 5. Kommentera koden med # för att förklara vad varje rad gör.
# ============================================================

# Fibonacci-talen är en talföljd där varje tal är summan av de två föregående tal i talföljden.


# Varför två basfall?
# Fibonacci kräver att de två första talen är kända (0 och 1). 
# Om vi bara hade ett basfall (t.ex. n == 1) skulle anropet för n == 0 bli negativt och skapa problem.

# Till skillnad från fakultet (som bara anropar sig själv en gång per steg) anropar Fibonacci sig själv två gånger. 
# Detta gör att antalet anrop växer explosionsartat (exponentiellt) för stora tal. 
# Därför är rekursiv Fibonacci ganska långsam, men den är väldigt pedagogisk!



# === STEG 1, 2 & 3: SKAPA DEN REKURSIVA FUNKTIONEN ===

def fibonacci(n):
    
# Om n är mindre än 0, returnera None (eller 0)
# Två Basfall: Fibonacci(0) = 0, Fibonacci(1) = 1. Skapa en if-elif-else sats med jämförelseoperatorer som jämfört om n är lika med noll eller en.

    if n == 0: # Första Basfall: Fibonacci(0) = 0
        return 0
    elif n == 1: # Andra Basfall: Fibonacci(1) = 1
        return 1
    else:
        # Rekursiva anropet: Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)
    



# === STEG 4: SKRIV UT DE 10 FÖRSTA TALEN ===
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci(i)}")  # Anropa funktionen och skriv ut den i varje iteration.