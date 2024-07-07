def es_bisiesto(año):
    if año % 4 == 0 and año % 100 != 0:
        return True
    elif año % 400 == 0:
        return True
    else:
        return False


if "__main__" == __name__:
    no_bisiesto = 2023
    bisiesto_secular = 1600
    bisiesto_no_secular = 2020

print(es_bisiesto(no_bisiesto))
print(es_bisiesto(bisiesto_secular))
print(es_bisiesto(bisiesto_no_secular))
