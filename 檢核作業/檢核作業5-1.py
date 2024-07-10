from vpython import *  #引用視覺畫套件Vpython

G = 6.67*10**(-11) ; M_earth = 6*10**24 ; m_mater = 1000  
Re = 6.4*10**6 ; H = 5*Re ; t = 0 ; dt = 1
def Fg(x):                                 #定義公式
    return -G*M_earth*m_mater/(x**2)
V0 = (G*M_earth/H)**0.5

scene = canvas(align = 'left',title ='4_01_Gravity force',  width=800, height=300, center=vec(0,0,0), background=vec(0.6,0.8,0.8)) #設定視窗
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth) #放置物件地球
mater = sphere(pos=vec(H,0,0), radius=0.1*Re,color=color.red, make_trail=True) #放置物件衛星
materv = vec(0,0.7*V0,0)

gd = graph(align='left',width=400,height=400,  
              title='K+U+E', xtitle='t', ytitle='E(red),K(black),U(green)',
              foreground=color.black,background=color.white,
              xmax=10**5, xmin=0, ymax=4*10**10, ymin=-4*10**10)
f_U = gcurve(color=color.green)
f_K = gcurve(color=color.black)
f_total = gcurve(color=color.red)

def k_e(m,v):
    return(0.5*m*(v**2))

def u_e(r):
    return(-G * M_earth * m_mater / r)

while True:  #執行迴圈
    rate(5000)
    dist = ((mater.pos.x-earth.pos.x)**2+(mater.pos.y-earth.pos.y)**2+(mater.pos.z-earth.pos.z)**2)**0.5 #距離純量
    radiavector = (mater.pos-earth.pos)/dist #距離單位向量
    Fg_vector = Fg(dist)*radiavector # 萬有引力向量=萬有引力量值*單位向量

    materv += (Fg_vector/m_mater) * dt
    mater.pos += materv * dt

    E_k = k_e(m_mater, mag(materv))
    E_u = u_e(dist)
    E_total = E_k + E_u

    f_K.plot(pos=(t,E_k))
    f_U.plot(pos=(t,E_u))
    f_total.plot(pos=(t,E_total))
    
    t += dt