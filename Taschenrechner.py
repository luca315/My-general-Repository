# Frage nach der ersten Zahl
zahl1 = float(input("Gib die erste Zahl ein: "))

# Frage nach der zweiten Zahl
zahl2 = float(input("Gib die zweite Zahl ein: "))

# Berechnungen
summe = zahl1 + zahl2 
differrenz = zahl1 - zahl2 
produkt = zahl1 * zahl2
quotient = zahl1 / zahl2 if zahl2 != 0 else "Unedlich (Division durch Null)"

# Ergebnisse ausgeben
print(f"Die Summe von {zahl1} und {zahl2} ist {summe}.")
print(f"Die Differenz von {zahl1} und {zahl2} ist {differrenz}.")
print(f"Das Produkt von {zahl1} und {zahl2} ist {produkt}.")
print(f"Der Quotient von {zahl1} und {zahl2} ist {quotient}.")

