from vpython import *
from random import *
"""
1. 參數設定
"""
t = 0.0 ; t1 = 0.0  ; dt = 0.001 #時間參數
theta = 00.0 * pi / 180 #氣體入射角度
k = 9*10**9
Q_charge = 10**(-5)  #設定金原子電量
q_charge = 10 **(-8) #設定粒子電量
q_m = 10**(-3)       #設定粒子質量
d = 3.0  #氣體與牆壁距離
r = 0.50  #氣柱半徑
v0 = 2.0  # 氣體初速率
m = 0.01  #單一氣體質量
K = 5.0  #牆壁碰撞參數
per_N = 5.0 #每秒射出的粒子數
F_theory = 2*m*v0*cos(theta)*per_N  #氣體碰撞的理論平均力

"""
2. 畫面設定
"""
scene = canvas(align = 'left' , center = vec ( -0.5 , 0 , 0 ) , height=600, width=1000, range=5,auto_scale=False)  #設定畫面
Q = sphere(pos=vec(0.0,0,0),radius = 0.2 , color = color.yellow)  #設定牆壁             
q = []  #粒子的List

def Force_E(r, q):
    r1 = r - Q.pos
    return k*q*Q_charge*r1.norm()/(r1.mag*r1.mag)

"""
3. 執行迴圈
"""
while t < 30:
    rate(10000)
    t = t + dt       #時間
    t1 = t1 + dt  

    if t1 > 1/ per_N:  # 設定per_N = 100.0時，則每1/100秒會射出一顆空氣分子
        t1 = 0  
        r_dom = random()  #空氣射出的位置隨機參數
        p_dom = random() #空氣射出的角度位置參數
        q.append( sphere(pos = vector((-d*cos(theta)+r*r_dom*cos(p_dom*2*pi)*sin(theta)),(d*sin(theta)+r*r_dom*cos(p_dom*2*pi)*cos(theta)),(r*r_dom*sin(p_dom*2*pi))) , radius = 0.05, v = vec(v0*cos(theta),-v0*sin(theta),0) , Fx = 0 , visible = True , make_trail = True))
        # 每1/100秒會產生一個隨機位置的分子，以相同的速度射出
    for N in q :  #List內所有的分子撞擊牆壁時，都會受到一個-Kx的向左受力
  
        if mag(N.pos - Q.pos) >= 0.05 :  
            N.v += Force_E(N.pos, q_charge) / q_m*dt            #力改變x軸方向的速度
            N.pos += N.v*dt                              #速度控制位置             
        else:                                   #若空氣分子沒碰到牆壁時，即等速度前進
            N.pos = N.pos


        if N.pos.x > 2 :   #當空氣分子打至左側 -d*cos(theta) - 0.3位置時，使其由List消失
            N.visible = False
            N = None
