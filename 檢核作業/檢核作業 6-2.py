"""
    建國中學 Vpython物理模擬
    作者: 物理科 賴奕帆老師
    特色課程 Lecture 06 雙星運動與日地月三行星運動
    6_02_Three star sports.py
"""
from vpython import *  #引用視覺畫套件Vpython
"""
    1. 參數設定，設定變數及定義萬有引力公式
"""

G = 6.67 ; m1 = 100; m2 = 10; m3 = 1; R_12 = 10; R_23 = 1; t = 0 ; dt = 0.001
v2 = (G*m1/R_12)**0.5
v3 = (G*m2/R_23)**0.5

def Fg(x,y1,y2): 
    return -G*y1*y2/(x**2)
"""
    2. 畫面設定
"""
scene = canvas(width=1200, height=800, center=vec(0,0,0),background=vec(0.6,0.8,0.8),range=2*R_12)

ball_m1 = sphere(pos=vector(0,0,0), radius=1, color = color.yellow, make_trail=True)
ball_m2 = sphere(pos=vector(R_12,0,0), radius=0.3, color = color.blue, make_trail=True)
ball_m3 = sphere(pos=vector(R_12+R_23,0,0), radius=0.1, color = color.red, make_trail=True)

ball_m1_v = vector(0,0,0) ; ball_m2_v = vector(0,v2,0) ; ball_m3_v = vector(0,v2 + v3,0)

earth = arrow(pos = ball_m3.pos, shaftwidth = 0.1, color=color.blue)
sun = arrow(pos=ball_m3.pos,shaftwidth = 0.1,  color=color.yellow)
total = arrow(pos=ball_m3.pos, shaftwidth =0.1, color=color.black)
"""
    3. 執行迴圈
"""
while True:
    rate(1000)
    dist_12 = mag(ball_m1.pos-ball_m2.pos) 
    radiavector_12 = (ball_m2.pos-ball_m1.pos)/dist_12
    Fg_12_vector = Fg(dist_12,m1,m2)*radiavector_12

    dist_23 = mag(ball_m2.pos - ball_m3.pos) 
    radiavector_23 = (ball_m3.pos-ball_m2.pos)/dist_23
    Fg_23_vector = Fg(dist_23,m2,m3)*radiavector_23
    earth.axis = Fg_23_vector/3
    
    # 月球受太陽的力
    dist_13 = mag(ball_m1.pos -ball_m3.pos) 
    radiavector_13 = (ball_m3.pos-ball_m1.pos)/dist_13
    Fg_13_vector = Fg(dist_13,m1,m3)*radiavector_13
    sun.axis = Fg_13_vector/3
    
    ball_m2_v += Fg_12_vector/m2*dt
    ball_m2.pos = ball_m2.pos + ball_m2_v*dt
    
    ball_m3_v += (Fg_23_vector+Fg_13_vector)/m3*dt
    ball_m3.pos = ball_m3.pos + ball_m3_v*dt

    total.axis = (Fg_13_vector + Fg_23_vector)/3

    earth.pos = ball_m3.pos
    sun.pos = ball_m3.pos
    total.pos = ball_m3.pos

    t = t+dt