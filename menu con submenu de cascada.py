
##Menu
from tkinter import *
import tkinter.messagebox
def hacernada():
    print("Ok Ok no hago nada")
    
root= Tk()


menu1= Menu(root)
root.config(menu=menu1)

subMenu= Menu(menu1)
menu1.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New Project",command= hacernada)
subMenu.add_command(label= "New",command=hacernada)
subMenu.add_separator()
subMenu.add_command(label="Exit",command=hacernada)

editMenu= Menu(menu1)
menu1.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Redo",command=hacernada)

#----------

##Notificacion y pregunta

tkinter.messagebox.showinfo("Advertencia"," Hemos detectado algo")
#--------

pregunta= tkinter.messagebox.askquestion("Pregunta 1"," Desea ingresar otro producto?")
if pregunta=="yes":
    print("Respuesta igual a si")
else:
    print("Respuesta igual a no")


root.mainloop()
