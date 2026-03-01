import sys
import re

def limpiar_valor(valor):
    """
    Limpia un valor individual:
    - Quita espacios
    - Elimina caracteres no validos
    - Retorna el numero limpio como string
    """
    if valor is None:
        return "0"

    s = str(valor).strip()
    if s == "":
        return "0"

    # Permitir un signo '-' al inicio y dígitos y un posible punto decimal
    # Eliminamos cualquier caracter que no sea dígito, signo al inicio o punto
    if s.startswith('-'):
        limpio = '-' + re.sub(r'[^0-9.]', '', s[1:])
    else:
        limpio = re.sub(r'[^0-9.]', '', s)

    # Si quedó solo '-' o vacío, retornar 0
    if limpio in ("-", "", None):
        return "0"

    return limpio

def procesar_linea(linea):
    """
    Procesa una linea completa:
    - Separa por comas
    - Limpia cada valor
    - Trunca a entero
    - Suma todos
    - Retorna el resultado
    """
    if linea is None:
        return 0

    linea = linea.strip()
    if linea == "":
        return 0

    # Separa por comas
    valores = linea.split(',')

    suma = 0
    for v in valores:
        limpio = limpiar_valor(v)

        try:
            numero_float = float(limpio)
            numero_truncado = int(numero_float)
        except ValueError:
            numero_truncado = 0

        suma += numero_truncado

    return suma

def main():
    """
    Lee de stdin linea por linea
    Procesa cada linea
    Imprime el resultado
    """
    for linea in sys.stdin:
        resultado = procesar_linea(linea)
        print(resultado)

if __name__ == "__main__":
    main()