from vpython import *  #引用視覺畫套件Vpython

G = 6.67*10**(-11) 
M_earth = 6*10**24  
Re = 6.4*10**6 

m_mater1 = 1000  
H1 = 5*Re 
V1 = (G*M_earth/H1)**0.5

m_mater2 = 1000  
H2 = 10*Re 
V2 = (G*M_earth/H2)**0.5

m_mater3 = 1000  
H3 = 15*Re 
V3 = (G*M_earth/H3)**0.5

t = 0 
dt = 1
def Fg(x):                                 #定義公式
    return -G*M_earth*m_mater1/(x**2)

scene = canvas(align = 'left',title ='4_01_Gravity force',  width=800, height=300, center=vec(0,0,0), background=vec(0.6,0.8,0.8)) #設定視窗
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth) #放置物件地球

mater1 = sphere(pos=vec(H1,0,0), radius=0.1*Re,color=color.red, make_trail=True) #放置物件衛星
materv = vec(0,0.8*V1,0)

mater2 = sphere(pos=vec(H1,0,0), radius=0.1*Re,color=color.blue, make_trail=True) #放置物件衛星
mater2v = vec(0,0.7*V1,0)

mater3 = sphere(pos=vec(H1,0,0), radius=0.1*Re,color=color.green, make_trail=True) #放置物件衛星
mater3v = vec(0,0.9*V1,0)

while True:  #執行迴圈
    rate(5000)
    
    dist1 = ((mater1.pos.x-earth.pos.x)**2+(mater1.pos.y-earth.pos.y)**2+(mater1.pos.z-earth.pos.z)**2)**0.5 #距離純量
    radiavector1 = (mater1.pos-earth.pos)/dist1 #距離單位向量
    
    dist2 = ((mater2.pos.x-earth.pos.x)**2+(mater2.pos.y-earth.pos.y)**2+(mater2.pos.z-earth.pos.z)**2)**0.5 #距離純量
    radiavector2 = (mater2.pos-earth.pos)/dist2 #距離單位向量

    dist3 = ((mater3.pos.x-earth.pos.x)**2+(mater3.pos.y-earth.pos.y)**2+(mater3.pos.z-earth.pos.z)**2)**0.5 #距離純量
    radiavector3 = (mater3.pos-earth.pos)/dist3 #距離單位向量

    Fg_vector1 = Fg(dist1)*radiavector1 # 萬有引力向量=萬有引力量值*單位向量
    Fg_vector2 = Fg(dist2)*radiavector2
    Fg_vector3 = Fg(dist3)*radiavector3

    materv += (Fg_vector1/m_mater1) * dt
    mater1.pos += materv * dt

    mater2v += (Fg_vector2/m_mater2) * dt
    mater2.pos += mater2v * dt

    mater3v += (Fg_vector3/m_mater3) * dt
    mater3.pos += mater3v * dt
    
    t += dt