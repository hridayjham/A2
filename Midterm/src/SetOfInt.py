## @file SetOfInt.py
#  @author Hriday Jham
#  @brief Set of integers
#  @date 03/04/2021


class SetOfInt:
    
    #Constructor for SetOfInt
    def __init__(self, xs):
        set1 = []
        for x in xs:
            set1.append(x)
        self.s = set(set1)
    
    #returns whether x is a member of the set    
    def is_member(self, x):
        return x in self.s
    
    #returns the set as a sequence
    def to_seq(self):
        return list(self.s)
    
    #returns the union of the set with the set taken as parameter
    def union(self, t):
        self_list = self.to_seq()
        t_list = t.to_seq()
        for i in t_list:
            self_list.append(i)
        return SetOfInt(self_list)
    
    #Returns the disjunction of complement. i.e. Integers which are in 
    #one set but not the other
    def diff(self, t):
        self_list = self.to_seq()
        t_list = t.to_seq()
        new_list = []
        for i in self_list:
            if i not in t_list:
                new_list.append(i)
        for x in t_list:
            if x not in self_list:
                new_list.append(x)
        return SetOfInt(new_list)
    
    #returns size of set
    def size(self):
        return len(self.s)
    
    #returns whether set is empty
    def empty(self):
        return self.size() <= 0
    
    #checks whether two sets are equal
    def equals(self, t):
        flag = True
        for i in self.s:
            if i in t.to_seq() == False:
                flag = False
        return flag
        