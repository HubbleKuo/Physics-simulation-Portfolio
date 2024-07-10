from vpython import *
g = 9.8                 #重力加速度 9.8 m/s^2
size = 0.05             #球半徑 0.05 m            
L = 0.5                 #彈簧原長 0.5m
k = 10                  #彈簧力常數 10 N/m
m = 0.1                 #球質量 0.1 kg
Fg = m*vector(0,-g,0)   #球所受重力向量
K=0
Uk=0
Ug=0
TOTAL=0

def SpringForce(r,L):
    return -k*(mag(r)-L)*r/mag(r)

scene = canvas(width=600, height=600, center=vector(0, -L*0.9, 0))#設定畫面
ceiling = box(length=0.4, height=0.005, width=0.4, opacity = 0.2)#畫天花板
ball = sphere(radius = size,  color=color.yellow, make_trail = True, retain = 1000, interval=1)#畫球
spring = helix(radius=0.02, thickness =0.01)#畫彈簧

f_tot_arrow = arrow(color=color.red, shaftwidth = 0.02)
mg_arrow = arrow(color=color.yellow, shaftwidth = 0.02)
fs_arrow = arrow(color=color.white, shaftwidth = 0.02)
v_arrow = arrow(color=color.green, shaftwidth = 0.02)

f_tot_text = label(box = False, opacity = 0, height = 25, color=color.red, text='F_total')
mg_text = label(box = False, opacity = 0, height = 25, color=color.yellow, text='F_g')
fs_text = label(box = False, opacity = 0, height = 25, color=color.white, text='Fs')
v_text = label(box = False, opacity = 0, height = 25, color=color.green, text='V')

f1=graph(width=500, height=500, title='Energy check:green for K, red for Uk, blue for Ug, balck for TOTAL',xtitle='t',ytitle='energy')
f1_1=gcurve(color=color.red)
f1_2=gcurve(color=color.green)
f1_3=gcurve(color=color.blue)
f1_4=gcurve(color=color.black)      
ball.pos = vector(0, -L, 0)     #球在t=0時的位置
ball.v = vector(0, 0, 0)        #球初速
spring.pos = vector(0, 0, 0)    #彈簧頭端的位置
t = 0
dt = 0.001

while t < 2 :
    rate(1/dt)
    t = t + dt
    spring.axis = ball.pos - spring.pos           #彈簧的軸方向，由頭端指向尾端的距離向量
    ball.a = (Fg + SpringForce(spring.axis,L))/m  #球的加速度由重力和彈力所造成
    ball.v += ball.a*dt      #球的速度
    ball.pos += ball.v*dt    #球的位置

    
    f_tot_arrow.pos=vector(ball.pos.x-0.2, ball.pos.y, ball.pos.z)
    f_tot_arrow.axis=(Fg+SpringForce(spring.axis,L))/5
    mg_arrow.pos=ball.pos
    mg_arrow.axis=Fg/5
    fs_arrow.pos=ball.pos
    fs_arrow.axis=SpringForce(spring.axis,L)/5
    v_arrow.pos=vector(ball.pos.x+0.2, ball.pos.y, ball.pos.z)
    v_arrow.axis=ball.v/5


    v_text.pos = v_arrow.pos + v_arrow.axis*1.2
    f_tot_text.pos = f_tot_arrow.pos + f_tot_arrow.axis*1.2
    mg_text.pos = mg_arrow.pos + mg_arrow.axis*1.2
    fs_text.pos = fs_arrow.pos + fs_arrow.axis*1.2

    Ug = m*g*(ball.pos.y+L)
    Uk = 0.5*k*(mag(spring.axis)-L)**2
    K = 0.5*m*mag(ball.v)**2
    TOTAL = Ug + Uk + K

    f1_1.plot(pos=(t,Uk))
    f1_2.plot(pos=(t,K))
    f1_3.plot(pos=(t,Ug))
    f1_4.plot(pos=(t,TOTAL))     
