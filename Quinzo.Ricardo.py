##Nombre: Ricardo Quinzo
##Fecha: 14/06/2017

from tkinter import  *
import turtle

def funcion():
    ##Cambio de una ventana a otra
    ventana = Toplevel(root)
    frame = Frame(ventana)
    ventana.title("EJERCICIO 1")
    ventana.geometry("200x180")
    
    t = turtle.Pen()

    def Area():
        
        total1 = int(num1.get())
        total2 = (360/(int(num2.get())))
        for i in range(10):
            t.forward(total1)
            t.right(total2)
     
    ent1 = IntVar()
    ent2 = IntVar()
    etiquetan1 = Label(ventana, text="1) Largo de la figura")    
    etiquetan2 = Label(ventana, text="2) Lados de la Figura(1-5)")
    etiquetan3 = Label(ventana, text="-3 lados: triangulo")
    etiquetan4 = Label(ventana, text="-4 lados: cuadrado")
    etiquetan5 = Label(ventana, text="-5 lados: pentagono")
    etiquetan1.pack()
    num1 = Entry(ventana, textvariable = ent1)
    etiquetan2.pack()
    num2 = Entry(ventana, textvariable = ent2)
    num1.pack()
    num2.pack()
    

    etiquetan3.pack()
    etiquetan4.pack()
    etiquetan5.pack()

    area = Button(ventana, text=" INGRESE DATOS DE LA FIGURA",fg = "red", command = Area)

    area.pack()

    root.iconify()


root = Tk()
root.title("EXAMEN DE PROGRAMACION")
root.geometry("640x480")
etiqueta1 = Label(root, text="ESCUELA POLITECNICA NACIONAL",fg = "black")
etiqueta2 = Label(root, text="Examen Programacion Avanzada")
etiqueta3 = Label(root, text="2017A")
etiqueta4 = Label(root, text="Calcular el área y el perímetro de una figura geométrica de n lados, n<=5")
etiqueta5 = Label(root, text="Pulse el boton 1:")
etiqueta1.pack()
etiqueta2.pack()
etiqueta3.pack()
etiqueta4.pack()
etiqueta5.pack()
boton = Button(root, text="Ejercicio 1",fg = "red", command=funcion)
boton2 = Button(root, text="Ejercicio 2",fg = "blue", command="2")
boton.pack()
boton2.pack()
root.mainloop()                


