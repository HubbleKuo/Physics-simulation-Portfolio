from vpython import *

size = 0.1     #球的大小
theta = 0.0    #初始角度
R = 1.0        #圓周運動半徑
omega = 2*pi   #角速度大小=單位時間繞過的角度
t = 0.0        #初始時間
pre_theta = theta
pre_pre_theta = pre_theta

scene = canvas(width=500, height=500, center=vector(0,0,0), background=vector(148.0/225,228.0/225,204.0/225))
ball = sphere(radius=size, color=color.blue,pos=vector(R,0,0), v=vector(0,0,0), make_trail=True, interval = 1, retain = 900)
v_vector = arrow(radius=size, color=color.green)
a_vector = arrow(radius=size, color=color.red)
v_text = label(box =False, opacity=0, height=25, color=color.green, text = "v" )
a_text = label(box =False, opacity=0, height=25, color=color.red, text = "a" )


t = 0.0       #初始時間
dt = 0.001    #時間間隔
ac = R*omega**2

back = False
period_t = 0
plot_t = 0
count = 0
N = 20
T = 1/20

while True:
    t += dt
    rate(1/dt)

    pre_pre_theta = pre_theta
    pre_theta = theta
    theta += omega*dt

    pre_pre_ball_pos = vector(R*cos(pre_pre_theta), R*sin(pre_pre_theta), 0)
    pre_ball_pos = vector(R*cos(pre_theta), R*sin(pre_theta), 0)
    now_ball_pos = vector(R*cos(theta), R*sin(theta),0)
    ball.pos = pre_ball_pos

    pre_v = (pre_ball_pos - pre_pre_ball_pos) / dt
    v = (now_ball_pos - pre_ball_pos) / dt
    ball.v = pre_v

    ball_a = (v - pre_v)/dt
    s_a = mag(ball_a)

    v_vector.pos = ball.pos
    v_vector.axis = ball.v/10
    v_text.pos = v_vector.pos + v_vector.axis*1.2

    a_vector.pos = ball.pos
    a_vector.axis = ball_a * R / mag(ball_a)
    a_text.pos = a_vector.pos + a_vector.axis*1.2


    print(f"simulated acceleration = {s_a}, theoretical acceleraion = {ac}")