from vpython import *  

G = 6.67*10**(-11) ; M = 6*10**24 ; m = 1000  
Re = 6.4*10**6 ; H = 5*Re ; t = 0 ; dt = 1
def Fg(x):                                 #定義公式
    return -G*M*m/(x**2)
V0 = (G*M/H)**0.5


scene = canvas(align = 'left',title ='4_01_Gravity force',  width=800, height=300, center=vec(0,0,0), background=vec(0.6,0.8,0.8)) #設定視窗
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth) #放置物件地球
mater = sphere(pos=vec(H,0,0), radius=0.1*Re,color=color.red, make_trail=True) #放置物件衛星
materv = vec(0,0.7*V0,0) 

Fe = G*M*m/Re**2 #定義地球表面重力強度

v_arrow = arrow(shaftwidth=0.05*Re, pos=mater.pos, color = color.red)
a_arrow = arrow(shaftwidth=0.05*Re, pos=mater.pos, color = color.yellow)
at_arrow = arrow(shaftwidth=0.05*Re, pos=mater.pos, color = color.green)
an_arrow = arrow(shaftwidth=0.05*Re, pos=mater.pos, color = color.white)


oval = curve( color = color.black )
for N in range(0, 360, 1):
    oval.append( pos =(2.119*10**7*cos(N*pi/180)+1*(2.119**2-1.8228**2)**0.5*10**7,1.8228*10**7*sin(N*pi/180),0) )

"""
    3. 執行迴圈
"""
while True:  #執行迴圈
    rate(5000)
    dist = ((mater.pos.x-earth.pos.x)**2+(mater.pos.y-earth.pos.y)**2+(mater.pos.z-earth.pos.z)**2)**0.5 #距離純量
    radiavector = (mater.pos-earth.pos)/dist #距離單位向量
    Fg_vector = Fg(dist)*radiavector # 萬有引力向量=萬有引力量值*單位向量
    
    materv += Fg_vector/m*dt   #Δv = F/m *dt
    mater.pos = mater.pos + materv*dt  # S = S0 + v *dt

    v_arrow.axis = materv*5*10**3
    a_arrow.axis = Fg_vector/m*10**7
    at_arrow.axis = dot(Fg_vector/m,materv)*(norm(materv)/mag(materv))*10**7
    an_arrow.axis = (mag(cross(Fg_vector/m,materv))/mag(materv))*cross(norm(materv),vector(0,0,-1))*10**7

    v_arrow.pos = mater.pos
    a_arrow.pos = mater.pos
    at_arrow.pos = mater.pos
    an_arrow.pos = mater.pos
    t = t+dt
