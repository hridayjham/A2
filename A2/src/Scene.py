## @file Scene.py
#  @author Hriday Jham
#  @brief Contains a class Scene which calculates the
#  required fields to simulate the physics of a scene
#  where an object moves through 2D space.
#  @date 02/16/2021
#  @details Contains functions necessary for 2D Simulation
#  when given a Shape


from scipy.integrate import odeint

## @brief Scene is used to represent the simulation of a
#  scene where an object moves through 2D space


class Scene:

    ## @brief constructor for class Scene.
    #  @param s an object of type Shape
    #  @param Fx a function which takes a real number and returns
    #  a real number
    #  @param Fy a function which takes a real number and returns
    #  a real number
    #  @param vx a real number
    #  @param vy a real number
    def __init__(self, s, Fx, Fy, vx, vy):
        self.s = s
        self.Fx = Fx
        self.Fy = Fy
        self.vx = vx
        self.vy = vy

    ## @brief returns the shape object
    #  @return a Shape object returning the shape

    def get_shape(self):
        return self.s

    ## @brief returns the functions representing the unbalanced forces
    #  @return a function representing the unbalanced forces on x axis
    #  @return a function representing the unbalanced forces on y axis

    def get_unbal_forces(self):
        return self.Fx, self.Fy

    ## @brief returns the initial velocities along the x and y axes
    #  @return a real number representing the initial velocity along the x axis
    #  @return a real number representing the initial velocity along the y axis
    def get_init_velo(self):
        return self.vx, self.vy

    ## @brief setter that sets the Shape
    #  @param s an object of type Shape
    def set_shape(self, s):
        self.s = s

    ## @brief setter that sets the unbalanced forces functions
    #  @param Fx a function that takes a real object and returns a real object
    #  @param Fy a function that takes a real object and returns a real object
    def set_unbal_forces(self, Fx, Fy):
        self.Fx = Fx
        self.Fy = Fy

    ## @brief setter that sets the initial velocities along both axes
    #  @param vx the initial velocity along x axis
    #  @param vy the initial velocity along y axis
    def set_init_velo(self, vx, vy):
        self.vx = vx
        self.vy = vy

    ## @brief function to be used as an input for calling odeint in function sim
    #  @param w a sequence of real numbers of length 4
    #  @param t a real number representing the time
    #  @return a sequence of real numbers of length 4
    def __ode(self, w, t):
        t = [w[2], w[3], self.Fx(t) / self.s.mass(), self.Fy(t) / self.s.mass()]
        return t

    ## @brief calculates the final values to be plotted for the simulation
    #  @param tfinal a real number representing the final time
    #  @param nsteps an integer representing the number of steps
    #  @return a sequence of real numbers
    #  @return a nested sequence of real numbers with each inner sequence of length 4
    def sim(self, tfinal, nsteps):
        t = []
        for i in range(nsteps):
            t.append(i * tfinal / (nsteps - 1))

        return t, odeint(self.__ode, [self.s.cm_x(), self.s.cm_y(), self.vx, self.vy], t)
