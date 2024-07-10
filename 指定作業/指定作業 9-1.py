from vpython import *  

k = 9*10**9 ;  size = 0.1  ;  b_N = 36
t = 0 ; dt = 0.01

Q1_charge = 10**(-5)
Q2_charge = -10**(-5)
Q3_charge = 10**(-5)
Q4_charge = -10**(-5)

Q1_pos = vector(2, 0, 0)
Q2_pos = vector(0, 2, 0)
Q3_pos = vector(-2, 0, 0)
Q4_pos = vector(0, -2, 0)

q_charge = 10**(-8.5)
q_pos = vector(-0.42, -0.2, 0)
q_m = 10**(-3)
q_v = vector(0,0,0)

scene = canvas(title='dipole', height=700, width=700, range=3.5,auto_scale=False)
Q1 = sphere(pos = Q1_pos , radius = size , color = color.blue)
Q2 = sphere(pos = Q2_pos, radius = size , color = color.blue)
Q3 = sphere(pos = Q3_pos, radius = size , color = color.red)
Q4 = sphere(pos = Q4_pos, radius = size , color = color.red)
q = sphere(pos = q_pos , radius = 0.5*size , color = color.green, v = q_v, make_trail=True)


field_ball_1=[]
for N in range(0,b_N,1):#build field ball from ball
    field_ball_1.append(sphere(pos=vector(size*cos(2*pi*N/b_N), size*sin(2*pi*N/b_N),0)+Q1.pos,radius=0.01, color=vec(1,1,0), make_trail=True, v=vector(0,0,0)))

field_ball_2=[]
for N in range(0,b_N,1):#build field ball from ball
    field_ball_2.append(sphere(pos=vector(size*cos(2*pi*N/b_N), size*sin(2*pi*N/b_N),0)+Q2.pos,radius=0.01, color=vec(1,1,0), make_trail=True, v=vector(0,0,0)))

field_ball_3=[]
for N in range(0,b_N,1):#build field ball from ball
    field_ball_3.append(sphere(pos=vector(size*cos(2*pi*N/b_N), size*sin(2*pi*N/b_N),0)+Q3.pos,radius=0.01, color=vec(0.8,0.8,0.3), make_trail=True, v=vector(0,0,0)))                             

field_ball_4=[]
for N in range(0,b_N,1):#build field ball from ball
    field_ball_4.append(sphere(pos=vector(size*cos(2*pi*N/b_N), size*sin(2*pi*N/b_N),0)+Q4.pos,radius=0.01, color=vec(0.8,0.8,0.3), make_trail=True, v=vector(0,0,0)))

def Force_E(r, q):#force of field 
    r1 = r - Q1.pos
    r2 = r - Q2.pos
    r3 = r - Q3.pos
    r4 = r - Q4.pos
    return k*q*Q1_charge*r1.norm()/(r1.mag*r1.mag)+  k*q*Q2_charge*r2.norm()/(r2.mag*r2.mag)+k*q*Q3_charge*r3.norm()/(r3.mag*r3.mag)+k*q*Q4_charge*r4.norm()/(r4.mag*r4.mag)

while True :
    rate(1000)
    
    for N in field_ball_1:
        N.v = Force_E(N.pos, 1.0).norm()
        N.pos += N.v*dt

    for N in field_ball_2:
        N.v = Force_E(N.pos, 1.0).norm()
        N.pos += N.v*dt

    for N in field_ball_3:
        N.v = Force_E(N.pos, 1.0).norm()
        N.pos += N.v*dt

    for N in field_ball_4:
        N.v = Force_E(N.pos, 1.0).norm()
        N.pos += N.v*dt


    if mag(q.pos-Q1_pos)>=size and mag(q.pos-Q2_pos)>=size and mag(q.pos-Q3_pos)>=size and mag(q.pos-Q4_pos)>=size  :    
        q.v = q.v + Force_E(q.pos, q_charge)/q_m *dt
        q.pos = q.pos+q.v*dt
    else :
        q.pos = q.pos





