from vpython import *
g = 9.8                 #重力加速度 9.8 m/s^2
size = 0.05             #球半徑 0.05 m            
L = 0.5                 #彈簧原長 0.5m
k = 100000              #彈簧力常數 100000 N/m
m = 0.1                 #球質量 0.1 kg
theta = 30 * pi/180     #初始擺角
Fg = m*vector(0,-g,0)   #球所受重力向量

def SpringForce(r,L):
    return -k*(mag(r)-L)*r/mag(r)

scene = canvas(width=600, height=600, center=vector(0, -L*0.8, 0), range=1.2*L)#設定畫面
ceiling = box(length=0.4, height=0.005, width=0.4, opacity = 0.2)#畫天花板
ball1 = sphere(radius = size,  color=color.yellow, make_trail = True, retain = 1000, interval=1)#畫球
rod1 = cylinder(radius=size/10)#畫棒子
ball2 = sphere(radius = size,  color=color.green, make_trail = True, retain = 1000, interval=1)#畫球
rod2 = cylinder(radius=size/10)#畫棒子
	
ball1.pos = vector(L, 0, 0)   #球的初始位置
ball1.v = vector(0, 0, 0)                            #球初速
rod1.pos = vector(0, 0, 0)#棒子頭端的位置

ball2.pos = vector(2*L, 0, 0)   #球的初始位置
ball2.v = vector(0, 0, 0)                            #球初速
rod2.pos = vector(L, 0, 0)     

f1 = graph(width=500, height=500, title = 'E plot', xtitle = 't' )
f1_1 = gcurve(color=color.red)
f1_2 = gcurve(color=color.green)
f1_3 = gcurve(color=color.blue)

dt = 0.001    #時間間隔
t = 0.0       #初始時間


while True:
    rate(1/dt)

    rod1.axis = ball1.pos - rod1.pos#桿子的軸方向：由桿子頭端指向尾端的向量
    rod2.pos = ball1.pos
    rod2.axis = ball2.pos - ball1.pos

    ball1.a = (Fg + SpringForce(rod1.axis,L) - SpringForce(rod2.axis,L) )/m    #牛頓第二定律：加速度＝合力/質量
    ball1.v += ball1.a*dt
    ball1.pos += ball1.v*dt

    ball2.a = (Fg + SpringForce(rod2.axis,L) )/m
    ball2.v += ball2.a*dt
    ball2.pos += ball2.v*dt

    t += dt

    E1 = (m*g*ball1.pos.y) + (0.5*k*(mag(rod1.axis)-L)**2) + (0.5*m*mag(ball1.v)**2)
    E2 = (m*g*ball2.pos.y) + (0.5*k*(mag(rod2.axis)-L)**2) + (0.5*m*mag(ball2.v)**2)
    E_total =E1 + E2 

    f1_1.plot(pos=(t, E1))
    f1_2.plot(pos=(t, E2))
    f1_3.plot(pos=(t, E_total) )
   
