from vpython import *

size = 0.1
theta = 0.0
R = 1.0
omega = 2*pi
t = 0.0
pre_theta = theta
pre_pre_theta = pre_theta

scene = canvas(width=500, height=500, center=vector(0,0,0), background=vector(148.0/225,228.0/225,204.0/225))
ball = sphere(radius=size, color=color.blue, make_trail=True, interval = 1, retain = 900)

ball.pos = vector(R,0,0)
t = 0.0
dt = 0.001

while True:
    t += dt
    rate(1/dt)
    pre_pre_theta = pre_theta
    pre_theta = theta
    theta += omega*dt
    ball.pos = vector(R*cos(theta), R*sin(theta), 0)

    if pre_theta % (2 * pi) > pre_pre_theta % (2 * pi) and pre_theta % (2 * pi) > theta % (2 * pi):
        print('period = ', t)
        t = 0