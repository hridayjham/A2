## @file
#  @author
#  @brief
#  @date
#  @details

import matplotlib.pyplot as plt

def plot(w, t):
    if len(w) != len(t):
        raise ValueError("Invalid Inputs for plot")
    else:
        x = []
        y = []
        for i in range (len(w)):
            x.append(w[i][0])
            y.append(w[i][1])
            
        fig, axs = plt.subplots(3)
        fig.suptitle('Motion Simulation')
        axs[0].plot(t, x)
        axs[0].set(ylabel = "x (m)")
        axs[1].plot(t, y)
        axs[1].set(ylabel = "y (m)")
        axs[2].plot(x, y)
        axs[2].set(xlabel = "x (m)", ylabel = "y (m)")
        plt.show()