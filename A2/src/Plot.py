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
        for i in w:
            x.append(w[i][0])
            y.append(w[i][1])
            
        a = plt.plot(x, t)
        a.show()
        b = plt.plot(y, t)
        b.show()
        c = plt.plot(y, x)
        
        plt.show()