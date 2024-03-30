#Modeling the "roller coaster" potential energy trick in python using pyplot
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation

def dxdt(x,t):
    return [x[1], -3*x[0]*x[0] + 4 * x[0]]
    

def potential(x):
    return x**3 - 2 * x * x


x = np.linspace(0,3,100)
t = np.linspace(0, np.pi, 50)
x_prime, _ = odeint(dxdt, [4/3 + 0.3, 0.0], t).T
U = potential(x)


fig, axis = plt.subplots()
axis.set_xlim([min(x_prime)-1,max(x_prime)+1])
axis.set_ylim([-2,2])
plt.grid()
axis.plot(x,U)
animated_plot, = axis.plot([],[], "o", markersize=4)

def update_data(frame):
    animated_plot.set_data(x_prime[frame],potential(x_prime[frame]))
    return animated_plot,

animation = FuncAnimation(
    fig = fig,
    func = update_data,
    frames=len(t),
    interval=25
    )
animation.save("my_animation_okay.gif")
plt.show()
