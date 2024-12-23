
1. Consistency
* Truncation error : |discretized equation - the exact| $\to 0$ for a method to be consistent.  
기본적으로 $\Delta t \to 0, \Delta x \to 0$ 조건에서 error는 0으로 수렴. error는 $\Delta t^n, \Delta x^n$ n차 에러, 즉  n>0 인게 consistency에 조건에 해당함. x,t 항에 대해서 연관된 경우 두가지 항 비율로 인해서 consistency 문제가 발생할 수 있음. $\Delta x$, $\Delta t$ appropriate ratio to go to zero.
2. Stability

* Exact solution -> bounded -> the method proudced a bounded solution. stable 하다는 것은 diverge 하지 않다는 것입니다. BC나 nolniearity가 존재한다면 iterative stable method는 .. 조사가 어렵다. 그래서 이러한 제약조건을 제한하고 조사하는 것이 일반적이다. The most widely used approach to studying stability of numerical schemes is the
**von Neumann’s method.**

3. Convergence
* grid size -> 0으로 수렴할 때, 이산화 된 해가 exact solution으로 수렴한다면 우리는 Convergence 하다고 말한다. For linear intial value problems, the *The lax equivalence thoerem* 은 잘 주어진 IVP 와 FD가정에 따라서 consistency를 잘 만족 할 수 있다. 명백하게도, solution method가 converges 하지 않다면, cosnsitent shceme은 필요없다.  
* 비선형 문제에 있어서 BC에 따라서 Convergence 문제는 발생한다. stability and convergence of a method are difficult to demsotrate. Tehrefore, convergence is usally checked using numerical experiments. repeating the calculation on a series of successively refined grids. 
4. Consrvation
* 

5. Boundedness
6. Realizabilty
7. Accuracy