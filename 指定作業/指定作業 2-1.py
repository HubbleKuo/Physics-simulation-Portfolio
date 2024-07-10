from vpython import*

g = 9.8
m = 1.0
size = 0.5
k = 0.05

t = 0
nt = 0
dt = 0.001


scene = canvas(width=600, height=600,x=0, y=0, center = vector(0,0,0)) 
floor = box(length=20, height=0.01, width=10, color=color.blue)  	
xball = sphere(radius = size, color=color.red, make_trail= True, trail_type="points", interval=10) 	
yball = sphere(radius = size, color=color.yellow, make_trail= True, trail_type="points", interval=10) 	
zball = sphere(radius = size, color=color.green, make_trail= True, trail_type="points", interval=100) 

xball.pos = vector(-10, size, 0)
xball.v = vector(8, 15, 0)
xball.a = vector(0, -m*g, 0)

yball.pos = vector(-10, size, 0)
yball.v = vector(8, 15, 0)
yball.a = vector(0, -m*g, 0)


zball.pos = vector(-10, size, 0)
zball.v = vector(8, 15, 0)
zball.a = vector(0, -m*g, 0)


while xball.pos.y >= 0 or yball.pos.y >= 0 :
    rate(1/dt)
    
    xball.v = xball.v + xball.a*dt
    xball.pos = xball.pos + xball.v*dt
    yball.v = yball.v + yball.a*dt
    yball.v -= yball.v*k*dt
    yball.pos = yball.pos + yball.v*dt

    if xball.pos.y <= size and xball.v.y < 0 :
        xball.v = vector(0, 0, 0)
        xball.a = vector(0, 0, 0)
        t = 0
        break
    if yball.pos.y <= size and yball.v.y < 0 :
        yball.v = vector(0, 0, 0)
        yball.a = vector(0, 0, 0)       

while zball.pos.y >= size :
    rate(1/dt)
    t = t + dt

    zball.pos.x = -10 + zball.v.x * (1 - exp(-k*t))/k 
    zball.pos.y = size - g*t/k + (k*zball.v.y + g) * (1 - exp(-k*t))/k**2 
    zball.pos.z = 0
   
    



