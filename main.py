import tkinter as tk


class GraphingApp:
    def __init__(self, root=None):
        self.root = root
        self.frame = tk.Frame(self.root, width=600, height=400)
        self.frame.pack()
        tk.Button(self.frame,text="Start Graphing", command=self.make_graphingWindow).place(x=240, y=200)
        tk.Label(self.frame, text="GraphX", font=("Helvetica", 16)).place(x=250, y=50)
        tk.Label(self.frame, text="The Premiere 3D Graphing Calculator", font=("Helvetica", 11)).place(x=150, y=100)
        self.graphingPage = graphingWindow(master=self.root, app=self)

    def make_graphingWindow(self):
        self.frame.pack_forget()
        self.graphingPage.frame.pack()


class graphingWindow:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master, width=600, height=400)
        tk.Button(self.frame, text="Exit", command=self.go_back).place(x=10, y=10)
        tk.Label(self.frame, text="Graph Page", font=("Helvetica", 16)).place(x=240, y=10)
        tk.Button(self.frame,text="equations", command=self.make_equationWindow).place(x=350, y=10)
        tk.Button(self.frame, text="options", command=self.make_optionsWindow).place(x=450, y=10)
        tk.Button(self.frame, text="help", command=self.make_helpWindow).place(x=550, y=10)

        self.equationPage = equationsWindow(master=self.master, app=self)
        self.optionsPage = optionsWindow(master=self.master, app=self)
        self.helpPage = helpWindow(master=self.master, app=self)

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
        self.frame = tk.Frame(self.master, width=600, height=400)
        tk.Button(self.frame, text="Exit", command=self.go_back).place(x=10,y=10)
        tk.Label(self.frame, text="Help", font=("Helvetica", 16)).place(x=240, y=10)

    def go_back(self):
        self.frame.pack_forget()
        self.app.frame.pack()


class optionsWindow:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master, width=600, height=400)
        tk.Button(self.frame, text="Exit", command=self.go_back).place(x=10,y=10)
        tk.Label(self.frame, text="Options", font=("Helvetica", 16)).place(x=240, y=10)

    def go_back(self):
        self.frame.pack_forget()
        self.app.frame.pack()


class equationsWindow:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master, width=600, height=400)
        tk.Button(self.frame, text="Exit", command=self.go_back).place(x=10,y=10)
        tk.Label(self.frame, text="Equations", font=("Helvetica", 16)).place(x=240, y=10)

    def go_back(self):
        self.frame.pack_forget()
        self.app.frame.pack()


root = tk.Tk()
app = GraphingApp(root)
root.mainloop()
