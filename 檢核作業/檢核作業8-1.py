from vpython import*
import numpy as np
N = 50		#質點個數
g = 9.8		#重力加速度
size, m, k, d = 0.016, 0.1/N, N*1000.0, 2.0/N    #球大小、質點質量、各力常數、間距
t, dt = 0, 0.0001                                #初始時間、時間間隔

scene = canvas(width=1200, height = 600, center = vector(d*N/2.0*0.9, 0, 0)) 
balls = [sphere(radius=size, color=color.yellow) for i in range(N)]
springs = [helix(radius = size/2.0, thickness = size/5.0) for i in range(N-1)]


ball_pos, ball_v, ball_g = np.zeros((N, 3)), np.zeros((N,3)), np.zeros((N,3))
#以array建立初位置、初速度、重力加速度，全為0的N列3行的陣列

#print(type(balls))

for i in range(N):
    ball_pos[i][0] = d*i*0.9 #將球沿x方向的初位置，沿axis=0擺入pos array，並使兩端點距離為0.9倍繩子全長
    ball_pos[i][1] = d*i*0.2
    ball_g[i][1] = -g        #將重力加速度陣列的第2行改為-9.8，表示每個球在y方向受到的重力場

center_of_gravity = np.sum(ball_pos, axis = 0) / 50
gravity_vector = arrow(color=color.red, shaftwidth = 0.01, axis = vector(0,(-50*m*g) / 5,0), 
                               pos = vector(center_of_gravity[0], center_of_gravity[1], center_of_gravity[2]))
TR_vector = arrow(color=color.green, shaftwidth = 0.01, axis = vector(0,(-50*m*g) / 5,0), 
                               pos = vector(center_of_gravity[0], center_of_gravity[1], center_of_gravity[2]))
TL_vector = arrow(color=color.blue, shaftwidth = 0.01, axis = vector(0,(-50*m*g) / 5,0), 
                               pos = vector(center_of_gravity[0], center_of_gravity[1], center_of_gravity[2]))

while True:
    rate(1/dt)
    t += dt        #計時器
    spring_axis = ball_pos[1:] - ball_pos[:-1]        #每個彈簧的軸方向
    b = np.sum(spring_axis**2, axis = 1)**0.5         #每個彈簧的長度
    spring_axis_unit = spring_axis / b[:, np.newaxis] #每個彈簧軸方向的單位向量
    fs = - k * (spring_axis - d*spring_axis_unit)     #每個彈簧的作用力
    fs[b<=d] = 0                                      #彈簧長度小於原長設為零，表示繩子的鬆弛狀態
    
    ball_v[1:-1] += (fs[:-1] - fs[1:])/m*dt + ball_g[1:-1]*dt - 5.0*ball_v[1:-1]*dt    
                                                      #計算第二個~倒數第二個球的速度
    ball_pos += ball_v *dt                            #計算球的位置
    
    center_of_gravity = np.sum(ball_pos, axis = 0) / 50
    TR_vector.axis = vector(spring_axis_unit[-1][0]* fs[-1][0]/-5, spring_axis_unit[-1][1]* fs[-1][1]/-5, spring_axis_unit[-1][2]* fs[-1][2]/-5)
    TL_vector.axis = vector(fs[0][0]/5,fs[0][1]/5,fs[0][2]/5)
    
    T = t % (50*dt)                  #用餘數除法定出要更新圖形的時間點，每50個迴圈會歸零一次
    if T + dt >50*dt and T < 50*dt:  #在T被歸零前的那瞬間更新畫面圖形
        #gravity_vector.pos = vector(center_of_gravity[0], center_of_gravity[1], center_of_gravity[2])
        for i in range(N):        #畫球
            balls[i].pos = vector(ball_pos[i][0], ball_pos[i][1], ball_pos[i][2])
        for i in range(N-1):      #畫彈簧
            springs[i].pos = balls[i].pos
            springs[i].axis = balls[i+1].pos - balls[i].pos

        gravity_vector.pos = vector(center_of_gravity[0], center_of_gravity[1], center_of_gravity[2])
        TR_vector.pos = balls[49].pos
        TL_vector.pos = balls[0].pos