from tkinter import Tk, Label

def get_mouse_pos():
    label.config(text='{}, {}'.format(*root.winfo_pointerxy()))
    root.after(100, get_mouse_pos)
    
root = Tk()
color = root['bg']

#click-through
root.attributes('-transparent', color,\
                '-topmost', True,\
                '-fullscreen', True)

root.config(bg = color) #evita eventos
root.overrideredirect(1) #para hacer la ventana invisible solo dep. shell

#root.state("zoomed") #si no fs -> maximizado

label = Label(root)
label.pack()

get_mouse_pos()

root.mainloop()

