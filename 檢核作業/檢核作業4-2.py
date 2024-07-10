from vpython import *  #引用視覺畫套件Vpython

m1 = 2.0                   #球1質量
x1 = -20.0                  #球1X軸初位置
v1= 6.0                    #球1初速度
size1 = 2.5                 #球1大小

m2 = 2.0                   #球2質量
x2 = -5.0                   #球2X軸初位置
v2= 3.0                    #球2初速度
size2 = 2.5                 #球2大小

Force = 5.0               #彈力大小
spring_L = 5.0             #彈簧長度 
spring_k = 5.0

scene = canvas(width=1000, height=300, background=vec(0.6,0.8,0.8), center=vec(5,0,10),forward=vec(0,0,-1),range=10, fov=0.004)#設定畫面
ball1 = sphere(radius=size1, color = color.red, make_trail = True)  #設定球1
ball1.pos = vector(x1,2.5,0)             #球1位置
ball1.v = vector (v1,0,0)                        #球1的速度
v1_arrow = arrow(pos=ball1.pos,axis=ball1.v,shaftwidth=0.2*size1 ,color = color.red)

ball2 = sphere(radius=size2, color = color.blue,make_trail = True) #設定球2
ball2.pos = vector(x2,0,0)             #球2位置
ball2.v = vector (0,0,0)                        #球2的速度
v2_arrow = arrow(pos=ball2.pos,axis=ball2.v,shaftwidth=0.2*size2 ,color = color.blue)

t = 0                                            #時間
dt = 0.001                                       #單位時間

while True :
    rate(1000)
    t+=dt
    ball1.pos = ball1.pos+ball1.v*dt  #控制球1的運動
    ball2.pos = ball2.pos+ball2.v*dt  #控制球2的運動

    v1_arrow.pos = ball1.pos #球1速度向量箭頭的起始點在球1上
    v1_arrow.axis = ball1.v  #球1速度向量箭頭的長度與方向等於球1速度

    v2_arrow.pos = ball2.pos#球2速度向量箭頭的起始點在球2上
    v2_arrow.axis =ball2.v  #球1速度向量箭頭的長度與方向等於球2速度

    if mag(ball2.pos - ball1.pos) < spring_L :  #如果兩球的距離比彈簧長度短，則產生受力(加速度)
        ball1_a = -1 * norm(ball2.pos-ball1.pos) * spring_k * (spring_L - mag( ball2.pos - ball1.pos )) / m1
        ball2_a = 1 * norm(ball2.pos-ball1.pos) * spring_k * (spring_L - mag( ball2.pos - ball1.pos )) / m1
        ball1.v = ball1.v + ball1_a *dt
        ball2.v = ball2.v + ball2_a*dt

    else :                             #如果沒有，兩球的加速度均為0
        ball1_a = 0
        ball2_a = 0
    
    if t>4.0 and t< 4.1: #注意此必須在碰撞結束後才計算角度
        cos_theta = dot(ball1.v,ball2.v)/(ball1.v.mag*ball2.v.mag)
        theta = acos(cos_theta)*180/pi #將弧度改為角度
        print (theta)
