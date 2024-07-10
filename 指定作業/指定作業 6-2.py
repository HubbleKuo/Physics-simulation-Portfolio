from vpython import *  #引用視覺畫套件Vpython
"""
    1. 參數設定，設定變數及定義萬有引力公式
"""

G = 6.67*10**(-11) ; m1 = 1.9891*10**30 ; r1 = 6.955*10**8 ; 
m2 = 5.9742*10**24 ; r2 = 6.3728*10**6 ; m3 = 7.342*10**22 ; r3 = 1.7371*10**6 
R_12 = 1.496*10**11 ; R_23 = 3.84399*10**8
t = 0 ; dt = 100
v2 = (G*m1/R_12)**0.5
v3 = (G*m2/R_23)**0.5  #月球以圓周運動繞地球的速率
T_earth = 0 ; T1_moon =0 ;  T2_moon = 0
t1 = t2 = t3 = 0
pre_pre_m1m2_rv = pre_m1m2_rv = vector(0,0,0)
pre_pre_m2m3_rv = pre_m2m3_rv = vector(0,0,0)
radiavector_12 =  radiavector_23 = vector(0,0,0)
def Fg(x,y1,y2): 
    return -G*y1*y2/(x**2)
"""
    2. 畫面設定
"""
scene = canvas(width=1200, height=800, center=vec(0,0,0),background=vec(0.6,0.8,0.8),range=7*R_23)

ball_m1 = sphere(pos=vector(0,0,0), radius=20*r1, color = color.yellow, make_trail=True)
ball_m2 = sphere(pos=vector(R_12,0,0), radius=20*r2, color = color.blue, make_trail=True)
ball_m3 = sphere(pos=vector(R_12+R_23,0,0), radius=20*r3, color = color.red, make_trail=True)

ball_m1_v = vector(0,0,0) ; ball_m2_v = vector(0,v2,0) ; ball_m3_v = vector(0,v2+v3,0)
#ball_m1=sun ; ball_m2=earth ; ball_m3=moon
"""
    3. 執行迴圈
"""
while True:
    rate(10000)
    scene.center = ball_m2.pos

    pre_pre_m1m2_rv = pre_m1m2_rv
    pre_m1m2_rv = radiavector_12

    pre_pre_m2m3_rv = pre_m2m3_rv
    pre_m2m3_rv = radiavector_23    
    
    # 月球受太陽的力與產生的運動
    dist_12 = mag(ball_m1.pos-ball_m2.pos) 
    radiavector_12 = (ball_m2.pos-ball_m1.pos)/dist_12
    Fg_12_vector = Fg(dist_12,m1,m2)*radiavector_12

    dist_23 = mag(ball_m2.pos - ball_m3.pos) 
    radiavector_23 = (ball_m3.pos-ball_m2.pos)/dist_23
    Fg_23_vector = Fg(dist_23,m2,m3)*radiavector_23

    
    # 地球受太陽的力
    dist_13 = mag(ball_m1.pos -ball_m3.pos) 
    radiavector_13 = (ball_m3.pos-ball_m1.pos)/dist_13
    Fg_13_vector = Fg(dist_13,m1,m3)*radiavector_13
   
    
    ball_m2_v += Fg_12_vector/m2*dt
    ball_m2.pos = ball_m2.pos + ball_m2_v*dt
    
    ball_m3_v += (Fg_23_vector+Fg_13_vector)/m3*dt
    ball_m3.pos = ball_m3.pos + ball_m3_v*dt
    

    if pre_m1m2_rv.x > pre_pre_m1m2_rv.x and pre_m1m2_rv.x >  radiavector_12.x :
        T_earth = t1/86400.0 #設定earth_T為地球週期
        print ('earth_t=' , '%1.2f'%T_earth)
        t1=0 #時間重置

    #找月球相對地球右端點位置
    if pre_m2m3_rv.x > pre_pre_m2m3_rv.x and pre_m2m3_rv.x >  radiavector_23.x :
        T1_moon = t2/86400.0 #設定moon_T為月球週期
        print ('moon_T=' , '%1.2f'%T1_moon)
        t2=0 #時間重置

    #找月球相對地球向量與太陽相對地球向量相減最小的位置
    if mag(pre_m1m2_rv-pre_m2m3_rv) > mag(pre_pre_m1m2_rv-pre_pre_m2m3_rv) and mag(pre_m1m2_rv-pre_m2m3_rv) >  mag(radiavector_12-radiavector_23) :
        T2_moon = t3/86400.0 #設定moon_T2為月球週期2
        print ('moon_T2=' , '%1.2f'%T2_moon)
        t3=0 #時間重置
        
    t += dt
    t1 += dt
    t2 += dt
    t3 += dt
