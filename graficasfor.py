from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,30*np.pi,0.0001)
plt.figure(figsize=(7,7))
def f(x,e,a):
    return (a**2)/(1+(e*np.cos((1-(3/(a**2)))*x)))
for L in np.arange(0.1,2,0.1):
    for e in np.arange(0,2,0.1):
        ll=round(L, 2)
        ee=round(e, 2)
        #plt.figure(figsize=(7,7))
        plt.plot(f(x,ee,ll)*np.cos(x),f(x,ee,ll)*np.sin(x),linewidth=0.7,label='orbita')
        plt.plot(f(x,0,ll)*np.cos(x),f(x,0,ll)*np.sin(x),linewidth=0.7,label='circulo')
        plt.scatter(0,0,s=10,color='black')
        plt.title(f'Orbitas L={ll} y e={ee}')
        #identificar  eje (x)
        plt.axvline(0,linewidth=1, color=(0,0,0))
        #identificar  eje (y)
        plt.axhline(0,linewidth=1, color=(0,0,0))
        #Nombre para los ejes
        plt.xlabel(r'$X$')
        plt.ylabel(r'$Y$')
        #Limites en los ejes
        if e >= 1:
            plt.ylim(-(ll**2), (ll**2))
            plt.xlim(-(ll**2), (ll**2)) 
        #Colocar labels
        plt.rcParams['legend.fontsize'] = 10
        plt.legend(loc="upper right")
        #Colocar malla.
        plt.grid(b=True, which='major', color=(0,0,0), linestyle='-')
        plt.minorticks_on()
        plt.grid(b=True, which='minor', color=(0.2,0.2,0.2), linestyle='-', alpha=0.2)
        plt.savefig(f'orbita{ll},{ee}.png',dpi=300)
        print('Momento angular ',ll,'Excentricidad ',ee)
        print('---------------------------------------------------------------------------------')
        print('---------------------------------------------------------------------------------')
        plt.clf()
        plt.cla()
        #plt.show()
#plt.show()
