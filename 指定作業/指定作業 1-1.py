
from vpython import*

size = 0.5

scene = canvas(width=600, height=400, center=vector(2.5,0,0), background=vector(0,0,0))



x = arrow(pos=vector(0,0,0), axis=vector(20,0,0), shaftwidth=0.15, color=color.green)
y = arrow(pos=vector(0,0,0), axis=vector(0,20,0), shaftwidth=0.15, color=color.red)
z = arrow(pos=vector(0,0,0), axis=vector(0,0,20), shaftwidth=0.15, color=color.cyan)
ball = sphere(radius=size, color=color.yellow, pos=vector(0,0,0), v=vector(0,0,0))


gd = graph(title = 'x-t plot', width=600, height=400, xtitle='t', ytitle='x')
f1=gcurve(color=color.blue)


gd = graph(title = 'v-t plot', width=600, height=400, xtitle='t', ytitle='v')
f2=gcurve(color=color.blue)


gd = graph(title = 'a-t plot', width=600, height=400, xtitle='t', ytitle='a')
f3=gcurve(color=color.blue)





dt = 0.001
t = 0



while t < 6 :
    if t <= 2 :
        ball.a = vector(5.0,0,0)
        rate(1/dt)
        t = t+dt
        ball.v = ball.v + ball.a*dt
        ball.pos = ball.pos+ball.v*dt
    
        f1.plot(pos=(t,ball.pos.x))
        f2.plot(pos=(t,ball.v.x))
        f3.plot(pos=(t,ball.a.x))
    else :
        ball.a = vector(-5.0,0,0)
        rate(1/dt)
        t = t+dt
        ball.v = ball.v + ball.a*dt
        ball.pos = ball.pos+ball.v*dt
    
        f1.plot(pos=(t,ball.pos.x))
        f2.plot(pos=(t,ball.v.x))
        f3.plot(pos=(t,ball.a.x))
    if ball.v.x > 0 and ball.v.x + ball.a.x*dt < 0 :
        print('球的位置',ball.pos)
        print('時間',t)
        print('球的速度',ball.v)
print(t)

print(t)
