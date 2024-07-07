def tipo_renta(renta):
    if renta < 10000:
        return 5
    elif 10000 <= renta <= 20000:
        return 15
    elif 20000 < renta <= 35000:
        return 20
    elif 35000 < renta <= 60000:
        return 30
    else:
        return 45

if "__main__" == __name__:
    renta1 = 10005
    renta2 = 34000
    renta3 = 60000
    renta4 = 60400
    renta5 = 9500

print(tipo_renta(renta1))
print(tipo_renta(renta2))
print(tipo_renta(renta3))
print(tipo_renta(renta4))
print(tipo_renta(renta5))
