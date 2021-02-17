## @file Shape.py
#  @author Hriday Jham
#  @brief An interface for modules that implement Shape
#  @date 02/16/2021

from abc import ABC, abstractmethod

## @brief Shape provides an interface for shapes
#  @details The method in the interface are abstract and need to be
#  overridden by the modules that inherit this interface


class Shape(ABC):

    @abstractmethod
    ## @brief a generic method for returning the centre of mass
    #  along the x axis
    #  @return a real number indicating the centre of mass along the
    #  x axis
    def cm_x(self):
        pass

    @abstractmethod
    ## @brief a generic method for returning the centre of mass
    #  along the y axis
    #  @return a real number indicating the centre of mass along the
    #  y axis
    def cm_y(self):
        pass

    @abstractmethod
    ## @brief a generic method for returning the mass of the shape
    #  @return a real number indicating the mass of the shape
    def mass(self):
        pass

    @abstractmethod
    ## @brief a generic method for returning the moment of inertia of the shape
    #  @return a real number indicating the moment of inertia of the shape
    def m_inert(self):
        pass
