# Taller4
El programa consiste en dos clases. La primera clase  cuenta con metodos para calcular derivadas los cuales son:
hacia adelante
central
diferencia extrapolada
la segunda clase cuenta con metodos para calcular ceros de una funcion. Estos los 
realiza por diferentes metodos como 
newton 
bisectriz 
extrapolacion lineal 
los cuales tambien se comparan con los metodos definidos en SCYPY 
newton-sp
brentq-sp
solve-sp
finalmente se hace un ejemplo del empleo del programa para cada clase 

~~
      #uso de la calse zeros
      z=Zeros(np.cos,'newton',0,error=1e-4,max_iter=100).zero((np.pi/2))
      print(z)
      print("***")
      #uso de la calse Derivada
      d=Derivada(np.cos,'segunda',dx=0.001).calc(np.pi)
      print (d)

~~
