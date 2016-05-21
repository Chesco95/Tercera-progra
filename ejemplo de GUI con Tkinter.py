
from tkinter import *
import tkinter.messagebox
def ventana():
    
    

    ##Crear ventana
    root= Tk()
    label=Label(root,text="Hola Mundo")
    label.pack()
    root.mainloop()

def ventana2():
    
    root= Tk()
    topframe= Frame(root)
    topframe.pack()
    bottomframe= Frame(root)
    bottomframe.pack(side=BOTTOM)

    boton1= Button(topframe,text="Presione aqui para el boton1",fg="red")
    boton2= Button(topframe,text="Presione aqui para el boton2",fg="blue")
    boton3= Button(topframe,text="Presione aqui para el boton3",fg="green")
    boton4= Button(bottomframe,text="Presione aqui para el boton4",fg="purple")

    boton1.pack(side=LEFT)
    boton2.pack(side=LEFT)
    boton3.pack(side=LEFT)
    boton4.pack(side=BOTTOM)
    

def ventana3():
    root= Tk()

    one=Label(root,text= "Uno",bg= "red",fg= "white")
    one.pack()
    two=Label(root,text= "Dos",bg= "green",fg= "black")
    two.pack(fill=X)
    three=Label(root,text= "Tres",bg= "blue",fg= "white")
    three.pack(side=LEFT,fill=Y)

    root.mainloop()

def ventana4():
#Grid layout
    root= Tk()
    label_1= Label(root,text="Nombre",)
    label_2= Label(root,text="Contraseña")
    ##entrada
 

    entrada=Entry(root,textvariable=)
    entrada1=Entry(root)
    ##acomodar con filas y columnas:
    label_1.grid(row=0,sticky=E)
    label_2.grid(row=1,sticky=E)
    entrada.grid(row=0,column=1,)
    entrada1.grid(row=1,column=1)
##    c.grid(columnspan=2)
##  Conseguir el valor de la entrada
    ingresar= Button(root,text= "Ingresar",command= contenido(entrada))
    ingresar.grid(row=3)


def contenido(entrada):
    nombre= entrada.get()
    print(nombre)
    

def ventana5():
    ##Conecta una funcion a un boton
    root= Tk()
    boton1=Button(root,text="Presione para imprimir su nombre",command=printname)
    boton1.pack()

    root.mainloop()

def ventana6():
    ##Conecta una funcion a un boton, segunda forma
    root= Tk()
    boton1=Button(root,text="Presione para imprimir su nombre")
    boton1.bind("<Button-1>",printname)
    boton1.pack()

    root.mainloop()
def ventana6():
    root=Tk()



    frame=Frame(root,width=300,height=250)
    frame.bind("<Button-1>",leftClick)
    frame.bind("<Button-2>",middleClick)
    frame.bind("<Button-3>",rightClick)
    frame.pack()
    


    root.multiloop()
    



def printname():
    print("Hola me llamo jose")

def printname2(event):
    print("Hola me llamo jose")

def leftClick(event):
    print("Left")
def rightClick(event):
    print("Right")
def middleClick(event):
    print("Middle")

def al_presionar(entrada):
    print(entrada.get())





