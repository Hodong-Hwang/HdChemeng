from fenics import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import svd

# 난류 문제를 위한 매개변수
nx, ny = 64, 64  # 격자의 수
T = 2.0          # 시간의 최대 값
num_steps = 50   # 시간 스텝 수
dt = T / num_steps

# 유체 도메인 및 경계 조건 설정
mesh = UnitSquareMesh(nx, ny)
V = VectorFunctionSpace(mesh, 'P', 2)
u = TrialFunction(V)
v = TestFunction(V) 
bc = [DirichletBC(V, Constant((1, 0)), 'near(x[1], 1)'),
      DirichletBC(V, Constant((0, 0)), 'near(x[1], 0)')]

# 초기 조건 설정
u0 = Expression(('sin(pi*x[1])', '0'), degree=2)
u_n = interpolate(u0, V)
u_n1 = Function(V)

# 알고리즘을 위한 기본 식 설정
F = (1/dt)*dot(u - u_n, v)*dx + dot(dot(u_n, nabla_grad(u_n)), v)*dx + \
    0.01*dot(grad(u), grad(v))*dx - dot(div(u_n)*u_n, v)*dx
a, L = lhs(F), rhs(F)

# 시간에 따른 유체 흐름 계산
for n in range(num_steps):
    # 시간 스텝 진행
    solve(a == L, u_n1, bc)
    
    # 결과 시각화
    plot(u_n1, title='Velocity')
    plt.show()

    # 현재 시간 스텝을 다음으로 업데이트
    u_n.assign(u_n1)

# POD를 위한 데이터 수집
u_values = [interpolate(u_n1, V).vector().get_local()]
for n in range(num_steps - 1):
    solve(a == L, u_n1, bc)
    u_values.append(interpolate(u_n1, V).vector().get_local())

# POD를 위한 데이터 매트릭스 생성
data_matrix = np.array(u_values)

# POD 수행
u_mean = np.mean(data_matrix, axis=0, keepdims=True)
data_matrix_centered = data_matrix - u_mean
u, s, v = svd(data_matrix_centered.T)

# POD 모드 시각화
plt.figure(figsize=(12, 4))
for mode in range(3):  # 상위 3개 모드만 시각화
    plt.subplot(1, 3, mode + 1)
    mode_vector = Function(V)
    mode_vector.vector().set_local(u[:, mode])
    plot(mode_vector, title=f'POD Mode {mode+1}')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

plt.tight_layout()
plt.show()