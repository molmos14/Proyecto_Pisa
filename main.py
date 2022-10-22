import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    respuesta = bienvenida()
    os.system('cls' if os.name == 'nt' else 'clear')
    if respuesta != 'n' or respuesta != 'N':
        pregunta = input('\n1) Español \n2) Ciencias\n\nCuál es la materia que desea practicar? (escriba el numero): ')
        while True:
            if pregunta == '1':
                español()
                break
            elif pregunta == '2':
                ciencias()
                break
            else:
                pregunta = input('\n1) Español \n2) Ciencias\n\nCuál es la materia que desea practicar? (escriba el numero): ')
   

def bienvenida():
    print(
    '''
    Hola, bienvenido a este proyecto de alumnos del
    Tencológico de Monterrey que está echo para ayudar
    a los niños de 15 años en México a estudiar para 
    el examen PISA, el cual se necesita de cierto apoyo
    para elevar la calificacion de los niños del país, 
    ya que esta es muy baja con respecto al promedio mundial.

    Por lo que este programa está enfocado a las materias de:

        - Ciencias:
            Juego estilo jeopardy que te da puntos con base
            a las preguntas contestadas correctamente. Estas 
            aumentan con respecto a su dificultad, por lo que
            recomendamos que tengas cuidado al elegir.

        - Español:
            5 lecturas con preguntas sobre comprensión lectora
    '''
    )
    respuesta = input('A continuación escribe \'siguiente\' si deseas continuar o escribe \'n\' en caso contrario: ')
    while True:
        if respuesta == 'siguiente':
            break
        else:
            respuesta = input('Escribe \'siguiente\' si deseas continuar: ')
    return respuesta

