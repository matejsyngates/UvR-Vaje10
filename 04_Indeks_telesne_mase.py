masa = float(input("Vnesite svojo telesno težo v kg:"))
visina_cm = float(input("Vnesite svojo telesno višino v cm:"))

visina_m = visina_cm / 100
indeks = float(masa / (visina_m**2))

print("Vaš indeks telesne mase znaša:", indeks)
