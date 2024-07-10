from vpython import*

x_axis =  arrow(pos=vector(0,0,0), axis=vector(1,0,0), color=color.green)
y_axis =  arrow(pos=vector(0,0,0), axis=vector(0,1,0), color=color.red)
z_axis =  arrow(pos=vector(0,0,0), axis=vector(0,0,1), color=color.blue)

ball = sphere(radius=0.2, color=color.yellow, pos=vector(0,0,0), v=vector(3,0,0), a=vector(-2,0,0))

gdx = graph(title="x-t plot", width=600, height=400, xtitle="t", ytitle="x")
gdv = graph(title="v-t plot", width=600, height=400, xtitle="t", ytitle="v")
gda = graph(title="a-t plot", width=600, height=400, xtitle="t", ytitle="a")

fx = gcurve(color=color.blue, graph=gdx)
fv = gcurve(color=color.blue, graph=gdv)
fa = gcurve(color=color.blue, graph=gda)

t = 0.0
dt = 0.001
breakpoint = [0,0,0]

while t<=3:
    rate(1/dt)
    t += dt
    ball.v = ball.v + ball.a*dt
    ball.pos = ball.pos + ball.v*dt

    fx.plot(pos=(t,ball.pos.x))
    fv.plot(pos=(t,ball.v.x))
    fa.plot(pos=(t,ball.a.x))

    #if ball.v.x == 0.0:
        #breakpoint[0] = t
        #breakpoint[1] = ball.pos.x
        #breakpoint[2] = ball.v.x
    #浮點數的計算會出現極小誤差，算出柴會不一樣，要用不等式給他一個邏輯的門檻

    if ball.v.x > 0 and ball.v.x + ball.a.x*dt < 0:
        breakpoint[0] = t
        breakpoint[1] = ball.pos.x
        breakpoint[2] = ball.v.x

        print(breakpoint)


