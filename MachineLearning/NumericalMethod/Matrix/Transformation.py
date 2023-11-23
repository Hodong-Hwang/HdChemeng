import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


# Linear Transformation.

class RotationMatrix:
    def __init__(self,angle):
        self.angle_ =angle
        self.Mat=np.array([[np.cos(angle),np.sin(-angle)],[np.sin(angle),np.cos(angle)]])
        self
    def print(self):
        print(self.Mat)
    def get_Mat(self)->np.array :
        return self.Mat
        
class PointData:
    def __init__(self,xini,xend,Nx,yini,yend,Ny) :
        self.X = np.linspace(xini,xend,Nx)
        self.Y = np.linspace(yini,yend,Ny)
        self.LTFM = np.array([[1,0],[0,1]])
        self.callnums=0
    
    def set_LTFM(self,lstm=np.array):
        self.LTFM=lstm
            
    def data_scatter(self,ax):
        X,Y = np.meshgrid(self.X,self.Y)
        id=X
        for i in range(len(X)):
            for j in range(len(X)):
                X[i][j] = self.LTFM[0,0]*X[i][j]+self.LTFM[0,1]*Y[i][j]
                Y[i][j] = self.LTFM[1,0]*X[i][j]+self.LTFM[1,1]*Y[i][j]        
        ax.scatter(X,Y,c=id,cmap='viridis')
                
        
        

    
if __name__ =="__main__":
    Rot = RotationMatrix(45)        
    Rot.print()
    pd=PointData(0,1,10,0,1,10)
    fig,ax=plt.subplots(2,2)
    
    pd.data_scatter(ax[0,0])
    pd.set_LTFM(Rot.get_Mat())
    pd.data_scatter(ax[0,1])
    #strechss Matrix
    pd.set_LTFM(np.array([[2,0],[0,1]]))
    pd.data_scatter(ax[1,0])
    pd.set_LTFM(0.5*np.array([[3,-1],[1,-1]]))
    pd.data_scatter(ax[1,1])
    plt.show()
    
    
    