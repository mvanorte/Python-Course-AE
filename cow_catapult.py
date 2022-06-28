"""This program will simulate a cow-catapult"""
import math
from matplotlib import pyplot as plt

#constants
rho_air=1.225
rho_cow=1000
dragcoef=0.7
g=9.81
dt=0.0001
#start parameters
h0=60

R=10.0
phi_stop=60*math.pi/180
l_0=0.5
k=9000.0
m=550

#h=y+h0
phi=0


#radius of the cow
volume=m/rho_cow
r=(volume/(4/3*math.pi))**(1/3)

def catapult(R, phi, phi_stop, l_0, k,m):
    x=-R
    y=0
    t=0
    a=0
    v=0

    #starting lists
    time=[]
    vlist=[]
    alist=[]
    philist=[]
    xlist=[]
    ylist=[]
    hlist=[]
    deltaxlist=[]
    F_g=-m*g
    flightpathlist=[]

    #phase 1
    while phi<phi_stop:
        #forces
        l=math.sqrt(2*(R**2)-2*(R**2)*math.cos(math.pi/2-phi))
        #l=R*math.cos(phi)/(math.sin(math.pi/4+phi/2))
        #beta=45-phi/2
        F_k=k*(l-l_0)
        F_k_tan=F_k*math.cos(math.pi/4-phi/2) 
        F_g_tan=F_g*math.cos(phi) 
        F_r_tan=F_g_tan+F_k_tan

        #motion
        t+=dt
        a=F_r_tan/m
        v+=a*dt
        phi+=(v/R)*dt
        
        #print(v)
        #xy coordinates
        vx=v*math.cos(math.pi/2-phi)
        vy=v*math.sin(math.pi/2-phi)
        
        x+=vx*dt
        y+=vy*dt
        h=y+h0
        flightpath=math.atan(vy/vx)
        delta_x=x+R
        v=math.sqrt(vx**2+vy**2)
        #lists
        time.append(t)
        alist.append(a)
        vlist.append(v)
        philist.append(phi)
        xlist.append(x)
        ylist.append(y)
        hlist.append(h)
        deltaxlist.append(delta_x)
        flightpathlist.append(flightpath)
    #print(vx)
    #print(vy)
    #print(v)

    while h>0:
        S=math.pi*r**2
        #Dx=0.5*rho_air*(vx**2)*S*dragcoef
        #Dy=0.5*rho_air*(vy**2)*S*dragcoef
        Dx=0
        Dy=0
        t+=dt
        ax=-Dx/m
        ay=-Dy/m-g
        vy+=ay*dt
        vx+=ax*dt
        x+=vx*dt
        y+=vy*dt
        h=y+h0
        #delta_x=x+R
        flightpath=math.atan(vy/vx)
        v=math.sqrt(vx**2+vy**2)
            
        time.append(t)
        alist.append(a)
        vlist.append(v)
        xlist.append(x)
        deltaxlist.append(delta_x)
        ylist.append(y)
        hlist.append(h)
        flightpathlist.append(flightpath)
                              
    
    #print(delta_x)

    return time, alist, vlist, xlist, deltaxlist, ylist, hlist, flightpathlist

time, alist, vlist, xlist, deltaxlist, ylist, hlist, flightpathlist=catapult(R, phi, phi_stop, l_0, k,m)
print(time[-1])
print(deltaxlist[-1])
print(xlist[-1])

plt.figure()
plt.subplot(2, 2, 1)
plt.title("Height vs Distance")
plt.plot(xlist, hlist)

plt.subplot(2, 2, 2)
plt.title("Distance vs Time")
plt.plot(xlist,time)

plt.subplot(2, 2, 3)
plt.title("Speed vs Time")
plt.plot(time, vlist)

plt.subplot(2,2,4)
plt.title("Flight Path Angle vs Time")
plt.plot(time,flightpathlist)

plt.show()


dk=1000
dl=0.01
dphistop=0.001

#print("ok")
while catapult(10, 0, 60*math.pi/180, 0.5, k, 550)[3][-1]<300:
    k+=dk
        
    
print("To reach 300 m the spring constant has to be: ", k, "N/m")



while catapult(10, 0, 60*math.pi/180, l_0, 9000, 550)[3][-1]<300:
    l_0+=dl

print("Or L_0 has to be: ", l_0, "m")



while catapult(10, 0, phi_stop, 0.5, 9000, 550)[3][-1]<300:
    phi_stop+=dphistop
    

phi_stop=phi_stop*180/math.pi
print("Or phi_stop has to be: ", phi_stop , "degrees")
    

