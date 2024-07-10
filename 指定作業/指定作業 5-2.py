from vpython import*

G = 6.67*10**(-11) ; M = 6*10**24 ; m = 1000  
Re = 6.4*10**6 ; H = 5*Re ; t = 0 ; dt = 1
def Fg(x):                                 #定義公式
    return -G*M*m/(x**2)
V0= (G*M/H)**0.5


scene = canvas(align = 'left',title ='4_01_Gravity force',  width=800, height=300, center=vec(0,0,0), background=vec(0.6,0.8,0.8)) #設定視窗
sun = sphere(pos=vec(0,0,0), radius=Re,color=color.red ) 
earth = sphere(pos=vec(H,0,0), radius=0.1*Re,texture=textures.earth, make_trail=True)
venus = sphere(pos=vec(H,0,0), radius=0.1*Re,color=color.yellow, make_trail=True) 
earthv = vec(0,0.7*V0,0)
venusv = vec(0,0.9*V0,0) 

Fe = G*M*m/Re**2 #定義地球表面重力強度

pre_pre_pos_earth = vector(0,0,0)
pre_pos_earth = vector(0,0,0)
pre_pre_pos_venus = vector(0,0,0)
pre_pos_venus = vector(0,0,0)
el = er =ve = vr = 0
Te = Tv = 0

while True:  #執行迴圈
    rate(5000)
    
    dist1 = ((earth.pos.x-sun.pos.x)**2+(earth.pos.y-sun.pos.y)**2+(earth.pos.z-sun.pos.z)**2)**0.5 #距離純量
    radiavector1 = (earth.pos-sun.pos)/dist1 #距離單位向量
    Fg1_vector = Fg(dist1)*radiavector1 # 萬有引力向量=萬有引力量值*單位向量    
    earthv += Fg1_vector/m*dt   #Δv = F/m *dt
    pre_pre_pos_earth = pre_pos_earth
    pre_pos_earth = earth.pos    
    earth.pos = earth.pos + earthv*dt  # S = S0 + v *dt

    dist2 = ((venus.pos.x-sun.pos.x)**2+(venus.pos.y-sun.pos.y)**2+(venus.pos.z-sun.pos.z)**2)**0.5 #距離純量
    radiavector2 = (venus.pos-sun.pos)/dist2 #距離單位向量
    Fg2_vector = Fg(dist2)*radiavector2 # 萬有引力向量=萬有引力量值*單位向量    
    venusv += Fg2_vector/m*dt   #Δv = F/m *dt
    pre_pre_pos_venus = pre_pos_venus 
    pre_pos_venus = venus.pos
    venus.pos = venus.pos + venusv*dt  # S = S0 + v *dt
    
    t = t+dt
    Te +=dt
    Tv +=dt

    if pre_pos_earth.x < pre_pre_pos_earth.x and pre_pos_earth.x < earth.pos.x :
        el = earth.pos.x
    if pre_pos_earth.x > pre_pre_pos_earth.x and pre_pos_earth.x > earth.pos.x :
        er = earth.pos.x
        print("k1 = ",((er-el)**3/(8*Te**2)))
        Te = 0
    if pre_pre_pos_venus.x > pre_pos_venus.x and pre_pos_venus.x < venus.pos.x :
        vl = venus.pos.x
    if pre_pre_pos_venus.x < pre_pos_venus.x and pre_pos_venus.x > venus.pos.x :
        vr = venus.pos.x
        print("k2 = ", (vr-vl)**3/(8*Tv**2))
        Tv = 0
