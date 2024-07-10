from vpython import *  #引用視覺畫套件Vpython
"""
    1. 參數設定，設定變數及定義萬有引力公式
"""

G = 6.67 ; m = 1300 ; R = 2 ; v_m2 = 5 ; t = 0 ; dt = 0.001
L = 50 ; V0 = 10
def Fg(x): #定義萬有引力函數
    return -G*m*m/(x**2)
"""
    2. 畫面設定
"""
 
scene = canvas(width=700, height=700, center=vec(0,0,0),
                background=vec(0.6,0.8,0.8))

ball_1 = sphere(pos=vector(0,L,0), radius=1, color = color.yellow, make_trail=True)
ball_2 = sphere(pos=vector(L*cos(pi/6),-L*sin(pi/6),0), radius=1, color = color.red, make_trail=True)
ball_3 = sphere(pos=vector(-L*cos(pi/6),-L*sin(pi/6),0), radius=1, color = color.blue, make_trail=True)
ball_1_v = vector(-V0,0,0)
ball_2_v = vector(V0*cos(pi/3), V0*sin(pi/3), 0 )
ball_3_v =vector(V0*cos(pi/3), -V0*sin(pi/3), 0 )

while True:
    rate(2000)
    # 將純量改為向量
    dist1_2 = ((ball_1.pos.x-ball_2.pos.x)**2+(ball_1.pos.y-ball_2.pos.y)**2+(ball_1.pos.z-ball_2.pos.z)**2)**0.5
    radiavector1_2 = (ball_2.pos-ball_1.pos)/dist1_2
    Fg_vector_12 = Fg(dist1_2)*radiavector1_2 #行星所受萬有引力

    dist2_3 = ((ball_2.pos.x-ball_3.pos.x)**2+(ball_2.pos.y-ball_3.pos.y)**2+(ball_2.pos.z-ball_3.pos.z)**2)**0.5
    radiavector2_3 = (ball_3.pos-ball_2.pos)/dist2_3
    Fg_vector_23 = Fg(dist2_3)*radiavector2_3 #行星所受萬有引力

    dist3_1 = ((ball_3.pos.x-ball_1.pos.x)**2+(ball_3.pos.y-ball_1.pos.y)**2+(ball_3.pos.z-ball_1.pos.z)**2)**0.5
    radiavector3_1 = (ball_1.pos-ball_3.pos)/dist3_1
    Fg_vector_31 = Fg(dist3_1)*radiavector3_1 #行星所受萬有引力

    ball_1_v += (Fg_vector_31 - Fg_vector_12)/m*dt #力生加速度, 產生速度變化
    ball_1.pos +=  ball_1_v*dt #速度產生位置變化
    ball_2_v += (Fg_vector_12 - Fg_vector_23)/m*dt #力生加速度, 產生速度變化
    ball_2.pos +=  ball_2_v*dt #速度產生位置變化
    ball_3_v += (Fg_vector_23 - Fg_vector_31)/m*dt #力生加速度, 產生速度變化
    ball_3.pos +=  ball_3_v*dt #速度產生位置變化
   

