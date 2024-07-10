from vpython import*

m1 = 1.0                 
size1 = 1.0                 #球1大小
Y1 = 20

m2 = 5.0                   #球2質量
size2 = 2.0                 #球2大小
Y2 = 17

m3 = 30.0                   #球2質量
size3 = 3.0
Y3 = 12

g = 9.8
Force = 5.0
k = 0.05
t = 0
dt = 0.001

v1y = 0
v2y = 0
v3y = 0


scene = canvas(width=600, height=600,x=0, y=0, center = vector(0,0,0)) 
floor = box(length=20, height=0.01, width=10, color=color.blue)
ball1 = sphere(radius=size1, color = color.yellow, make_trail = False)
ball2 = sphere(radius=size2, color = color.green, make_trail = False)
ball3 = sphere(radius=size3, color = color.blue, make_trail = False)  

ball1.pos = vector(0,Y1,0)            
ball1.v = vector (0,v1y,0)
ball1.a = vector(0,-g,0)
ball2.pos = vector(0,Y2,0)            
ball2.v = vector (0,v2y,0)
ball2.a = vector(0,-g,0)
ball3.pos = vector(0,Y3,0)            
ball3.v = vector (0,v3y,0)
ball3.a = vector(0,-g,0)

pre_ball1_pos = 0
pre_pre_ball1_pos = 0


while True  :
    rate(1/dt)
    t += dt
    
    pre_pre_ball1_pos = pre_ball1_pos
    pre_ball1_pos = ball1.pos.y
    
    ball1.v = ball1.v + ball1.a*dt
    #ball1.v -= ball1.v*k*dt
    ball1.pos += ball1.v*dt
    ball2.v = ball2.v + ball2.a*dt
    #ball2.v -= ball2.v*k*dt
    ball2.pos += ball2.v*dt
    ball3.v = ball3.v + ball3.a*dt
    #ball3.v -= ball3.v*k*dt
    ball3.pos += ball3.v*dt



    if ball3.pos.y - size3 <= 0 and ball3.v.y < 0  :
        ball3.v = -ball3.v

    if ball1.pos.y-ball2.pos.y < size1 + size2 :
        v1y = ((m1-m2)*(ball1.v.y)/(m1+m2)) + (2*m2*ball2.v.y)/(m1+m2)
        v2y = (m2-m1)*ball2.v.y/(m1+m2) + 2*m1*ball1.v.y/(m1+m2)
        ball1.v = vector (0 , v1y , 0)
        ball2.v = vector (0 , v2y , 0)
        
    if ball2.pos.y-ball3.pos.y < size2 + size3 :
        v2y = (m2-m3)*ball2.v.y/(m2+m3) + 2*m3*ball3.v.y/(m3+m2)
        v3y = (m3-m2)*ball3.v.y/(m3+m2) + 2*m2*ball2.v.y/(m3+m2)
        ball2.v = vector (0 , v2y , 0)
        ball3.v = vector (0 , v3y , 0) 

    if pre_ball1_pos > pre_pre_ball1_pos and pre_ball1_pos > ball1.pos.y :
        print (ball1.pos.y)



