from SimpleDiffScheme import Diff2DSimple
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from matplotlib import animation

N_POINTS = 41
DOMAIN_SIZE = 1.0
N_ITERATIONS = 500
TIME_STEP_LENGTH = 0.001
KINEMATIC_VISCOSITY = 0.1
DENSITY = 1.0
HORIZONTAL_VELOCITY_TOP = 1.0

N_PRESSURE_POISSON_ITERATIONS = 50
STABILITY_SAFETY_FACTOR = 0.5
class DataSet2D :
  def __init__(self,domainsize,npoint):        
    self.x = np.linspace(0.0, DOMAIN_SIZE, N_POINTS)
    self.y = np.linspace(0.0, DOMAIN_SIZE, N_POINTS)
    self.X, self.Y = np.meshgrid(self.x, self.y)
    self.u_prev = np.zeros_like(self.X)
    self.v_prev = np.zeros_like(self.X)
    self.p_prev = np.zeros_like(self.X)
    self.u_next = self.u_prev
    self.p_next = self.p_prev
    self.v_next = self.v_prev

data=DataSet2D(DOMAIN_SIZE,N_POINTS)
fig, ax = plt.subplots()
#fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax)
ax.set_xlim((0, 1))
ax.set_ylim((0, 1))
pressure_plot=ax.contourf(data.X[::2, ::2], data.Y[::2, ::2], data.p_next[::2, ::2], cmap="coolwarm")
#velocity_field=ax.quiver(data.X[::2, ::2], data.Y[::2, ::2], data.u_next[::2, ::2], data.v_next[::2, ::2], color="black")
def CFDRun(frame,data:DataSet2D):
    diffscheme=Diff2DSimple(DOMAIN_SIZE,N_POINTS)
    d_u_prev__d_x = diffscheme.central_difference_x(data.u_prev)
    d_v_prev__d_x = diffscheme.central_difference_x(data.v_prev)
    d_u_prev__d_y = diffscheme.central_difference_y(data.u_prev)
    d_v_prev__d_y = diffscheme.central_difference_y(data.v_prev)
    laplace__u_prev = diffscheme.laplace(data.u_prev)
    laplace__v_prev = diffscheme.laplace(data.v_prev)

    # Perform a tentative step by solving the momentum equation without the
    # pressure gradient
    u_tent = (
        data.u_prev
        +
        TIME_STEP_LENGTH * (
            -
            (
                data.u_prev * d_u_prev__d_x
                +
                data.v_prev * d_u_prev__d_y
            )
            +
            KINEMATIC_VISCOSITY * laplace__u_prev
        )
    )
    v_tent = (
        data.v_prev
        +
        TIME_STEP_LENGTH * (
            -
            (
                data.u_prev * d_v_prev__d_x
                +
                data.v_prev * d_v_prev__d_y
            )
            +
            KINEMATIC_VISCOSITY * laplace__v_prev
        )
    )

    # Velocity Boundary Conditions: Homogeneous Dirichlet BC everywhere
    # except for the horizontal velocity at the top, which is prescribed
    u_tent[0, :] = 0.0
    u_tent[:, 0] = 0.0
    u_tent[:, -1] = 0.0
    u_tent[-1, :] = HORIZONTAL_VELOCITY_TOP
    v_tent[0, :] = 0.0
    v_tent[:, 0] = 0.0
    v_tent[:, -1] = 0.0
    v_tent[-1, :] = 0.0


    d_u_tent__d_x = diffscheme.central_difference_x(u_tent)
    d_v_tent__d_y = diffscheme.central_difference_y(v_tent)

    # Compute a pressure correction by solving the pressure-poisson equation
    rhs = (
        DENSITY / TIME_STEP_LENGTH
        *
        (
            d_u_tent__d_x
            +
            d_v_tent__d_y
        )
    )

    for _ in range(N_PRESSURE_POISSON_ITERATIONS):
        data.p_next = np.zeros_like(data.p_prev)
        data.p_next[1:-1, 1:-1] = 1/4 * (
            +
            data.p_prev[1:-1, 0:-2]
            +
            data.p_prev[0:-2, 1:-1]
            +
            data.p_prev[1:-1, 2:  ]
            +
            data.p_prev[2:  , 1:-1]
            -
            diffscheme.element_length**2
            *
            rhs[1:-1, 1:-1]
        )

        # Pressure Boundary Conditions: Homogeneous Neumann Boundary
        # Conditions everywhere except for the top, where it is a
        # homogeneous Dirichlet BC
        data.p_next[:, -1] = data.p_next[:, -2]
        data.p_next[0,  :] = data.p_next[1,  :]
        data.p_next[:,  0] = data.p_next[:,  1]
        data.p_next[-1, :] = 0.0

        data.p_prev = data.p_next
    

    d_p_next__d_x = diffscheme.central_difference_x(data.p_next)
    d_p_next__d_y = diffscheme.central_difference_y(data.p_next)

    # Correct the velocities such that the fluid stays incompressible
    data.u_next = (
        u_tent
        -
        TIME_STEP_LENGTH / DENSITY
        *
        d_p_next__d_x
    )
    data.v_next = (
        v_tent
        -
        TIME_STEP_LENGTH / DENSITY
        *
        d_p_next__d_y
    )

    # Velocity Boundary Conditions: Homogeneous Dirichlet BC everywhere
    # except for the horizontal velocity at the top, which is prescribed
    data.u_next[0, :] = 0.0
    data.u_next[:, 0] = 0.0
    data.u_next[:, -1] = 0.0
    data.u_next[-1, :] = HORIZONTAL_VELOCITY_TOP
    data.v_next[0, :] = 0.0
    data.v_next[:, 0] = 0.0
    data.v_next[:, -1] = 0.0
    data.v_next[-1, :] = 0.0
    pressure_plot=ax.contourf(data.p_next)
    #elocity_field=ax.quiver(data.X[::2, ::2], data.Y[::2, ::2], data.v_next[::2, ::2], color="black")

    # Advance in time
    data.u_prev = data.u_next
    data.v_prev = data.v_next
    data.p_prev = data.p_next
    return pressure_plot,#velocity_field

def test_CFD():
    diffscheme=Diff2DSimple(DOMAIN_SIZE,N_POINTS)
    maximum_possible_time_step_length = (
        0.5 * diffscheme.element_length**2 / KINEMATIC_VISCOSITY
    )
    if TIME_STEP_LENGTH > STABILITY_SAFETY_FACTOR * maximum_possible_time_step_length:
        raise RuntimeError("Stability is not guarenteed")
    anim = animation.FuncAnimation(fig, CFDRun, frames=300, blit=False,fargs={data})
    Writer = animation.writers['pillow']
    writer = Writer(fps=15)
    #anim.run()
    #plt.show()
    # Save the animation
    anim.save('pressure_animation.gif', writer=writer)



    
def main():
    test_CFD()
        
        
if __name__ == "__main__":
    main()