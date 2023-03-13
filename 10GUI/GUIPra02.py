from tkinter import *
top = Tk()

Player = ['muller', 'musiala', 'davies', 'deliht']
Club = ['madrid', 'munchen', 'manchester']
lista = Listbox(top)
listb = Listbox(top)
for item in Player:
    lista.insert(0, item)

for item in Club:
    listb.insert(0, item)

lista.pack()
listb.pack()
top.mainloop()
