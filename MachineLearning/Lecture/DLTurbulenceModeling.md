Turbulence Moeling in the age of data
 -> key advances to this field of turbulence models with machine learing

 Karthik Durasiamy is expert turbulence modelers 

 RANS, LES, 

 mean drags. 


 coarser grid

 NN -

RANS
$$
\frac{\partial U }{\partial t} + (\bf{u} \cdot \nabla)\bf{u} = -\nabla(p)+\frac{1}{Re}\nabla^2u\\
\nabla \cdot u =0
$$

여기에서 유속은 평균 유속과 그 주변의 편차로 구분해서 나타낼 수 있다. 수식으로 쓰면 다음과 같이 나타냄.

where
$$
\bf{u}(x,t)=\bar{U(x)}+u'(x,t)
$$

이를 위 비압축성 유동에 적용함녀 다음의 식으로 나타남.
$$
\bf{u}\cdot \nabla = [u,v,w] \cdot [\frac{\partial  }{\partial x},\frac{\partial  }{\partial y},\frac{\partial  }{\partial z}]^T = (u\frac{\partial  }{\partial x}+v\frac{\partial  }{\partial y}+w\frac{\partial  }{\partial z})
$$
$$
\bar{U} +\bf{u}\cdot \nabla \bar{U} + \frac{\partial \bar{u'u'}}{\partial x}
+ \frac{\partial \bar{u'v'}}{\partial y}
+ \frac{\partial \bar{u'w'}}{\partial z} = - \nabla \bar{P} + \frac{1}{Re}\nabla\bar{U}
$$

여기에서 난류가 발생하는 텀은 다음과 같으며, 이를 레이놀즈 stress로 표시함.

$$
\frac{\partial \bar{u'u'}}{\partial x}
+ \frac{\partial \bar{u'v'}}{\partial y}
+ \frac{\partial \bar{u'w'}}{\partial z}
$$

clousre Problem : mean flow profile depends on turbulent fluctuations. >> it's key point to apply machine learning into fluiddyanmics

LES (Large Eddy Simulation)

coarser grid

low pass filtering

inside .. les closure problem

Closure problem : nonlienarity couples scales, so need sub grid scales models.

Kolomogorov Energy Cscade

POPE (1975) 논문 확인해볼 것


RNAS Clousre Model.s

1. first effective viscosity hypothesis was 결국 평균 유속에 비례하도록 난류가 발생할 것이라는 간단한 이론.
$$
\bar{u_1u_2} = \mu_eff U_{12}
$$

POPE Paper


Proper othogonal Decomposition -> Lumley 가 시행. PINN RANS 식이 만족 하도록..

LEVM, QEVM, TBNN -> Tensor Based NN 모델 정확함.

tensor lay times construction the time networks.. 

2016 논문 -> ㄱ


2019,maulik LES maulik,시도해보기

Reinforce Learning, 

2021 (Guido Novati) 
multi agnent rl , interaction .. .


Super Resouliton -> imagme science


coarse grid -> syper grid!!

