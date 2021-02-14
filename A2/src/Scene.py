## @file
#  @author
#  @brief
#  @date
#  @details


from Shape import Shape
from scipy import *


class Scene:
    
    def __init__(self, s, Fx, Fy, vx, vy):
        self.s = s
        self.Fx = Fx
        self.Fy = Fy
        self.vx = vx
        self.vy = vy
        
    def get_shape(self):
        return self.s
    
    def get_unbal_forces(self):
        return self.Fx, self.Fy
    
    def get_init_velo(self):
        return self.vx, self.vy
    
    def set_shape(self, s):
        self.s = s
    
    def set_unbal_forces(self, Fx, Fy):
        self.Fx = Fx
        self.Fy = Fy
        
    def set_init_velo(self, vx, vy):
        self.vx = vx
        self.vy = vy
        
        
    def __ode(self, w, t):
        t = [w[2], w[3], self.s.Fx(t)/self.s.mass(), self.s.Fy(t)/self.s.mass]   
    
    
    def sim(self, tfinal, nsteps):
        t = []
        for i in range(nsteps):
            t.append(i.tfinal/(nsteps - 1))
            
        return t, odeint(self.ode, [self.s.cm_x(), self.s.cm_y(), self.vx, self.vy], t)
        
    
    
        
    