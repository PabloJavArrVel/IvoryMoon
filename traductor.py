import tkinter as tk
import parserIvory
import turtle



def traductor(comandos:list):
    ventana = turtle.Screen()
    tortuga = turtle.Turtle()
    tortuga.speed(1)

    # Inicializamos la tortuga
    tortuga.clear()
    tortuga.penup()
    tortuga.goto(0, 0)
    tortuga.pendown()
    tortuga.setheading(0)

    # Definimos una lista para almacenar las variables
    variables = []
    if comandos:
        print(comandos)
        for comando in comandos:
            # Separamos el comando en palabras
            palabras = comando.split()
            print(palabras)

            # Verificamos si el comando es colorFondo
            if palabras[0] == 'colorFondo':
                if palabras[1] == 'azul':
                    ventana.bgcolor('blue')
                elif palabras[1] == 'rojo':
                    ventana.bgcolor('red')
                elif palabras[1] == 'negro':
                    ventana.bgcolor('black')
                if palabras[1] == 'blanco':
                    ventana.bgcolor('white')
        
            # Verificamos si el comando es arriba
            elif palabras[0] == 'arriba':
                tortuga.setheading(90)
                tortuga.forward(int(palabras[1]))
        
            # Verificamos si el comando es abajo
            elif palabras[0] == 'abajo':
                tortuga.setheading(270)
                tortuga.forward(int(palabras[1]))
        
            # Verificamos si el comando es izquierda
            elif palabras[0] == 'izquierda':
                tortuga.setheading(180)
                tortuga.forward(int(palabras[1]))
        
            # Verificamos si el comando es derecha
            elif palabras[0] == 'derecha':
                tortuga.setheading(0)
                tortuga.forward(int(palabras[1]))
        
            # Verificamos si el comando es borrar
            elif palabras[0] == 'borrar':
                ventana.bye()
            # Verificamos si el comando es colorRGB
            elif palabras[0] == 'colorRGB':
                r = int(palabras[1])
                g = int(palabras[2])
                b = int(palabras[3])
                tortuga.pencolor(r, g, b)

            # Verificamos si el comando es colorRGB
            elif palabras[0] == 'orientar':
                tortuga.setheading(int(palabras[1]))
                print('orientado')

            # Si el comando no es uno de los anteriores, asumimos que es una variable
            else:
                nombre = palabras[0]
                valor = int(palabras[1])
                variables.append((nombre, valor))

def correr_programa():
    run_button.config(state="disabled")
    programa = input_text.get(1.0, tk.END)[:-1]
    comandos = parserIvory.parserIvory(programa)
    if isinstance(comandos,int):
        output_label.config(text=f"Error en la línea {comandos}")
    else:
        output_label.config(text=f"Programa ejecutado exitosamente")
        traductor(comandos)
    run_button.config(state="normal")


root = tk.Tk()
root.title("Traductor IvoryMoon")

input_label = tk.Label(root, text="Introduce tu programa:")
input_label.pack()

input_text = tk.Text(root, height=10)
input_text.pack()

run_button = tk.Button(root, text="Correr", bg="green", fg="green", command=correr_programa)
run_button.pack()

output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
