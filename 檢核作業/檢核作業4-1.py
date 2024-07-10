from vpython import *  #引用視覺畫套件Vpython

m1 = 2.0                   #球1質量
x1 = -15.0                  #球1X軸初位置
v1= 6.0                    #球1初速度
size1 = 1.0                 #球1大小

m2 = 1.0                   #球2質量
x2 = -5.0                   #球2X軸初位置
v2= 3.0                    #球2初速度
size2 = 1.0                 #球2大小

Force = 5.0               #彈力大小
spring_L = 5.0             #彈簧長度 
spring_k = 2.0

E_total = 0
E_K = 0
E_U = 0

p_total = 0
p1 = 0
p2 = 0

scene = canvas(width=1000, height=300, background=vec(0.6,0.8,0.8), center=vec(5,0,10),forward=vec(0,0,-1),range=10, fov=0.004)#設定畫面
ball1 = sphere(radius=size1, color = color.red, make_trail = False)  #設定球1
ball1.pos = vector(x1,0,0)             #球1位置
ball1.v = vector (v1,0,0)   #球1的速度
ball1.a = vector(0,0,0)                       
v1_arrow = arrow(pos=ball1.pos,axis=ball1.v,shaftwidth=0.2*size1 ,color = color.red)

ball2 = sphere(radius=size2, color = color.blue,make_trail = False) #設定球2
ball2.pos = vector(x2,0,0)             #球2位置
ball2.v = vector (v2,0,0)                        #球2的速度
ball2.a = vector(0,0,0)    
v2_arrow = arrow(pos=ball2.pos,axis=ball2.v,shaftwidth=0.2*size2 ,color = color.blue)

spring = helix(pos=ball2.pos, radius=0.5, thickness =0.1) #畫彈簧
spring.coils = 10
spring.axis = vector(-spring_L,0,0)

t = 0                                            #時間
dt = 0.001                                       #單位時間

E_t = graph(align='left',width=333,height=300,                                 
              title='E-t', xtitle='t', ytitle='E',
              foreground=color.black,background=color.white,
              xmax=8, xmin=0, ymax=45, ymin=0)
fE_K = gcurve(color=color.purple, graph = E_t)
fE_U = gcurve(color=color.green, graph = E_t) 
fE_total = gcurve(color=color.black, graph = E_t) 

P_t = graph(align='left',width=333,height=300,                                 
              title='P-t', xtitle='t', ytitle='E',
              foreground=color.black,background=color.white,
              xmax=8, xmin=0, ymax=20, ymin=0)
fP_1 = gcurve(color=color.red, graph = P_t)
fP_2 = gcurve(color=color.blue, graph = P_t) 
fP_total = gcurve(color=color.black, graph = P_t) 

while True :
    rate(1000)
    t=t+dt

    ball1.pos = ball1.pos + ball1.v * dt
    ball2.pos = ball2.pos + ball2.v * dt

    v1_arrow.pos = ball1.pos
    v1_arrow.axis = ball1.v
    
    v2_arrow.pos = ball2.pos
    v2_arrow.axis = ball2.v

    spring.pos = ball2.pos

    E_K = 0.5 * m1 * (ball1.v.x ** 2) + 0.5 * m2 * (ball2.v.x ** 2)
    E_U = 0.5 * spring_k * (spring_L - mag(spring.axis)) ** 2
    E_total = E_K + E_U

    p1 = m1 * ball1.v.x
    p2 = m2 * ball2.v.x
    p_total = p1 + p2

    fE_K.plot(pos=(t, E_K))
    fE_U.plot(pos=(t, E_U))
    fE_total.plot(pos=(t, E_total))

    fP_1.plot(pos=(t,p1))
    fP_2.plot(pos=(t,p2))
    fP_total.plot(pos=(t,p_total))

    if mag(ball2.pos - ball1.pos) < spring_L:
        ball1.a.x = -1 * spring_k * (spring_L - (ball2.pos.x - ball1.pos.x)) / m1
        ball2.a.x = 1 * spring_k * (spring_L - (ball2.pos.x - ball1.pos.x)) / m2

        spring.axis = ball1.pos - ball2.pos
    else:
        ball1.a = vector(0, 0, 0 )
        ball2.a = vector(0, 0, 0 )
        spring.axis = vector(-spring_L,0,0)

    ball1.v = ball1.v + ball1.a * dt
    ball2.v = ball2.v + ball2.a * dt
    