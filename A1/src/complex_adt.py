## @file complex_adt.py
#  @author 
#  @brief 
#  @date 

class ComplexT: 
    x = 0.0
    y = 0.0
      
    # parameterized constructor 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y

    def real(self):
        return self.x

    def imaf(self):
        return self.y

     