import matplotlib.pyplot as plt
import numpy as np
import math

def plot_times(x,y):
  fig, ax = plt.subplots()
   
  y = [i * 1000 for i in y]
  ax.scatter(x, y, linewidth=2.0)
  for i in range(0,len(y)):
    ax.annotate(round(y[i],3), (x[i], y[i]))
  ax.set(xlim=(min(x), max(x)+0.2), xticks=np.arange(min(x), max(x)+1),
       ylim=(0, max(y)+400), yticks=np.arange(1, max(y),max(y)/(len(y))))
  plt.grid()
  plt.xlabel("Casillas por lado (n)")
  plt.ylabel("T(n) promedio 3 corridas (milisegundos)")
  plt.show()
  
def plot_errors(x,y):
  print(x)
  x = np.array(x)
  y = np.array(y)
  y_errs = []

  y_medias = [ np.mean(y[i]) for i in range(0,len(y))]
  for i in range(0,len(y_medias)):
    err_t = 0
    for j in y[i]:
      err = np.abs(y_medias[i]-j)
      err_t += err
    err_m = err_t/len(y[0])
    y_errs.append(err_m)
  fig, ax = plt.subplots()
  ax.errorbar(x, y_medias, y_errs, fmt='o', linewidth=2, capsize=10)
  for i in range(0,len(y)):
    st = str(round(y_medias[i],2)) + " \n EMA: " + str(round(y_errs[i],2))
    ax.annotate(st, (x[i], y_medias[i]))
  ax.set(xlim=(min(x)-1, max(x)+1), xticks=np.arange(min(x), max(x)+1),
       ylim=(0, np.max(y)+200), yticks=np.arange(1, np.max(y), np.max(y)/len(y)))
  plt.grid()
  plt.xlabel("Celdas por lado (n)")
  plt.ylabel("T(n) promedio en ms")
  plt.show()