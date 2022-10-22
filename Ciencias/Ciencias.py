import os


#Función limpia pantalla
def limpia():
    '''
'''
    pass

    print(limpia.__doc__)
    
    if os.name == 'nt':
        os.system('cls') 
    else:  
        os.system('clear')
        

#Función que muestra las instrucciones
def instrucciones():
    '''
    '''

    instrucciones = '''
    Bienvenido al juego de Ciencias, este juego tiene la como finalidad ayudar a los estudiantes
    a mejorar sus conocimientos en áreas de ciencia como Biología, Geografía, Física y Química.
    Durante el juego puedes equivocarte hasta 3 veces, si contestas bien 10 o más preguntas
    ganas el juego. ¡Mucho éxito y que lo disfrutes!
    
    ***Nota: No eligas la misma pregunta dos veces ya que puedes alterar tus resultados
    '''
    
    print(instrucciones)
    
print(instrucciones.__doc__)
    
#Función que crea la matriz
def crearMatriz():
    '''
    '''
    print(crearMatriz.__doc__)
    
    contador = 0
    matriz=[]
    renglon = ['1) Biología ',  ' 2) Geografía ', ' 3) Física ', ' 4) Química ']
    matriz.append(renglon)
    for r in range (len(renglon)-1):
        linea = []
        contador = contador + 1
        linea.append(contador)
        for c in range(3):
            linea.append(contador)
        matriz.append(linea)
    tabla(matriz)
    return matriz


 
#Función que da formato de tabla a la matriz
def tabla(m):
    '''
    '''
    print(tabla.__doc__)
    
    for renglonn in m:
        print("|", end="")
        for elemento in renglonn:
            print(f'{elemento}'.center(31), end="")
            print("|", end="")
        print('\n'+"--------"*16)

    
#Funcion que muestra las preguntas y valida respuestas    
def muestraPreguntas(m):
    '''
    '''
    print(muestraPreguntas.__doc__)
    
    buenas = 0
    malas = 0
    
    pregBio = open("/home/m0lm0s/Descargas/Code/Proyecto/Ciencias/biologia.txt", "r")
    pregGeo = open("/home/m0lm0s/Descargas/Code/Proyecto/Ciencias/geografia.txt", "r")
    pregFis = open("/home/m0lm0s/Descargas/Code/Proyecto/Ciencias/fisica.txt", "r")
    pregQui = open("/home/m0lm0s/Descargas/Code/Proyecto/Ciencias/quimica.txt", "r")
    
    resBio = open("/home/m0lm0s/Descargas/Code/Proyecto/Ciencias/biologiaRes.txt", "r")
    resGeo = open("/home/m0lm0s/Descargas/Code/Proyecto/Ciencias/geografiaRes.txt", "r")
    resFis = open("/home/m0lm0s/Descargas/Code/Proyecto/Ciencias/fisicaRes.txt", "r")
    resQui = open("/home/m0lm0s/Descargas/Code/Proyecto/Ciencias/quimicaRes.txt", "r")
    
    categoria = (input('¿De qué categoría quieres la pregunta?: '))
    pregunta = (input('¿Qué pregunta quieres?: '))

    while not categoria.isdigit():
        print('Por favor escribe la categoría en solo números en dígito')
        categoria = (input('¿De qué categoría quieres la pregunta?: '))
        
    while not pregunta.isdigit():
        print('Por favor escribe la pregunta en solo números en dígito')
        pregunta = (input('¿Qué pregunta quieres?: '))
        
    categoria = int(categoria)
    pregunta = int(pregunta)

    limpia()

    if 0 < categoria < 5:
        if 0 < pregunta < 5:

            if categoria == 1:
                m[pregunta][categoria-1] = ((pregBio.readlines())[pregunta-1].replace("\n", "")) 
                tabla(m)
                respuesta1 = input('Ingresa tu respuesta (minúsculas): ')
                
                if respuesta1 == ((resBio.readlines())[pregunta-1].replace("\n", "")):
                    m[pregunta][categoria-1] = '\u2713'
                    buenas += 1

                else:
                    m[pregunta][categoria-1] = '\u274c'
                    malas += 1
                tabla(m)
                
                
            elif categoria == 2:
                m[pregunta][categoria-1] = ((pregGeo.readlines())[pregunta-1].replace("\n", ""))
                tabla(m)
                respuesta2 = input('Ingresa tu respuesta (minúsculas y dígitos): ')
                
                if respuesta2 == ((resGeo.readlines())[pregunta-1].replace("\n", "")):
                    m[pregunta][categoria-1] = '\u2713'
                    buenas += 1
                    
                else:
                    m[pregunta][categoria-1] = '\u274c'
                    malas += 1
                tabla(m)
                
            elif categoria == 3:
                m[pregunta][categoria-1] = ((pregFis.readlines())[pregunta-1].replace("\n", ""))
                tabla(m)
                respuesta3 = input('Ingresa tu respuesta (minúsculas y dígitos): ')
                
                if respuesta3 == ((resFis.readlines())[pregunta-1].replace("\n", "")):
                    m[pregunta][categoria-1] = '\u2713'
                    buenas += 1

                else:
                    m[pregunta][categoria-1] = '\u274c'
                    malas += 1
                tabla(m)
                
            elif categoria == 4:
                m[pregunta][categoria-1] = ((pregQui.readlines())[pregunta-1].replace("\n", ""))
                tabla(m)
                respuesta4 = input('Ingresa tu respuesta (minúsculas): ')
                
                if respuesta4 == ((resQui.readlines())[pregunta-1].replace("\n", "")):
                    m[pregunta][categoria-1] = '\u2713'
                    buenas += 1
                    
                else:
                    m[pregunta][categoria-1] = '\u274c'
                    malas += 1
                tabla(m)
            
        else:
           print("Número de pregunta inválido. Escribe una pregunta entre 1 y 4") 
    else:
        print("Categoría inválida. Escribe una categoría entre 1 y 3")
    
    return [buenas, malas]


#Función que corre el juego
def jugar():
    '''
    '''
    print(jugar.__doc__)
    
    puntos = []
    buenas = 0
    malas = 0
    instrucciones()
    m = crearMatriz()
    while True:
        puntos = muestraPreguntas(m)
        buenas += puntos[0]
        malas += puntos[1]
        if malas >= 3:
            print("Perdiste tus 3 intentos, vuelve a intentar.")
            break
        elif buenas >= 10 and malas < 3:
            print("¡Felicidades! Has ganado")
            break


#Función que repite el programa
def main():
    '''
    '''
    print(main.__doc__)
    
    res = "si"
    while res == "si" or res == "SI" or res == "Si":
        jugar()
        res = input("¿Deseas jugar de nuevo? (si/no): ")
    print("Vuelve pronto")
    

if __name__ == '__main__':
    main()