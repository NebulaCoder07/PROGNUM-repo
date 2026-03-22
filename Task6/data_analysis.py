import numpy as np
class Stats:
    import numpy as np
    def __init__(self,X,Y):
        import numpy as np
        
        self.X = np.asarray(X,dtype=float)
        self.Y = np.asarray(Y,dtype=float)

    def n(self):
        return self.X.size
        
    def Sx(self):
        return sum(self.X)
        
    def Sy(self):
        return sum(self.Y)

    def Sxx(self):
        return sum(self.X**2)

    def Syy(self):
        return sum(self.Y**2)

    def Sxy(self):
        return sum(self.X*self.Y)

    def deltaX(self):
        return (self.n()*self.Sxx()-self.Sx()**2)

    def deltaY(self):
        return (self.n()*self.Syy()-self.Sy()**2)

    def all_Sats(self):

        dic =  {'n':    self.n(),
                'Sx':   self.Sx(),
                'Sxx':  self.Sxx(),
                'd_x':  self.deltaX(),
                'Sy':   self.Sy(),
                'Syy':  self.Syy(),
                'd_y':  self.deltaY(),
                'Sxy':  self.Sxy()}

        return dic
        
class Pearson(Stats):

    import numpy as np
    
    def __init__(self,X,Y):
        import numpy as np
        super().__init__(X,Y)

        self.X = np.asarray(X,dtype=float)
        self.Y = np.asarray(Y,dtype=float)

        self.N = super().n()
        self.sx = super().Sx()
        self.sxx = super().Sxx()
        self.sy = super().Sy()
        self.syy = super().Syy()
        self.sxy = super().Sxy()
        self.dX = super().deltaX()
        self.dY = super().deltaY()
        
    def r_xy(self):
        import numpy as np
        
        Rx = (self.N*self.sxy - self.sx*self.sy) / np.sqrt(self.dX) / np.sqrt(self.dY)
        return Rx
    
    def b(self):
        import numpy as np
        return self.r_xy()*self.sy/self.sx

    def a(self):
        import numpy as np
        return np.mean(self.Y)-self.b()*np.mean(self.X)

    def all_Pearson(self):

        dic =  {'r_xy':  self.r_xy(),
                'b':     self.b(),
                'a':     self.a()}

        return dic

class Method_Of_Least_Squares(Stats):

    def __init__(self,X,Y):
        import numpy as np
        super().__init__(X,Y)

        self.X = np.asarray(X,dtype=float)
        self.Y = np.asarray(Y,dtype=float)
        
        self.N = super().n()
        self.sx = super().Sx()
        self.sxx = super().Sxx()
        self.sy = super().Sy()
        self.syy = super().Syy()
        self.sxy = super().Sxy()
        self.dX = super().deltaX()
        self.dY = super().deltaY()


    def b(self):
        return (self.N*self.sxy - self.sx*self.sy) / self.dX

    def a(self):
        return (self.sxx*self.sy - self.sx*self.sxy) / self.dX

    def chi_sq(self):
        return sum((self.Y-(self.a()+self.b()*self.X))**2)

    def d_b(self):
        import numpy as np
        return np.sqrt(self.N / self.dX * self.chi_sq() / (self.N-2))

    def d_a(self):
        import numpy as np
        return np.sqrt(self.sxx / self.dX * self.chi_sq() / (self.N-2))

    def all_Regress(self):

        dic =  {'b':       self.b(),
                'd_b':     self.d_b(),
                'a':       self.a(),
                'd_a':     self.d_a(),
                'chi^2':   self.chi_sq()}

        return dic
    