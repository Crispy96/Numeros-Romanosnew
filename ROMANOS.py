simbolos = {
    'unidades': ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
    'decenas': ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    'centenas': ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
    'millares': ['', 'M', 'MM', 'MMM']

}

def validar(n):
    """
        Restricciones: n es un entero
            n > 0 
            n < 4000
    """
    if not isinstance(n, int):
        raise ValueError("{} debe ser un entero".format(n))

    if n < 0 or n > 3999:
        raise ValueError("{} debe estar entre 0 y 3999".format(n))

def a_romano(n):
    """
        Restricciones: n es un entero
            n > 0 
            n < 4000
        Descomponer n en millares, centenas, decenas y unidades
        Traducir millares, centenas, decenas y unidades
        Concatenar millares, centenas, decenas y unidades
    """
    validar(n)
    c = "{:04d}".format(n)
    
    unidades = int(c[-1])
    decenas = int(c[-2])
    centenas = int(c[-3])
    millares = int(c[-4])

    return simbolos['millares'][millares] + simbolos['centenas'][centenas] + simbolos['decenas'][decenas] + simbolos['unidades'][unidades]