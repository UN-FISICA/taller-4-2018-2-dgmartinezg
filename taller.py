
# coding: utf-8

# In[1]:


import numpy as np
from scipy import optimize

def df(self):
    return -np.sin(self)

def f(self):
    return np.cos(self)
#calculo de las derivadas y ceros 
class Derivada:
    def __init__(self, f, metodo ="adelante", dx= 0.001):
        self.f=f
        self.metodo= metodo
        self.dx=dx
    
    def calc(self,x):
        self.x=x
        if self.metodo=='adelante':
            df=(self.f(self.x+self.dx)-self.f(self.x))/self.dx
            return df
            
            
            
            
        
        elif self.metodo=='extrapolada':
            d1=float((self.f(self.x+(self.dx/2))-self.f(self.x-(self.dx/2)))/self.dx)
            d2=float((self.f(self.x+(self.dx/4))-self.f(self.x-(self.dx/4)))/(self.dx/2))
            df=(4*d1-d2)/3
            return df

     
        elif self.metodo=='central':
                df=(self.f(self.x+(self.dx/2))-self.f(self.x-(self.dx/2)))/self.dx
                return df

        elif self.metodo=='segunda':
                d2=self.f(self.x+self.dx)+self.f(self.x-self.dx)-2*self.f(self.x)
                dt2=self.dx*self.dx
                df2=d2/dt2
                return df2
                

class Zeros:
    def __init__(self,f,metodo, x1,error=1e-4,max_iter=100):
        self.x1=x1 #segundo numero del intervalo para la bisectriz
        self.f=f
        self.metodo=metodo
        self.error=error
        self.max_iter=max_iter
    def zero(self,vi):
        if self.metodo=='bisectriz':
            self.vi=vi
            xa=self.vi
            xb=self.x1
            for i in range(self.max_iter):

                f1=self.f(xa)
                f2=self.f(xb)
                if f1*f2<0:
                    c=(xa-xb)/2
                    x3=f(c)
                    #print("**",c)
                    if x3*f1<0:
                        xb=c
                    else:
                        xa=c
                if x3==0:
                    
                    break
            return print(c)

        
        elif self.metodo=='brentq-sp':
            args=()
            self.vi=vi
            
            c=optimize.brentq(self.f, self.vi ,self.x1 ,args,xtol=self.error,maxiter=self.max_iter)
            return print(c)


        elif self.metodo=='newton':
            self.vi=vi
            
            xi=vi
            for i in range(self.max_iter):
                der=-np.sin(self.vi)
                xi=xi-self.f(xi)/der
                if abs(self.f(xi))<self.error:
                    break
            return print(xi)
                
        
        elif self.metodo=='newton-sp':
            self.vi=vi
            x0=vi
            args=()
            tol=self.error
            maxiter=self.max_iter
            z = optimize.newton(f, x0 , df ,args,tol,maxiter)
            return print(z)
                
                
        elif self.metodo=='interpolacion':
            self.vi=vi
            x1=vi
            x2=self.x1
            for i in range(self.max_iter):
                x=(x1*self.f(x2)-x2*self.f(x1))/(self.f(x2)-self.f(x1))
                if abs(self.f(x))<self.error:
                    break
                elif self.f(x1)*self.f(x)<0:
                    x2=x
                else:
                    x1=x
            return print(x)

        

        elif self.metodo=='fsolve-sp':
            self.vi=vi
            x1=vi
            args=()
            y=optimize.fsolve(f,x1,args,xtol=self.error,factor=self.max_iter)
            return print(y)

        
if __name__ == "__main__":
    #uso de la calse zeros
    z=Zeros(np.cos,'newton',0,error=1e-4,max_iter=100).zero((np.pi/2))
    print(z)
    print("***")
    d=Derivada(np.cos,'segunda',dx=0.001).calc(np.pi)
    print (d)
    

