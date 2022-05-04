import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pickle
from matplotlib import cm
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

matplotlib.use('TkAgg')

'''
Todo
Make font size relative for all labels and buttons - maybe change frame size to a default like 1080 by 1920 or smthing
we also need to set an aspect ratio 
fix location issues
fix entry 
beetter graph
'''


class GraphingApp:
		def __init__(self, root=None):
				self.root = root
				self.frame = tk.Frame(self.root,bg='white', width=screen_width, height=screen_height)
				self.frame.pack()
				tk.Button(self.frame,text="Start Graphing", bg='gray', font = ("Helvetica", int(scal/4)),command=self.make_graphingWindow).place(relx=.5, rely=.7,anchor= tk.CENTER,relheight =screen_height/(10*screen_height) , relwidth = screen_width/(5*screen_width) )
				tk.Label(self.frame, text="GraphX", bg='white', font=("Helvetica", scal)).place(relx=.5, rely=.3,anchor= tk.CENTER)
				tk.Label(self.frame, text="The Premiere 3D Graphing Calculator",bg='white', font=("Helvetica", int(scal/3))).place(relx=.5, rely=.5,anchor= tk.CENTER )
				self.graphingPage = graphingWindow(master=self.root, app=self)

				
		def make_graphingWindow(self):
				self.frame.pack_forget()
				self.graphingPage.frame.pack(padx=0, pady=0)


class graphingWindow:
		equation = ""
		equationlist = []
		temp = ""
		
		
		def __init__(self, master=None, app=None):
				self.master = master
				self.app = app
				self.frame = tk.Frame(self.master, width=screen_width, height=screen_height)
				
				self.equationPage = equationsWindow(master=self.master, app=self)
				self.optionsPage = optionsWindow(master=self.master, app=self)
				self.helpPage = helpWindow(master=self.master, app=self)
        
				fig = plt.figure(figsize=plt.figaspect(0.5))
				figure_canvas = FigureCanvasTkAgg(fig, self.frame)
				ax = fig.add_subplot(1, 2, 1, projection='3d')
				X = np.arange(-5, 5, 0.25)
				Y = np.arange(-5, 5, 0.25)
				X, Y = np.meshgrid(X, Y)
				R = np.sqrt(X**2 + Y**2)
				Z = np.sin(R)
				surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
				ax.set_zlim(-1.01, 1.01)
				fig.colorbar(surf, shrink=0.5, aspect=10)
				figure_canvas.get_tk_widget().pack(side=tk.TOP, ipadx = 200, ipady= 200)  

				tk.Label(self.frame, text="Graph Page", bg='white', font=("Helvetica", int(scal/3))).place(relx=.5, rely=.05,anchor= tk.CENTER)
			
				tk.Button(self.frame, text="Exit",font=("Helvetica", int(scal/4)), command=self.go_back).place(relx=0.025, rely=.025,relheight =screen_height/(20*screen_height) , relwidth = screen_width/(15*screen_width))
				tk.Button(self.frame,text="Equations", font=("Helvetica", int(scal/4)),command=self.make_equationWindow).place(relx=0.15, rely=.025,relheight =screen_height/(20*screen_height) , relwidth = screen_width/(8*screen_width))
				tk.Button(self.frame, text="Options", font=("Helvetica", int(scal/4)),command=self.make_optionsWindow).place(relx=0.75, rely=.025,relheight =screen_height/(20*screen_height) , relwidth =screen_width/(10*screen_width))
				tk.Button(self.frame, text="Help", font=("Helvetica", int(scal/4)),command=self.make_helpWindow).place(relx=0.9, rely=.025,relheight =screen_height/(20*screen_height) , relwidth =screen_width/(15*screen_width))
				self.word = tk.Entry(self.frame)
				self.word.place(relx=0.5, rely=0.75)
				tk.Button(self.frame, text="Save", font=("Helvetica", int(scal/4)),command=self.SaveEquation).place(relx=0.9, rely=.915,relheight =screen_height/(20*screen_height) , relwidth =screen_width/(15*screen_width))
				
				
		def go_back(self):
				self.frame.pack_forget()
				self.app.frame.pack()
				
				
		def make_equationWindow(self):
				self.frame.pack_forget()
				self.equationPage.frame.pack()
				
				
		def make_optionsWindow(self):
				self.frame.pack_forget()
				self.optionsPage.frame.pack()
				
				
		def make_helpWindow(self):
				self.frame.pack_forget()
				self.helpPage.frame.pack()
				
				
		def SaveEquation(self):
				self.equation = self.word.get()
				self.equationlist.append(self.equation)
				print(self.equationlist)
				
				for x in graphingWindow.equationlist:
						self.temp += x + '\n' 




class helpWindow:
		def __init__(self, master=None, app=None):
				self.master = master
				self.app = app
				self.frame = tk.Frame(self.master,bg='white', width=screen_width, height=screen_height)
				tk.Button(self.frame, text="Exit",font=("Helvetica", int(scal/4)), command=self.go_back).place(relx=0.025, rely=.025,relheight =screen_height/(20*screen_height) , relwidth = screen_width/(15*screen_width))
				tk.Label(self.frame, text="Help", bg='white', font=("Helvetica", int(scal/3))).place(relx=.5, rely=.05,anchor= tk.CENTER)
				
				
		def go_back(self):
				self.frame.pack_forget()
				self.app.frame.pack()
				
				
class optionsWindow:
		def __init__(self, master=None, app=None):
				self.master = master
				self.app = app
				self.frame = tk.Frame(self.master,bg='white',  width=screen_width, height=screen_height)
				tk.Button(self.frame, text="Exit",font=("Helvetica", int(scal/4)), command=self.go_back).place(relx=0.025, rely=.025,relheight =screen_height/(20*screen_height) , relwidth = screen_width/(15*screen_width))
				tk.Label(self.frame, text="Options", bg='white', font=("Helvetica", int(scal/3))).place(relx=.5, rely=.05,anchor= tk.CENTER)

				
		def go_back(self):
				self.frame.pack_forget()
				self.app.frame.pack()
				
				
class equationsWindow:
		def __init__(self, master=None, app=None):
				self.master = master
				self.app = app
				self.frame = tk.Frame(self.master,bg='white',  width=screen_width, height=screen_height)
				tk.Button(self.frame, text="Exit",font=("Helvetica", int(scal/4)), command=self.go_back).place(relx=0.025, rely=.025,relheight =screen_height/(20*screen_height) , relwidth = screen_width/(15*screen_width))
				tk.Label(self.frame, text="Equations", bg='white', font=("Helvetica", int(scal/3))).place(relx=.5, rely=.05,anchor= tk.CENTER)
				tk.Label(self.frame, text = "graphingWindow.temp", font=("Helvetica", 16)).place(relx=0.4, rely=0.2)
				
				
		def go_back(self):
				self.frame.pack_forget()
				self.app.frame.pack()
				
				
root = tk.Tk()
scal = int(root.winfo_screenwidth()/16)
if scal < 50:
		scal = 50

screen_width = 16*scal
print(screen_width)
screen_height = 9*scal
print(screen_height)
root.geometry(f'{screen_width}x{screen_height}')

app = GraphingApp(root)
root.mainloop()
