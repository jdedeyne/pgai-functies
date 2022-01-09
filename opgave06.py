def cijferInGetal(cijfer, getal):
    laatsteCijfer = 0
    while getal > 0 and laatsteCijfer != cijfer:
        laatsteCijfer = getal % 10
        getal = getal // 10

    return laatsteCijfer == cijfer

def limiet(cijfer, limiet):
    for getal in range(limiet + 1):
        kwadraat = getal**2
        if cijferInGetal(cijfer, getal) and cijferInGetal(cijfer, kwadraat):
            print(getal, kwadraat)

def main():
    print(cijferInGetal(5, 126))
    limiet(3,250)

if __name__ == '__main__':
    main()