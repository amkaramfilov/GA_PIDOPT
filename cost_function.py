import numpy as np


#todo: individuals will contain [Kp,Ti,Td,N]
def simulation(individuals,ref,A,B,C,Ts):

    Kp = np.reshape(individuals[:,0],(len(individuals),1))
    Ti = np.reshape(individuals[:,1],(len(individuals),1))
    Td = np.reshape(individuals[:,2],(len(individuals),1))
    N = np.reshape(individuals[:,3],(len(individuals),1))
    u = np.zeros([1,len(individuals)])
    uprev = np.zeros([1,len(individuals)])
    e = 0
    #uipvect = np.zeros([1,len(individuals)])
    #udpvect = np.zeros([1,len(individuals)])
    udpvect = 0
    uipvect = 0
    J = np.zeros([len(individuals),1])
    refp = 0
    yp = 0
    xvect = np.zeros([4,len(individuals)])
    xpvect =np.zeros([4,len(individuals)])
    for i in range(0,100):
        xvect = np.dot(A,xpvect)
        xvect = xvect + np.dot(B,u)
        y = np.dot(C,xvect)
        y = y.T

        xpvect = xvect
        upvect = Kp*(ref-y)
        uivect =uipvect + (Kp*Ts/Ti)*(ref-y)
        udvect =(Td/(Td+N*Ts))*udpvect + ((Kp*Td*N)/(Td+N*Ts))*(ref-refp -y +yp)
        uipvect = uivect
        udpvect = udvect

        u = (upvect+uivect+udvect).T
        yp = y
        refp = ref
        t=(i/2)**2
        deltau = (u -2).T
        e = t*((ref - y)**2) + 0.5*(deltau**2)
        J = J+e
        uprev = u
    return individuals,J

