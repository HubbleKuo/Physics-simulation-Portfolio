from vpython import*
import numpy as np
N = 20		#質點個數
g = 3.8		#重力加速度
size, m, k = 0.016, 0.1/N, N*0.75#球大小、質點質量、各力常數、間距
d = size/5
t, dt = 0, 0.0001                                #初始時間、時間間隔
T, T0 = 0, 2.5
f = 0.05

scene = canvas(width=300, height = 725, center = vector(0, -d*N*0.9, 0), range = 5*d*N)
floor = box(color=color.blue, height = 0.01, width = 0.4, length = 0.4, pos = vector(0, -10*d*N, 0))
springs = [helix(radius = size*3, thickness = size/2.5, coils = 1) for i in range(N-1)]
f1 = graph(xtitle='t', ytitle='v', width=300, height=300)
f1_1 = gcurve(color=color.red)
f1_2 = gcurve(color=color.green)
ball_pos, ball_v, ball_g = np.zeros((N, 3)), np.zeros((N,3)), np.zeros((N,3))
#以array建立初位置、初速度、重力加速度，全為0的N列3行的陣列

ball1 = sphere(radius=size*3, color=color.yellow, pos = vector(0, 10*d*N-20*0.9*d,0)) 
ball2 = sphere(radius=size, color=color.green, pos = vector(0, -0.9*d*N/2+10*N*d,0)) 
for i in range(N):
    ball_pos[i][1] = -d*i*0.9 + 10*d*N
    ball_g[i][1] = -g        #將重力加速度陣列的第2行改為-9.8，表示每個球在y方向受到的重力場

while ball1.pos.y > -10*d*N + size*3:
    rate(1/dt)
    t += dt        #計時器
    spring_axis = ball_pos[1:] - ball_pos[:-1]        #每個彈簧的軸方向
    b = np.sum(spring_axis**2, axis = 1)**0.5         #每個彈簧的長度
    spring_axis_unit = spring_axis / b[:, np.newaxis] #每個彈簧軸方向的單位向量
    fs = - k * (spring_axis - d*spring_axis_unit)     #每個彈簧的作用力
    fs[b<=d] = 0                                      #彈簧長度小於原長設為零，表示繩子的鬆弛狀態
    
    ball_v[1:-1] += (fs[:-1]-fs[1:]) /m*dt + ball_g[1:-1]*dt - (f*ball_v[1:-1]/m)*dt                                                       #計算第二個~倒數第二個球的速度
    ball_v[-1] += fs[-1]/m*dt + ball_g[-1]*dt - (f*ball_v[-1]/m)*dt   
    ball_pos += ball_v *dt                            #計算球的位置



    for i in range(N-1):
        springs[i].pos = vector(ball_pos[i][0], ball_pos[i][1], ball_pos[i][2])
        springs[i].axis = vector(ball_pos[i+1][0], ball_pos[i+1][1], ball_pos[i+1][2]) - vector(ball_pos[i][0], ball_pos[i][1], ball_pos[i][2])
    ball1.v = vector(ball_v[-1][0], ball_v[-1][1], ball_v[-1][2])
    ball1.pos += ball1.v*dt
    ball2.pos = vector(0, np.sum(ball_pos, axis = 0)[1]/N, 0)

    if t >T0 :
        f = 0
        ball_v[0] += ball_g[0]*dt - fs[0]/m*dt
        ball_pos[0] += ball_v[0]*dt
        for j in arange(N-1): #由第1根彈簧算到最個最後1根，個數比球少1個
            if (ball_pos[j][1] - ball_pos[j+1][1]) <= d:  #球和球間距小於彈簧原長
                ball_v[j] = ball_v[j+1] = (ball_v[j] + ball_v[j+1])/2  #碰撞後速度
                ball_pos[j+1][1] = ball_pos[j][1] - d                  #碰撞後球的間距
        ball1.v = vector(ball_v[-1][0], ball_v[-1][1], ball_v[-1][2])
        ball1.pos += ball1.v*dt
        ball2.pos = vector(0, np.sum(ball_pos, axis = 0)[1]/N, 0)
        ball2.v = vector(0, np.sum(ball_v, axis = 0)[1]/N, 0)
        f1_1.plot(pos=(t,ball1.v.y))
        f1_2.plot(pos=(t, ball2.v.y))

 
