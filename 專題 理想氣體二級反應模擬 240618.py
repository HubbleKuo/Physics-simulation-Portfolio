from vpython import *
import numpy as np
Ea = 150000                 # 活化能
m = 0.08                    # 分子質量
N_particals = 500           # 反應物粒子數
molecule_size = 0.1         # 反應物半徑    
T = 700                     # 絕對溫度
mass = 4e-3 / 6e23          # 質量
dt = 1e-4                   # 時間步長
t=0                         # 時間

# 創建顯示窗口
scene = canvas(title='分子運動模擬',
               width=800, height=600,
               center=vector(5, 5, 0),
               background=color.black, align="left")

# 箱子的尺寸
x_min = 0
x_max = 10
y_min = 0
y_max = 10
z_min = -10
z_max = 10
thickness = 0.1             # 邊界的厚度

# 畫出箱子的邊界
box(pos=vector(5, thickness / 2, 0), size=vector(10, thickness, 20), color=color.gray(0.7), opacity=0.3)        # 底面
box(pos=vector(5, 10 - thickness / 2, 0), size=vector(10, thickness, 20), color=color.gray(0.7), opacity=0.3)   # 頂面
box(pos=vector(5, 5, 10 - thickness / 2), size=vector(10, 10, thickness), color=color.gray(0.7), opacity=0.3)   # 前面
box(pos=vector(5, 5, -10 + thickness / 2), size=vector(10, 10, thickness), color=color.gray(0.7), opacity=0.3)  # 後面
box(pos=vector(thickness / 2, 5, 0), size=vector(thickness, 10, 20), color=color.gray(0.7), opacity=0.3)        # 左面
box(pos=vector(10 - thickness / 2, 5, 0), size=vector(thickness, 10, 20), color=color.gray(0.7), opacity=0.3)   # 右面

# 生成 100x3 的速度陣列
def maxwell_boltzmann_velocity_array(T, mass, size=(N_particals, 3)):
    k_B = 1.38e-23                                 # 玻爾茲曼常數，單位：J/K
    sigma = np.sqrt(k_B * T / mass)                # 計算速度分佈的標準差
    velocities = np.random.normal(0, sigma, size)  # 生成符合正態分佈的速度分量
    return velocities

velocities = maxwell_boltzmann_velocity_array(T, mass)
# 將速度轉換為 VPython 的 vector
velocities_vpython = [vector(v[0], v[1], v[2]) for v in velocities]

# 創建分子球體
molecules = []      # 反應物容器
product = []        # 生成物容器

# 賦予隨機位置
positions = np.random.uniform(molecule_size, 10-molecule_size, (N_particals, 3))

for pos in positions:
    molecule = sphere(pos=vector(pos[0], pos[1], pos[2]), radius=molecule_size, 
                      color=color.red, velocity =vector(0,0,0), mass=m)
    molecules.append(molecule)

for i in range(len(molecules)):
    molecules[i].velocity = velocities_vpython[i]

# 彈性碰撞
def handle_collision(molecules1, molecules2):
    m1, m2 = m, m
    v1 = molecules1.velocity
    v2 = molecules2.velocity
    x1 = molecules1.pos                         #位置
    x2 = molecules2.pos                         #位置             
    
    v12 = v1 - v2
    r12 = x1 - x2 
    n = norm(r12)                               # 單位向量
    v12n = dot(v12, n)                          

    u1 = v1 - (2 * m2 / (m1 + m2)) * v12n * n   # 新速度
    u2 = v2 + (2 * m1 / (m1 + m2)) * v12n * n   # 新速度
    
    molecules1.velocity = u1
    molecules2.velocity = u2

# 計算動能
def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * mag2(velocity)

# 動能轉速度
def kinetic_energy_to_velocity(molecule1,molecule2):
    v1 = vector(molecule1.velocity.x, molecule1.velocity.y, molecule1.velocity.z)
    v2 = vector(molecule2.velocity.x, molecule2.velocity.y, molecule2.velocity.z)
    v12 = v1 + v2
    v_new = v12 / 2
    return(v_new)

# 檢查反應條件
def check_reaction_conditions(molecule1, molecule2, threshold_ke):
    ke1 = calculate_kinetic_energy(m, molecule1.velocity)   # 分子1動能
    ke2 = calculate_kinetic_energy(m, molecule2.velocity)   # 分子2動能
    total_ke = ke1 + ke2                               

    if total_ke >= threshold_ke:                            # 檢查動能是否大於活化能
        return True
    return False

