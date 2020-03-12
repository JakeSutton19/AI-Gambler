#Tkinter
import tkinter as tk
from tkinter import ttk


Large_Font=("Verdana",16)

class UI(tk.Tk):#inherited tk.Tk
	def __init__(self, *args,**kwargs):
		tk.Tk.__init__(self,*args,**kwargs)

		#Title
		tk.Tk.wm_title(self,"AI Gambler Program")

		container = tk.Frame(self)#always have this, frame is predef frame is edge of window
		container.pack(side="top",fill="both",expand=True)# fill is for limits you set and expand is to go beyond if needed
		container.grid_rowconfigure(0,weight=1)#0 is min value, weight specs priority
		container.grid_columnconfigure(0,weight=1)

		self.frames={}
		for F in (Start, Admin, Betting, Stats):
			frame = F(container,self)
			self.frames[F]=frame
			frame.grid(row=0,column=0,sticky="nsew")

		self.show_frame(Start)

	def show_frame(self,cont):
		frame=self.frames[cont]
		frame.tkraise()


class Start(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		label=ttk.Label(self,text="AI Gambler - Home",font=Large_Font)
		label.pack(pady=10,padx=10)

		button = ttk.Button(self,text="Admin", command=lambda: controller.show_frame(Admin))
		button.pack()

		button1=ttk.Button(self,text="Betting",command=lambda: controller.show_frame(Betting))
		button1.pack()

		button2=ttk.Button(self,text="Stats",command= lambda: controller.show_frame(Stats))
		button2.pack()

class Admin(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label=tk.Label(self,text="AI Gambler - Admin",font=Large_Font)
		label.pack(pady=10,padx=10)

		button = ttk.Button(self,text="Back", command=lambda: controller.show_frame(Start))
		button.pack()


class Betting(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label=tk.Label(self,text="AI Gambler - Betting",font=Large_Font)
		label.pack(pady=10,padx=10)

		button = ttk.Button(self,text="Back", command=lambda: controller.show_frame(Start))
		button.pack()



class Stats(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		label=ttk.Label(self,text="AI Gambler - Stats",font=Large_Font)
		label.pack(pady=10,padx=10)

		button = ttk.Button(self,text="Back", command=lambda: controller.show_frame(Start))
		button.pack()





app=UI()
app.geometry("650x500")
app.mainloop()