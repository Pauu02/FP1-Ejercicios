# Escriba aquí su código
def precio_kilos(precios, fruta, kilos):
    for fruit, precio in precios.items():
        if (fruta not in precios) or (fruit == fruta and precios[fruit] == -1):
            return None
        else:
           return  precios[fruit] * kilos

def mensaje_precio_kilos(precios, fruta, kilos):
    if precio_kilos(precios, fruta, kilos) is None:
        return (f"La fruta '{fruta}' no está disponible.")
    else:
        coste = precio_kilos(precios, fruta, kilos)
        return (f"{kilos} kilos de '{fruta}' cuestan {coste:.2f} euros")

if __name__ == "__main__":
    precios_frutas = {
        "manzana": 2.5,
        "pera": 3.0,
        "banana": 1.8,
        "uva": -1  # Fruta no disponible temporalmente
    }

    fruta = "manzana"
    kilos = 3
    costo_total = precio_kilos(precios_frutas, fruta, kilos)
    print(costo_total)
    """
    # Descomentar esta parte cuando esté hecha la segunda función
    mensaje = mensaje_precio_kilos(precios_frutas, fruta, kilos)
    print(mensaje)
    """
