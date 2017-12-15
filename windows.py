from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)


raiz = Tk()

class windowsinit(object):
	def __init__(self):
		return

	def inicial (self):
		raiz.geometry("600x600")
		raiz.configure(bg = 'white')
		raiz.title('Aplicación estimación de mercados')

		ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM)
		raiz.mainloop()

	def campos (self):
		print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
		Label(master, text="First Name").grid(row=0)
		Label(master, text="Last Name").grid(row=1)

		e1 = Entry(master)
		e2 = Entry(master)

		e1.grid(row=0, column=1)
		e2.grid(row=1, column=1)

		Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
		Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

win = windowsinit()
win.inicial()
win.campos()