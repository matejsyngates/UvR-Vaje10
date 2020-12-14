tocke_tekmovalec1 = 0
tocke_tekmovalec2 = 0

while abs(tocke_tekmovalec1 - tocke_tekmovalec2) < 2:
    x = int(input("Tekmovalec 1, prfi faktor?"))
    y = int(input("Tekmovalec 1, drugi faktor?"))
    z = int(input("Tekmovalec 2, produkt?"))
    print("")
    if z == x*y:
        tocke_tekmovalec2 += 1

    x = int(input("Tekmovalec 2, prfi faktor?"))
    y = int(input("Tekmovalec 2, drugi faktor?"))
    z = int(input("Tekmovalec 1, produkt?"))
    print("")
    if z == x*y:
        tocke_tekmovalec1 += 1

    print("Trenutni rezultat:", tocke_tekmovalec1, ":", tocke_tekmovalec2)
    print("")

if tocke_tekmovalec1 > tocke_tekmovalec2:
    print("Bravo prvi! Drugi, cvek!!!")

else:
    print("Bravo drugi! Prvi, cvek!!!")
