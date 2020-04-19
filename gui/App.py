
import tkinter as tk
from tkinter import font  as tkfont
import matplotlib.pyplot as plt

<<<<<<< HEAD
=======
import numpy as np
>>>>>>> 95d7be8ce68a628b1c5648230ca6268ec23c2045

from algos.Dichotomie import *
from algos.Newton import *
from algos.Equa_Solver import *

<<<<<<< HEAD
from .ui.views.WelcomePage import *
from .ui.views.DichotomiePage import *



=======
>>>>>>> 95d7be8ce68a628b1c5648230ca6268ec23c2045

class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.resizable(width=False, height=False)
<<<<<<< HEAD
        self.geometry("883x661+477+168")
        self.title("Non Linear Equations Solver")
        self.configure(background="#000")




        container = tk.Frame(self)
        container.configure(background="#000")
        # container.place(relx=0, rely=0, relheight=1 , relwidth=1)
=======
        self.title("Systemes Non Linéaires")
        self.geometry("935x695+300+50")


        container = tk.Frame(self)
>>>>>>> 95d7be8ce68a628b1c5648230ca6268ec23c2045
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

<<<<<<< HEAD

        self.frames = {}
        for F in ( WelcomePage,DichotomiePage):
=======
        self.frames = {}
        for F in (HomePage, DichotomiePage, NewtonPage,CordesPage,FalsePosPage):
>>>>>>> 95d7be8ce68a628b1c5648230ca6268ec23c2045
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

<<<<<<< HEAD
        self.show_frame("WelcomePage")
=======
        self.show_frame("HomePage")
>>>>>>> 95d7be8ce68a628b1c5648230ca6268ec23c2045

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


<<<<<<< HEAD
# class HomePage(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="Systemes Non Lineaires " , font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#
#         btn_dicho = tk.Button(self, text="Dichotomie",
#                             command=lambda: controller.show_frame("DichotomiePage"))
#         btn_newton = tk.Button(self, text="Newton",
#                             command=lambda: controller.show_frame("NewtonPage"))
#         btn_cordes = tk.Button(self, text="Cordes",
#                             command=lambda: controller.show_frame("CordesPage"))
#         btn_falsePos = tk.Button(self, text="Fausse Position",
#                             command=lambda: controller.show_frame("FalsePosPage"))
#
#         btn_dicho.pack()
#         btn_newton.pack()
#         btn_cordes.pack()
#         btn_falsePos.pack()
#
#

#
#




# class NewtonPage(tk.Frame):
#
#     def test1(self):
#         fx = "x**2-math.cos(x)"
#         f = lambda x: eval("x**2-np.cos(x)")
#         Dfx="2*x+math.sin(x)"
#
#         equa=Newton(f=fx,df=Dfx,err=1e-8,x0=math.pi/4,max_iter=10)
#         newtonRes=Newton.solve(equa)
#         t = np.linspace(0, 2, 10)
#         drawGraph(t,f,newtonRes)
#
#     def test2(self):
#         fx = "x**3 - x**2 - 1"
#         f = lambda x: eval("x**3 -x**2 -1")
#         Dfx="3*x**2-2*x"
#         equa=Newton(f=fx,df=Dfx,err=1e-8,x0=0.75,max_iter=10)
#         newtonRes=Newton.solve(equa)
#         t = np.linspace(0, 1, 200)
#         drawGraph(t,f,newtonRes)
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="Méthode de Newton", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#
#         btntst1 = tk.Button(self, text="f(x)= x²-cos(x)",
#                            command=lambda: self.test1())
#         btntst2 = tk.Button(self, text="f(x)= x^3-x²-1",
#                            command=lambda: self.test2())
#         btntst3 = tk.Button(self, text="f(x)= cos²(2x)-x²",
#                            command=lambda: self.test1())
#
#         btntst4 = tk.Button(self, text="f(x)= cos(x)",
#                            command=lambda: self.test1())
#         btntst5 = tk.Button(self, text="f(x)= x^3-4x+1",
#                            command=lambda: self.test1())
#
#         button = tk.Button(self, text="retour",
#                            command=lambda: controller.show_frame("HomePage"))
#         btntst1.pack()
#         btntst2.pack()
#         btntst3.pack()
#         btntst4.pack()
#         btntst5.pack()
#         button.pack()
#
# class CordesPage(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="Méthode de Cordes", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#         button = tk.Button(self, text="retour",
#                            command=lambda: controller.show_frame("HomePage"))
#         button.pack()
#
# class FalsePosPage(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="Méthode de Fausse Position ", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#         button = tk.Button(self, text="retour",
#                            command=lambda: controller.show_frame("HomePage"))
#         button.pack()
=======

class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Systemes Non Lineaires " , font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        btn_dicho = tk.Button(self, text="Dichotomie",
                            command=lambda: controller.show_frame("DichotomiePage"))
        btn_newton = tk.Button(self, text="Newton",
                            command=lambda: controller.show_frame("NewtonPage"))
        btn_cordes = tk.Button(self, text="Cordes",
                            command=lambda: controller.show_frame("CordesPage"))
        btn_falsePos = tk.Button(self, text="Fausse Position",
                            command=lambda: controller.show_frame("FalsePosPage"))

        btn_dicho.pack()
        btn_newton.pack()
        btn_cordes.pack()
        btn_falsePos.pack()


