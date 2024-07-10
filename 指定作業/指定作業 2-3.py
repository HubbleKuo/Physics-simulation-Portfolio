from vpython import*

t = 0
dt = 0.001
size = 1.0
period_t = 0
R = 5.0
theta = 0
omega = 2*pi
back = False
pre_pre_theta = 0
pre_theta = 0
N = 20

scene = canvas(width=600, height=600,x=0, y=0, center = vector(0,0,0)) 	
ball = sphere(radius = size, color=color.yellow, pos = vector(R,0,0), make_trail= True, interval=1, retain = 900)

while True :
    rate(1/dt)
    t = t +dt
    pre_pre_theta = pre_theta
    pre_theta = theta
    theta = theta + omega*dt
    ball.pos = vector(R*cos(theta), R*sin(theta), 0)

    if pre_theta%(2*pi) > pre_pre_theta%(2*pi) > theta%(2*pi) :
        print('period= ', t)
        back = True
        period_t = t
        t = 0
    if back :
        plot_t = t%(period_t/N)
        if plot_t+dt >= period_t/N and plot_t < period_t/N :
            cylinder(radius=size/50, color=color.yellow, pos=ball.pos, axis=-ball.pos)
