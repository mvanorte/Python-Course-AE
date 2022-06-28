#ISA Calculator
import math
#Troposphere
print('ISA Calculator')

#ISA constants
g0=float(9.80665)
r=float(287.0)
t0=float(288.15)   #sl
p0=float(101325.0) #sl
h0=float(0) #sl
rho0=float(1.225) #sl

#troposphere
a1=-float(0.0065)
h1=float(11000)

#tropopause
a2=float(0)
h2=float(20000)

#stratosphere1
a3=float(0.001)
h3=float(32000)

#stratosphere2
a4=float(0.0028)
h4=float(47000)

#stratopause
a5=float(0)
h5=float(51000)

#mesosphere1
a6=-float(0.0028)
h6=float(71000)

#mesosphere2
a7=float(-0.0020)
h7=float(86000)

#reference values

#troposhpere
t1=t0+a1*(h1-h0)
p1=p0*(t1/t0)**(-g0/(a1*r))

#tropopause
t2=t1+a2*(h2-h1)
p2=p1*math.exp(-g0/(r*t2)*(h2-h1))

#stratosphere1
t3=t2+a3*(h3-h2)
p3=p2*(t3/t2)**(-g0/(a3*r))

#stratosphere2
t4=t3+a4*(h4-h3)
p4=p3*(t4/t3)**(-g0/(a4*r))

#stratopause
t5=t4+a5*(h5-h4)
p5=p4*math.exp(-g0/(r*t5)*(h5-h4))

#mesosphere1
t6=t5+a6*(h6-h5)
p6=p5*(t6/t5)**(-g0/(a6*r))

#mesosphere2
t7=t6+a7*(h7-h6)
p7=p6*(t7/t6)**(-g0/(a7*r))


#unit conversion constants
ft=float(0.3048)
FL=100.0*ft
#menu
print('1:Calculate ISA for altitude in meters')
print('2:Calculate ISA for altitude in feet')
print('3:Calculate ISA for altitude in FL')

choice=int(input('Enter your choice:'))

if choice==2 :
    hinft=float(input('Enter altitude in ft:'))
    h=hinft*ft
elif choice==3:
    hinfl=float(input('Enter altitude in FL:'))
    h=hinfl*FL
else:
    h=float(input('Enter altitude [m]: '))

print('')
#Calculations Troposphere
if h<=11000:
    t=t0+a1*(h-h0)
    p=p0*(t/t0)**(-g0/(a1*r))
elif h>11000 and h<=20000:
    t=t1+a2*(h-h1)
    p=p1*math.exp(-g0/(r*t)*(h-h1))

elif h>=20000 and h<32000:
    t=t2+a3*(h-h2)
    p=p2*(t/t2)**(-g0/(a2*r))
elif h>=32000 and h<47000:
    t=t3+a4*(h-h3)
    p=p3*(t/t3)**(-g0/(a3*r))
elif h>=47000 and h<51000:
    t=t4+a5*(h-h4)
    p=p4*(t/t4)**(-g0/(a4*r))
elif h>=51000 and h<71000:
    t=t5+a6*(h-h5)
    p=p5*math.exp(-g0/(r*t)*(h-h5))
    
elif h>=71000 and h<86000:
    t=t6+a7*(h-h6)
    p=p6*(t/t6)**(-g0/(a6*r))
else:
    print("I cannot calculate above 86000")
    #t=t7+a7*(h-h7)
    #p=p7*(t/t7)**(-g0/(a7*r))
    
#output
t=round(t, 2)
tc=t-273.15
tc=round(tc,2)
p=round(p,None)
rho=p/(r*t)
rho=round(rho,4)

print('Temperature: ',t,' K (',tc,') C')
print('Pressure: ',p,'Pa (', int(p/p0*100), '% SL)')
print('Density: ', rho, 'kg/m3 (', int(rho/rho0*100),'% SL)')

    

dummy=input('Press enter to end the ISA calculator.')
