# Bovada Bot 
# - written by Jacob Sutton

#--------------------------------------------------------------------- IMPORTS ---------------------------------------------------------------------#
#Imports (General)
import time
import os
import curses

#Bovada Imports
from .Bot.__init__ import *
from .controller import Controller

#Tkinter
import tkinter as tk
from tkinter import ttk


Large_Font=("Verdana",16)

class UI_Controller(tk.Tk, Controller):#inherited tk.Tk
	def __init__(self, *args,**kwargs):
		#Controller
		Controller.__init__(self)
		
		#TKINTER
		tk.Tk.__init__(self,*args,**kwargs)
		tk.Tk.wm_title(self,"AI Gambler Program")

		container = tk.Frame(self)#always have this, frame is predef frame is edge of window
		container.pack(side="top",fill="both",expand=True)# fill is for limits you set and expand is to go beyond if needed
		container.grid_rowconfigure(0,weight=1)#0 is min value, weight specs priority
		container.grid_columnconfigure(0,weight=1)

		self.frames={}
		for F in (Start, Admin, Manual_Setup, Manual_Actions, Bovada, Bovada_Betting, Bovada_Stats):
			frame = F(container,self)
			self.frames[F]=frame
			frame.grid(row=0,column=0,sticky="nsew")

		self.show_frame(Start)


	def show_frame(self,cont):
		frame=self.frames[cont]
		frame.tkraise()


	def Bovada_Quickstart(self):
		try:
			Info_Message("Starting Bovada setup..")
			#Setup
			self.Setup_Controller() #Setup controller
			self.Setup_Bovada() #Setup Bovada
			self.Setup_Live_Games() #Setup Live Games

			#Return
			Info_Message("Bovada setup complete.")
			return True 
		except:
			Error_Message("Unable to Setup Bovada_Quickstart")
			return False
		
	#Reset Bot
	def Reset(self):
		try:
			#Close Bot
			if (self.created_bot):
				self.Bot.Driver.quit()
				self.created_bot = False

			#Close DB
			if (self.connected_DB):
				self.conn.close()
				self.connected_DB = False
			Info_Message("Reset successful.")
			return True 
		except:
			Error_Message("Unable to Reset")
			return False

	#shutdown
	def QuitApp(self):
		#Close Bot
		if (self.created_bot):
			self.Bot.Driver.quit()

		#Close DB
		if (self.connected_DB):
			self.conn.close()

		#Kill Rest
		os.system("killall -9 python")

#
############## START #############
#

class Start(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		label=ttk.Label(self,text="AI Gambler - Home",font=Large_Font)
		label.pack(pady=10,padx=10)

		button1 = ttk.Button(self,text="Admin", command=lambda: controller.show_frame(Admin))
		button1.pack()

		button2=ttk.Button(self,text="Bovada",command=lambda: controller.show_frame(Bovada))
		button2.pack()

		button = ttk.Button(self,text="Exit Program", command=lambda: controller.QuitApp())
		button.pack()

#
############## ADMIN #############
#

class Admin(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label=tk.Label(self,text="AI Gambler - Admin",font=Large_Font)
		label.pack(pady=10,padx=10)

		#Bovada Setup
		button2=ttk.Button(self,text="Manual Setup",command=lambda: controller.show_frame(Manual_Setup))
		button1=ttk.Button(self,text="Manual Actions",command=lambda: controller.show_frame(Manual_Actions))
		button = ttk.Button(self,text="Back", command=lambda: controller.show_frame(Start))

		button1.pack()
		button2.pack()
		button.pack()


class Manual_Setup(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label=tk.Label(self,text="Admin - Setup",font=Large_Font)
		label.pack(pady=10,padx=10)

		#Bovada Setup
		button1=ttk.Button(self,text="Setup Controller",command=lambda: controller.Setup_Controller())
		button1.pack()

		button2=ttk.Button(self,text="Setup Bovada",command=lambda: controller.Setup_Bovada())
		button2.pack()

		button3=ttk.Button(self,text="Setup Live Games",command=lambda: controller.Setup_Live_Games())
		button3.pack()

		button = ttk.Button(self,text="Back", command=lambda: controller.show_frame(Admin))
		button.pack()


class Manual_Actions(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label=tk.Label(self,text="Admin - Actions",font=Large_Font)
		label.pack(pady=10,padx=10)

		#Bovada Setup
		button4=ttk.Button(self,text="Reset",command=lambda: controller.Reset())
		button4.pack()

		button = ttk.Button(self,text="Back", command=lambda: controller.show_frame(Admin))
		button.pack()

#
############## BOVADA #############
#

class Bovada(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label=tk.Label(self,text="AI Gambler - Bovada",font=Large_Font)
		label.pack(pady=10,padx=10)

		#Bovada Setup
		button1=ttk.Button(self,text="Start Bovada",command=lambda: controller.Bovada_Quickstart())
		button1.pack()

		#Bovada Betting
		button2 = ttk.Button(self,text="Betting", command=lambda: controller.show_frame(Bovada_Betting))
		button2.pack()

		#Bovada Stats
		button3 = ttk.Button(self,text="Stats", command=lambda: controller.show_frame(Bovada_Stats))
		button3.pack()

		button = ttk.Button(self,text="Back", command=lambda: controller.show_frame(Start))
		button.pack()

class Bovada_Betting(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label=tk.Label(self,text="Bovada - Betting",font=Large_Font)
		label.pack(pady=10,padx=10)

		#Search Button
		button2=ttk.Button(self,text="Search Live Games",command=lambda: controller.Search_for_Live_Games())
		button2.pack()

		#Show Button
		button3=ttk.Button(self,text="Show Future Games",command=lambda: controller.Show_Future_Games())
		button3.pack()

		button = ttk.Button(self,text="Back", command=lambda: controller.show_frame(Bovada))
		button.pack()


class Bovada_Stats(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		label=ttk.Label(self,text="Bovada - Stats",font=Large_Font)
		label.pack(pady=10,padx=10)

		button = ttk.Button(self,text="Back", command=lambda: controller.show_frame(Bovada))
		button.pack()



