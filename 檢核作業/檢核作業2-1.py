from vpython import*

g = 9.8
size = 0.5
m = 1.0
height = 15
k = 0.05

scene = canvas(width=1000, height=600, x=0, y=0, center = vector(0,height,0))
floor = box(length=50, height=0.01, width=10, color=color.cyan)

ball = sphere(radius=size, color=color.yellow, pos=vector(-25,0,0), v=vector(5,10,0), make_trail=True, trail_type="points", interval=100,)
ballR = sphere(radius=size, color=color.red, pos=vector(-25,0,0), v=vector(5,10,0), make_trail=True, trail_type="points", interval=100,)
ball.a = vector(0,-g, 0)
ballR.a = vector(0, -g, 0)

dt = 0.001
t = 0.0
f = -k * ballR.v

while t<20:
    rate(1/dt)
    t += dt
    #黃球
    ball.a = vector(0,-g,0)
    ball.v = ball.v + ball.a * dt
    ball.pos = ball.pos + ball.v * dt
    #紅球
    f = -k * ballR.v
    ballR.a = vector(0, -g, 0) + f
    ballR.v = ballR.v + ballR.a * dt
    ballR.pos = ballR.pos + ballR.v * dt

    if ball.pos.y <= size and ball.v.y <0:
        ball.v.y *= -1
    if ballR.pos.y <= size and ballR.v.y <0:
        ballR.v.y *= -1