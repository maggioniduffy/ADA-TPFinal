import matplotlib.pyplot as plt
import numpy as np

def plot_times(x,y):
  fig, ax = plt.subplots()
   
  y = [i * 1000 for i in y]
  ax.scatter(x, y, linewidth=2.0)
  
  ax.set(xlim=(min(x), max(x)+0.2), xticks=np.arange(min(x), max(x)+1),
       ylim=(0, max(y)+10), yticks=np.arange(1, max(y)+10,max(y)/(len(y)*3)))
  plt.grid()
  plt.xlabel("Casillas por lado (n)")
  plt.ylabel("T(n) promedio 3 corridas (milisegundos)")
  plt.show()