def drawGraph(x,f,markers):
    fig, ax = plt.subplots()

    ax.plot(x, f(x),'m')
    ax.axhline(y=0, xmin=0.0, xmax=1.0, color='k')

    for x in markers:
        plt.scatter(x, f(x), marker='o')
        plt.pause(0.8)

    plt.ylim(bottom=-2)
    plt.show()


class DichotomiePage(tk.Frame):

    def test1(self):
        fx = "x**2-math.cos(x)"
        f = lambda x: eval("x**2-np.cos(x)")

        equa=Equa_Solver(f=fx,a=0,b=1,err=1e-15)
        dichoRes=Dichotomie.solve(equa)
        t = np.linspace(0, 1, 10)
        drawGraph(t,f,dichoRes)

    def test2(self):
        fx="x**3 - x**2 - 1"
        f = lambda x: eval(fx)

        equa=Equa_Solver(f=fx,a=1,b=2,err=1e-8)
        dichoRes=Dichotomie.solve(equa)
        t = np.linspace(1, 2, 10)
        drawGraph(t,f,dichoRes)

    def test3(self):
        fx="math.cos(2*x)**2 - x**2"
        f= lambda x:eval("np.cos(2*x)**2 - x**2")

        equa=Equa_Solver(f=fx,a=0,b=2,err=1e-8)
        dichoRes=Dichotomie.solve(equa)
        t = np.linspace(0, 2, 10)
        drawGraph(t,f,dichoRes)

    def test4(self):
        fx="math.cos(x)"
        f= lambda x:eval("np.cos(x)")

        equa=Equa_Solver(f=fx,a=0,b=2,err=1e-14)
        dichoRes=Dichotomie.solve(equa)
        t = np.linspace(0, 2, 10)
        drawGraph(t,f,dichoRes)

    def test5(self):
        fx = "x**3 - 4*x + 1"
        f = lambda x: eval("x**3 - 4*x + 1")

        equa = Equa_Solver(f=fx, a=0, b=1, err=1e-14)
        dichoRes = Dichotomie.solve(equa)
        t = np.linspace(0, 1, 10)
        drawGraph(t, f, dichoRes)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Méthode De dichotomie", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        btntst1 = tk.Button(self, text="f(x)= x²-cos(x)",
                           command=lambda: self.test1())
        btntst2 = tk.Button(self, text="f(x)= x^3-x²-1",
                           command=lambda: self.test2())
        btntst3 = tk.Button(self, text="f(x)= cos²(2x)-x²",
                           command=lambda: self.test3())

        btntst4 = tk.Button(self, text="f(x)= cos(x)",
                           command=lambda: self.test4())
        btntst5 = tk.Button(self, text="f(x)= x^3-4x+1",
                           command=lambda: self.test5())

        button = tk.Button(self, text="retour",
                           command=lambda: controller.show_frame("HomePage"))
        btntst1.pack()
        btntst2.pack()
        btntst3.pack()
        btntst4.pack()
        btntst5.pack()
        button.pack()



class NewtonPage(tk.Frame):

    def test1(self):
        fx = "x**2-math.cos(x)"
        f = lambda x: eval("x**2-np.cos(x)")
        Dfx="2*x+math.sin(x)"

        equa=Newton(f=fx,df=Dfx,err=1e-8,x0=math.pi/4,max_iter=10)
        newtonRes=Newton.solve(equa)
        t = np.linspace(0, 2, 10)
        drawGraph(t,f,newtonRes)

    def test2(self):
        fx = "x**3 - x**2 - 1"
        f = lambda x: eval("x**3 -x**2 -1")
        Dfx="3*x**2-2*x"
        equa=Newton(f=fx,df=Dfx,err=1e-8,x0=0.75,max_iter=10)
        newtonRes=Newton.solve(equa)
        t = np.linspace(0, 1, 200)
        drawGraph(t,f,newtonRes)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Méthode de Newton", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        btntst1 = tk.Button(self, text="f(x)= x²-cos(x)",
                           command=lambda: self.test1())
        btntst2 = tk.Button(self, text="f(x)= x^3-x²-1",
                           command=lambda: self.test2())
        btntst3 = tk.Button(self, text="f(x)= cos²(2x)-x²",
                           command=lambda: self.test1())

        btntst4 = tk.Button(self, text="f(x)= cos(x)",
                           command=lambda: self.test1())
        btntst5 = tk.Button(self, text="f(x)= x^3-4x+1",
                           command=lambda: self.test1())

        button = tk.Button(self, text="retour",
                           command=lambda: controller.show_frame("HomePage"))
        btntst1.pack()
        btntst2.pack()
        btntst3.pack()
        btntst4.pack()
        btntst5.pack()
        button.pack()

class CordesPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Méthode de Cordes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="retour",
                           command=lambda: controller.show_frame("HomePage"))
        button.pack()

class FalsePosPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Méthode de Fausse Position ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="retour",
                           command=lambda: controller.show_frame("HomePage"))
        button.pack()
>>>>>>> 95d7be8ce68a628b1c5648230ca6268ec23c2045
