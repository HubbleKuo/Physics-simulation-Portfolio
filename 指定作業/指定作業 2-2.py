from vpython import*
g = 9.8
m = 1.0
size = 1.0
k = 0.99999
height = 2.0




radians(360) == 2*pi

theta = 0
dt = 0.001
t = 0.0

scene = canvas(width=600, height=600,x=0, y=0, center = vector(0,0,0)) 
floor = box(length=20, height=0.01, width=10, color=color.blue)  	
ball = sphere(radius = size, color=color.red, make_trail= True, trail_type="curve", interval=100) 	


ball.pos = vector(0, size, 0)
vX0 = -20
vY0 = -50
ball.v = vector(vX0*sin(theta), vY0*cos(theta), 0)
Fg = vector(0, -m*g, 0)


show_angle = label(pos=vector(0,-7*size,0), box = False, height = 20, color=color.yellow)
while True :
    rate(1/dt)
    t = t + dt
    ball.a = Fg/m
    ball.v = ball.v + ball.a*dt
    ball.pos = ball.pos + ball.v*dt
    ball.v = ball.v + ball.a*dt
    show_angle.text = 'theta = %1.0f deg' %((theta/pi*180)-180)
    if ball.pos.y <= size :
        ball.make_trail = False
        print("R= %s" %(ball.pos))
        theta = theta + 3*pi/180
        ball.pos = vector(0, size, 0)
        ball.v = vector(vX0*sin(theta), vY0*cos(theta), 0)
        ball.make_trail = True
        print("T=%s" %t)
        print("theta =%s" %((theta/pi*180)-183))
            
    
    
    
