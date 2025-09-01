import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#define robot parameters

r=15 #Radius of the wheels
s=4 * r #Distance between the wheels

timeVector = np.linspace(0, 100, 10000) 

#define angular velocity
DeltaL = 2*np.ones(timeVector.shape) #Left wheel angular velocity
DeltaR = 1.4*np.ones(timeVector.shape) #Right wheel angular velocity


#pos [0] = x, post[1] = y, post[2] = theta
def diffModel(pos,t,timePoints,sC ,rC ,DeltaL_Array,DeltaR_Array):

    #value of the Delta L at the currnt time t
    DeltaL_t = np.interp(t, timePoints, DeltaL_Array)
    #value of the Delta R at the currnt time t
    DeltaR_t = np.interp(t, timePoints, DeltaR_Array)

    # x_dot
    x_dot = (0.5*rC*np.cos(pos[2]))*(DeltaL_t + DeltaR_t)
    # y_dot
    y_dot = (0.5*rC*np.sin(pos[2]))*(DeltaL_t + DeltaR_t)
    # theta_dot
    theta_dot = (rC/sC)*(DeltaL_t - DeltaR_t)

    zeta = [x_dot, y_dot, theta_dot]
    return zeta

#define the initial values for the simulation
initialState = np.array([500,500,0])

solutionArray = odeint(diffModel, initialState, timeVector, args=(timeVector,s,r,DeltaL,DeltaR))

np.save('simulationData.npy', solutionArray)
plt.plot(timeVector,solutionArray[:,0],'b',label='x')
plt.plot(timeVector,solutionArray[:,1],'r',label='y')
plt.plot(timeVector,solutionArray[:,2],'m',label='theta')
plt.xlabel('Time')
plt.ylabel('x,y,theta')
plt.legend()
plt.show()