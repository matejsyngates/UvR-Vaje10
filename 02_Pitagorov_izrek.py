from math import *

kateta1 = float(input("Vnesi dolžino prve katete v mm:"))
kateta2 = float(input("Vnesi dolžino druge katete v mm:"))

hipotenuza = float(sqrt(kateta1**2 + kateta2**2))

print("Dolžina katete je", hipotenuza, "mm.")
