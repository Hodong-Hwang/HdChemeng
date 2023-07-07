import numpy as np
class Diff2DSimple:
    """_summary_
    Simple 2D Diff Scheme
    
    """
    def __init__(self,domain_size:float,Num_Node:int) -> None:
        self.element_length = domain_size / (Num_Node - 1)
        
    def central_difference_x(self,f:np.array):
        diff = np.zeros_like(f)
        diff[1:-1, 1:-1] = (
            f[1:-1, 2:  ]
            -
            f[1:-1, 0:-2]
        ) / (
            2 * self.element_length
        )
        return diff
    def central_difference_y(self,f:np.array):
        diff = np.zeros_like(f)
        diff[1:-1, 1:-1] = (
            f[2:  , 1:-1]
            -
            f[0:-2, 1:-1]
        ) / (
            2 * self.element_length
        )
        return diff
    
    def laplace(self,f:np.array):
        diff = np.zeros_like(f)
        diff[1:-1, 1:-1] = (
            f[1:-1, 0:-2]
            +
            f[0:-2, 1:-1]
            -
            4
            *
            f[1:-1, 1:-1]
            +
            f[1:-1, 2:  ]
            +
            f[2:  , 1:-1]
        ) / (
            self.element_length**2
        )
        return diff