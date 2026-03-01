import sys #PROGRAMA YA MODIFICADO PARA SU UTILIZACIÓN CON ARCHIVOS

def limpiar_valor(valor):
    """
    Limpia un valor individual:
    - Quita espacios
    - Elimina caracteres no válidos
    - Retorna el numero limpio como string
    """
    caracteres_validos = '0123456789.-'
    valor_str = str(valor).strip()
    resultado = ''
    for ch in valor_str:
        if ch in caracteres_validos:
            resultado += ch
    return resultado

def procesar_linea(linea):
    """
    Procesa una linea completa:
    - Divide por comas (si existen)
    - Limpia cada valor
    - Convierte a entero truncando
    - Suma todos los enteros
    - Retorna el total (int)
    """
    linea = linea.strip()
    if not linea:
        return 0

    partes = [p for p in linea.split(',')] 
    total = 0
    for p in partes:
        limpio = limpiar_valor(p)
        if limpio == '' or limpio == '-' or limpio == '.':
            continue
        try:
            numero = int(float(limpio))  # truncar decimales
            total += numero
        except ValueError:
            pass
    return total

def main():
    """
    Lee de stdin o archivo redirigido linea por linea
    Procesa cada linea y imprime el resultado
    """
    for linea in sys.stdin:
        resultado = procesar_linea(linea)
        print(resultado)

if __name__ == "__main__":
    main()