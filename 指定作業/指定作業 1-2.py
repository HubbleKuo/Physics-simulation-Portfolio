from vpython import*

size = 0.2

scene = canvas(width=600, height=400, center=vector(2.5,0,0), background=vector(0,0,0))


x = arrow(pos=vector(0,0,0), axis=vector(5,0,0), shaftwidth=0.1, color=color.cyan)
y = arrow(pos=vector(0,0,0), axis=vector(0,5,0), shaftwidth=0.1, color=color.blue)
z = arrow(pos=vector(0,0,0), axis=vector(0,0,5), shaftwidth=0.1, color=color.red)
ball = sphere(radius=size, color=color.yellow, pos=vector(0,0,0), v=vector(3.0,0,0))
ball.a = vector(-1.0,-0.5,0)

dt = 0.001
t = 0
T=0.4

while t < 5 :
    rate(1/dt)
    t = t + dt  
    plot_t = t%T
    ball.v = ball.v + ball.a*dt
    ball.pos = ball.pos+ball.v*dt
    if plot_t + dt >= T and plot_t < T: 
        arrow(pos=ball.pos, axis=ball.a, shaftwidth=0.05, color=color.red)
        arrow(pos=ball.pos, axis=ball.v, shaftwidth=0.05, color=color.green)
        sphere(radius=size, color=color.yellow, pos=ball.pos)
    if ball.v.x > 0 and ball.v.x+ball.a.x*dt < 0 :
        print('速度', ball.v)
        print('位置', ball.pos)
        print('時間', t)
 









    

    
    
