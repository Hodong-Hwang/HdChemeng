_
$A \phi = Q$ 를 푼다고 생각해보자


## Direct Method

* Gauss Elimination (GE)
  * Upper triangle matrix 만드는 과정을 통해서 형성함.
  * 벡터 마지막 해는 $\phi_n = \frac{Q_n}{A_{nn}}$ 
  * 그 마지막 전에 해를 구하면 $\phi_i=\frac{Q_i - \sum_{k=i+1}^nA_{ik}\phi_k}{A_ii}$
* LU decompositon 
  * GE를 보면 삼각형 형태의 Matirx를 구해서 푸는것을 보인다. U를 상삼각, L을 하삼각 Matrix라고함.
  * A=LU 과정을 fatorization 이라고 하고, 이를 유일 하게 만들기 위한 과정은 대각 함수를 1로 만드는 것임.
  * $A=LU \to A\phi=Q \to LU\phi=Q \to U\phi=Y \to LY=Q$ 
* Tridiagnoal System
  * FD (1D) problmes with CDS approximation 계수를 보면 3삼각 형태의 매트릭스를 가진다.
    * $A_W^i \phi_{i-1}+A_p^i\phi_i+A_E^i\phi_{i+1} =Q_i$
  * 이러한 형태의 가우스 소거범을 보자면 다음과 같다.
    * $A_p^i=A_p^i-\frac{A_W^iA_E^{i-1}}{A_p^{i-1}}$ 
    * $Q_i^* = Q_i - A_W^iQ_{i-1}^*/A_P^{i-1}$
    * 이러한 행렬 시스템은 TDMA로 풀림. 
* Cyclid Reduction
  * this allow still greater cost reduction than that offered by TDMA.
  * Cyclic reduction 예제 찾아보기

## Iterative method

the triangular factors of sparse matrices are not sparse, so the cost of these methods is quite high. (The direct method such as GE or LU )

iterative methods are used out of necessity for non linear problems, but tehy are just as valuable for sparese linear systems.


$$

A \phi ^ n = Q - \rho ^n \\
\epsilon ^ n = \phi - \phi ^n \\
A \epsilon ^ n = \rho ^ n
$$

이러한  residual은 다음과 같이 정의됨.
$A \epsilon ^ n = \rho ^ n$ 

해당 방법론은 iteration에서 발생하는 residual을 0으로 수렴시큰것과 같음. consider an interative shceme for a linear system ;

$$
M \phi^{n+1} = N \phi^n + B \\
A = M - N \text{ and } B = Q \\ 
PA = M-N, B=PQ
$$
where P is a non-singular, so-called preconditioning matrix. P is a non-singular, so-called preconditioning matrix

$$
M(\phi^{n+1}-\phi^n) = B - (M-N)\phi^n or M\delta ^n = \rho ^n
$$

* Relaxation Method
  * 외삽 또는 내삽을 하는 방법에 해당함
  * $x^{new}_i = \lambda x_i^{new} + (1-\lambda)x_i^{old}$

* Cholesky Method (Symmetric)
  * conjugate gradient mtehod에서 사용
  * NS나 Convection diffussion problems에서는적용이 어렵다. (해당식은 Symmetric 하지 않음)
* 