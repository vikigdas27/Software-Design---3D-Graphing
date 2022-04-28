import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

class GraphingApp:
    def __init__(self, root=None):
        self.root = root
        self.frame = tk.Frame(self.root, width=screen_width, height=screen_height)
        self.frame.pack()
        tk.Button(self.frame,text="Start Graphing", command=self.make_graphingWindow).place(relx=0.4, rely=0.5)
        tk.Label(self.frame, text="GraphX", font=("Helvetica", 16)).place(relx=0.416, rely=0.125)
        tk.Label(self.frame, text="The Premiere 3D Graphing Calculator", font=("Helvetica", 11)).place(relx=0.25, rely=0.25)
        self.graphingPage = graphingWindow(master=self.root, app=self)

    def make_graphingWindow(self):
        self.frame.pack_forget()
        self.graphingPage.frame.pack(padx=0, pady=0)


class graphingWindow:
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
        surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
        ax.set_zlim(-1.01, 1.01)
        fig.colorbar(surf, shrink=0.5, aspect=10)
        figure_canvas.get_tk_widget().pack(side=tk.TOP, ipadx = 200, ipady= 200)  
			
        tk.Button(self.frame, text="Exit", command=self.go_back).place(relx=0.016, rely=0.025)
        tk.Label(self.frame, text="Graph Page", font=("Helvetica", 16)).place(relx=0.4, rely=0.025)
        tk.Button(self.frame,text="Equations", command=self.make_equationWindow).place(relx=0.2, rely=0.025)
        tk.Button(self.frame, text="Options", command=self.make_optionsWindow).place(relx=0.75, rely=0.025)
        tk.Button(self.frame, text="help", command=self.make_helpWindow).place(relx=0.916, rely=0.025)
        
        
        
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


class helpWindow:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master, width=screen_width, height=screen_height)
        tk.Button(self.frame, text="Exit", command=self.go_back).place(relx=0.016,rely=0.025)
        tk.Label(self.frame, text="Help", font=("Helvetica", 16)).place(relx=0.4, rely=0.025)

    def go_back(self):
        self.frame.pack_forget()
        self.app.frame.pack()


class optionsWindow:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master, width=screen_width, height=screen_height)
        tk.Button(self.frame, text="Exit", command=self.go_back).place(relx=0.016,rely=0.025)
        tk.Label(self.frame, text="Options", font=("Helvetica", 16)).place(relx=0.4, rely=0.025)

    def go_back(self):
        self.frame.pack_forget()
        self.app.frame.pack()


class equationsWindow:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master, width=screen_width, height=screen_height)
        tk.Button(self.frame, text="Exit", command=self.go_back).place(relx=0.025,rely=0.025)
        tk.Label(self.frame, text="Equations", font=("Helvetica", 16)).place(relx=0.4, rely=0.025)

    def go_back(self):
        self.frame.pack_forget()
        self.app.frame.pack()


root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f'{screen_width}x{screen_height}')

app = GraphingApp(root)
root.mainloop()
