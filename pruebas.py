#QUITAR ESPACIOS DEL PRINCIPIO, FINAL Y DE CADA ELEMENTO
valortotal=''
valores = ['  1C', ' 2s', '-3    ',  'B   ', '  -2,3', '2.1    ']
valores_limpios = [v.strip() for v in valores]  # ['1C', '2s', '-3', 'B', '-2.3', '2.1']
print(valores_limpios)

#FUNCIÓN PARA LIMPIAR LOS DATOS Y QUITAR LAS LETRAS Y SIGNOS RAROS
def limpiar(texto):
    caracteres_validos = '0123456789.-'
    resultado = ''
    for char in str(texto):
        if char in caracteres_validos:
            resultado += char
    return resultado
           
#LIMPIAR LOS VALORES LIMPIOS Y DEJAR SOLO LOS NUMEROS
datoslimpios = [limpiar(v) for v in valores_limpios]
print(datoslimpios)