def español():
    Resultado = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
    Has elegido español como tu primer tema de estudio.
    A continuación se mostrarán las lecturas y posteriormente 
    se pondrán las preguntas para evaluar la comprensión lectora;
    por lo que una vez que escribas siguiente, la lectura 
    desaparecerá. Al final de el quiz aparecerá 
    tu resultado final.
    ''')
    with open('/home/m0lm0s/Descargas/Code/Proyecto/Lecturas/Lectura1.txt', 'r') as f1:
        print(''.join(f1.readlines()))
        siguiente = input('\nCuando acabes de leer la lectura por favor escribe (siguiente) para pasar a las preguntas: ')
        while True:
            if siguiente == 'siguiente':
                f1.close()
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else:
                siguiente = input('\nPor favor escribe (siguiente) para pasar a las preguntas: ')

    with open('/home/m0lm0s/Descargas/Code/Proyecto/Preguntas/Preguntas1.txt', 'r') as p1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(''.join(p1.readlines()))
        Respuesta1 = input('\nDame la letra de la respuesta correcta (pregunta 1): ')
        if Respuesta1 == 'e':
            Resultado += 1
        Respuesta2 = input('\nDame la letra de la respuesta correcta (pregunta 2): ')
        if Respuesta2 == 'c':
            Resultado += 1
        Respuesta3 = input('\nDame la letra de la respuesta correcta (pregunta 3): ')
        if Respuesta3 == 'd':
            Resultado += 1
        Respuesta4 = input('\nDame la letra de la respuesta correcta (pregunta 4): ')
        if Respuesta4 == 'd':
            Resultado += 1
        p1.close()

    os.system('cls' if os.name == 'nt' else 'clear')
    with open('/home/m0lm0s/Descargas/Code/Proyecto/Lecturas/Lectura2.txt', 'r') as f2:
        print(''.join(f2.readlines()))
        siguiente = input('\nCuando acabes de leer la lectura por favor escribe (siguiente) para pasar a las preguntas: ')
        while True:
            if siguiente == 'siguiente':
                f2.close()
                break
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                siguiente = input('\nPor favor escribe (siguiente) para pasar a las preguntas: ')
    
    os.system('cls' if os.name == 'nt' else 'clear')
    with open('/home/m0lm0s/Descargas/Code/Proyecto/Preguntas/Preguntas2.txt', 'r') as p2:
        print(''.join(p2.readlines()))
        Respuesta1 = input('\nDame la letra de la respuesta correcta (pregunta 1): ')
        if Respuesta1 == 'e':
            Resultado += 1
        Respuesta2 = input('\nDame la letra de la respuesta correcta (pregunta 2): ')
        if Respuesta2 == 'c':
            Resultado += 1
        p2.close()

    os.system('cls' if os.name == 'nt' else 'clear')
    with open('/home/m0lm0s/Descargas/Code/Proyecto/Lecturas/Lectura3.txt', 'r') as f3:
        os.system('cls' if os.name == 'nt' else 'clear')
        Lectura3 = print(''.join(f3.readlines()))
        siguiente = input('\nCuando acabes de leer la lectura por favor escribe (siguiente) para pasar a las preguntas: ')
        while True:
            if siguiente == 'siguiente':
                f3.close()
                break
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                siguiente = input('\nPor favor escribe (siguiente) para pasar a las preguntas: ')

    os.system('cls' if os.name == 'nt' else 'clear')
    with open('/home/m0lm0s/Descargas/Code/Proyecto/Preguntas/Preguntas3.txt', 'r') as p3:
        Preguntas1 = print(''.join(p3.readlines()))
        Respuesta1 = input('\nDame la letra de la respuesta correcta (pregunta 1): ')
        if Respuesta1 == 'b':
            Resultado += 1
        Respuesta2 = input('\nDame la letra de la respuesta correcta (pregunta 2): ')
        if Respuesta2 == 'a':
            Resultado += 1
        Respuesta3 = input('\nDame la letra de la respuesta correcta (pregunta 3): ')
        if Respuesta3 == 'b':
            Resultado += 1
        p3.close()
        os.system('cls' if os.name == 'nt' else 'clear')

    os.system('cls' if os.name == 'nt' else 'clear')
    with open('/home/m0lm0s/Descargas/Code/Proyecto/Lecturas/Lectura4.txt', 'r') as f4:
        os.system('cls' if os.name == 'nt' else 'clear')
        Lectura1 = print(''.join(f4.readlines()))
        siguiente = input('\nCuando acabes de leer la lectura por favor escribe (siguiente) para pasar a las preguntas: ')
        while True:
            if siguiente == 'siguiente':
                f4.close()
                break
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                siguiente = input('\nPor favor escribe (siguiente) para pasar a las preguntas: ')

    os.system('cls' if os.name == 'nt' else 'clear')
    with open('/home/m0lm0s/Descargas/Code/Proyecto/Preguntas/Preguntas4.txt', 'r') as p4:
        Preguntas1 = print(''.join(p4.readlines()))
        Respuesta1 = input('\nDame la letra de la respuesta correcta (pregunta 1): ')
        if Respuesta1 == 'a':
            Resultado += 1
        Respuesta2 = input('\nDame la letra de la respuesta correcta (pregunta 2): ')
        if Respuesta2 == 'c':
            Resultado += 1
        Respuesta3 = input('\nDame la letra de la respuesta correcta (pregunta 3): ')
        if Respuesta3 == 'e':
            Resultado += 1
        Respuesta4 = input('\nDame la letra de la respuesta correcta (pregunta 3): ')
        if Respuesta4 == 'c':
            Resultado += 1
        p4.close()
        os.system('cls' if os.name == 'nt' else 'clear')

    os.system('cls' if os.name == 'nt' else 'clear')
    with open('/home/m0lm0s/Descargas/Code/Proyecto/Lecturas/Lectura5.txt', 'r') as f5:
        os.system('cls' if os.name == 'nt' else 'clear')
        Lectura1 = print(''.join(f5.readlines()))
        siguiente = input('\nCuando acabes de leer la lectura por favor escribe (siguiente) para pasar a las preguntas: ')
        while True:
            if siguiente == 'siguiente':
                f5.close()
                break
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                siguiente = input('\nPor favor escribe (siguiente) para pasar a las preguntas: ')
    
    os.system('cls' if os.name == 'nt' else 'clear')
    with open('/home/m0lm0s/Descargas/Code/Proyecto/Preguntas/Preguntas5.txt', 'r') as p5:
        Preguntas1 = print(''.join(p5.readlines()))
        Respuesta1 = input('\nDame la letra de la respuesta correcta (pregunta 1): ')
        if Respuesta1 == 'e':
            Resultado += 1
        Respuesta2 = input('\nDame la letra de la respuesta correcta (pregunta 2): ')
        if Respuesta2 == 'a':
            Resultado += 1
        Respuesta3 = input('\nDame la letra de la respuesta correcta (pregunta 3): ')
        if Respuesta3 == 'b':
            Resultado += 1
        p5.close()
        os.system('cls' if os.name == 'nt' else 'clear')

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Tu resultado es: {Resultado} correctas de 16 preguntas')

def ciencias():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('python3 /home/m0lm0s/Descargas/Code/Proyecto/Ciencias/Ciencias.py')

if __name__ == '__main__':
    main()