# 執行反應
def perform_reaction(molecule1, molecule2):
    new_velocity = kinetic_energy_to_velocity(molecule1, molecule2) # 新速度
    new_pos = (molecules[i].pos + molecules[j].pos) / 2             # 新位置
    new_size = 2 * molecule_size                                    # 新半徑
    product.append(sphere(radius=new_size, color=color.cyan, pos=new_pos, 
                          velocity=new_velocity, mass=2*m))         #新增生成物到product

# 粒子數對時間圖
paricals_graph = graph(title="粒子數對時間圖", xtitle="時間", ytitle="粒子數", align="left")
molecule_amount = gcurve(color=color.red, graph=paricals_graph)          # 反應物數量
product_amount = gcurve(color=color.cyan, graph=paricals_graph)     # 生成物數量

# 倒數對時間圖
Rgraph = graph(title="test", xtitle="時間", ytitle="1/粒子數", align="left")
molecule_r_amount = gcurve(color=color.green, graph = Rgraph)

# k的標籤
k_list = []
k_average = 0
k_label = label(pos=vector(10,10,0,), text = k_average, 
                xoffset=20, yoffset=50, space=30, 
                height=16, border=4, font='sans')
update_k_list = True

# 溫度標籤
T_text = (f"Temperature {T}K")
T_label = label(pos=vector(10,0,0,), text = T_text, 
                xoffset=20, yoffset=50, space=30, 
                height=16, border=4, font='sans')

for i in range(len(molecules)):
        molecules[i].velocity = velocities_vpython[i]

# 主循環
while t < 2:
    rate(1000)
    t += dt
    previous_molecule_amount = len(molecules)

    # 反應物撞牆處理
    for i in range(len(molecules)):
        # 更新位置
        molecules[i].pos += molecules[i].velocity * dt
        if molecules[i].pos.x - molecule_size <= x_min or molecules[i].pos.x + molecule_size >= x_max:
            molecules[i].velocity.x = -molecules[i].velocity.x  # x 方向反彈
        if molecules[i].pos.y - molecule_size <= y_min or molecules[i].pos.y + molecule_size>= y_max:
            molecules[i].velocity.y = -molecules[i].velocity.y  # y 方向反彈
        if molecules[i].pos.z - molecule_size <= z_min or molecules[i].pos.z + molecule_size>= z_max:
            molecules[i].velocity.z = -molecules[i].velocity.z  # z 方向反彈

    # 生成物撞牆處理
    for i in range(len(product)):
        # 更新位置
        product[i].pos += product[i].velocity * dt

        # 碰到箱子邊界的反彈處理
        if product[i].pos.x - 2*molecule_size <= x_min or product[i].pos.x + 2*molecule_size >= x_max:
            product[i].velocity.x = -product[i].velocity.x  # x 方向反彈
        if product[i].pos.y - 2*molecule_size <= y_min or product[i].pos.y + 2*molecule_size>= y_max:
            product[i].velocity.y = -product[i].velocity.y  # y 方向反彈
        if product[i].pos.z - 2*molecule_size <= z_min or product[i].pos.z + 2*molecule_size>= z_max:
            product[i].velocity.z = -product[i].velocity.z  # z 方向反彈


    # 反應 or 碰撞 迴圈
    # 遍歷所有反應物
    for i in range(len(molecules)):     
        for j in range(i + 1, len(molecules)):
            if mag(molecules[i].pos - molecules[j].pos) < 2*molecule_size:      # 檢查是否碰到
                if check_reaction_conditions(molecules[i], molecules[j], Ea):   # 檢查反應條件
                    perform_reaction(molecules[i], molecules[j])                # 執行反應
                    molecules.pop(j)
                    molecules.pop(i)
                    break
                else:
                    handle_collision(molecules[i], molecules[j])                # 動能不足，進行彈性碰撞

    # 更新k_label
    rate_of_reaction = (previous_molecule_amount - len(molecules)) / dt
    k = rate_of_reaction / len(molecules)
    
    if k > 0 and update_k_list == True :
        k_list.append(k)
        k_average = round(sum(k_list) / int(len(k_list)), 3)

    # 取前40比非0的資料
    if len(k_list) == 25:
        print(f"The average of k = {k_average}")
        update_k_list = False           # 停止更新k_average
        k_list.append(k_average)        # 防止重複輸出 
    
    k_label.text = (f"The average of k = {k_average}")

    # 更新粒子數對時間關係圖
    if t < 4.5e-2:
        molecule_amount.plot(pos=(t,len(molecules)))
        product_amount.plot(pos=(t,len(product)))
    if update_k_list:
        molecule_r_amount.plot(t, 1/len(molecules))

