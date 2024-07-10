from vpython import *  #引用視覺畫套件Vpython
"""
    1. 參數設定，設定變數及定義萬有引力公式
"""

G = 6.67 ; m1 = 10 ; m2 = 3 ; R = 10 ; v_m2 = (G*m1/R)**0.5 ; t = 0 ; dt = 0.001

def Fg(x): #定義萬有引力函數
    return -G*m1*m2/(x**2)
"""
    2. 畫面設定
"""
 
scene = canvas(width=1200, height=800, center=vec(0,0,0),
                background=vec(0.6,0.8,0.8),range=2*R)

ball_m1 = sphere(pos=vector(0,0,0), radius=1, color = color.blue, make_trail=True)
ball_m2 = sphere(pos=vector(R,0,0), radius=0.3, color = color.red, make_trail=True)
ball_m1_v = vector(0,-v_m2*m2/m1,0)
ball_m2_v = vector(0,v_m2,0)

gd = graph(title="K1 + K2 + U = E", xtitle="t", ytitle="E")
g_k1 = gcurve(color=color.blue)
g_k2 = gcurve(color=color.red)
g_U = gcurve(color=color.green)
g_total = gcurve(color=color.black)

"""
    3. 執行迴圈
"""

while True:
    rate(2000)
    # 將純量改為向量
    ##dist = ((ball_m1.pos.x-ball_m2.pos.x)**2+(ball_m1.pos.y-ball_m2.pos.y)**2+(ball_m1.pos.z-ball_m2.pos.z)**2)**0.5
    dist = mag(ball_m1.pos-ball_m2.pos)  #mag可得純量    
    #radiavector = (ball_m2.pos-ball_m1.pos)/dist
    radiavector = norm(ball_m2.pos-ball_m1.pos) #norm可得單位向量
    Fg_vector = Fg(dist)*radiavector #行星所受萬有引力
    
    ball_m2_v += Fg_vector/m2*dt #力生加速度, 產生速度變化
    ball_m2.pos = ball_m2.pos + ball_m2_v*dt #速度產生位置變化

    ball_m1_v += -Fg_vector/m1*dt #讓藍色行星m1也受力  
    ball_m1.pos = ball_m1.pos + ball_m1_v*dt #讓藍色行星m1開始運動

    k_1 = 0.5 * m1 * (mag(ball_m1_v)**2)
    k_2 = 0.5 * m2 * (mag(ball_m2_v)**2)
    U = -G * m1 * m2 / dist

    g_k1.plot(pos=(t,k_1))
    g_k2.plot(pos=(t,k_2))
    g_U .plot(pos=(t, U))
    g_total.plot(pos=(t,k_1 + k_2 + U))


    t = t+dt