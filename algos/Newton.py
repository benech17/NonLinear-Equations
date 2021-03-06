
from sympy import *

from .Equa_Solver import *
from .basic_functions import *



class Newton(Equa_Solver):

    def solve_with_df(self):
        f=self.f
        Df=self.df
        max_iter=self.max_iter
        x0=self.x0
        epsilon=self.err
        x_list=[]

        fx = lambda x: eval(str(f))
        dfx = lambda x: eval(str(Df))
        print("\n\nfunction f : ", f, "\n", "Derivative f' : ", Df, "\n", "--------------------------------")

        xn = x0
        for n in range(0, max_iter):
            fxn = fx(xn)
            x_list.append(xn)
            self.affiche_info(n,xn,fxn)
            if abs(fxn) < epsilon:
                print('Found solution after', n, 'iterations.')
                print("the approximate solution is : ",x_list[-1])
                return x_list

            Dfxn = dfx(xn)

            if Dfxn == 0:
                print('Zero derivative. No solution found.')
                return None
            xn = xn - fxn / Dfxn

        print('Exceeded maximum iterations. No solution found.')
        return None

    def solve_without_df(self):
        f=self.f
        max_iter=self.max_iter
        x0=self.x0
        epsilon=self.err
        x_list=[]


        x = Symbol('x')
        fx = lambda x: eval(str(f))
        dfx = lambda x: eval(str(diff(f)))
        print("\n\nfunction f : ", f, "\n", "Derivative f' : ", diff(f), "\n", "--------------------------------")

        xn = x0

        for n in range(0, max_iter):
            fxn = fx(xn)
            x_list.append(xn)
            self.affiche_info(n, xn, fxn)
            if abs(fxn) < epsilon:
                print('Found solution after', n, 'iterations.')
                print("the approximate solution is : ",x_list[-1])
                return x_list
                
            Dfxn = dfx(xn)
            if Dfxn == 0:
                print('Zero derivative. No solution found.')
                return None
            xn = xn - fxn / Dfxn
        print('Exceeded maximum iterations. No solution found.')
        return None

    def solve(self):
        if self.df :
            return self.solve_with_df()

        return self.solve_without_df()

   