## @file SetOfInt.py
#  @author Your Name
#  @brief Set of integers
#  @date 03/04/2021


class SetOfInt:
    
    def __init__(self, xs):
        set1 = []
        for x in xs:
            set1.append(x)
        self.s = set(set1)
            
    def is_member(self, x):
        return x in self.s
    
    def to_seq(self):
        return list(self.s)
    
    def union(self, t):
        self_list = self.to_seq()
        t_list = t.to_seq()
        for i in t_list:
            self_list.append(i)
        return SetOfInt(self_list)
    
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
    
    def size(self):
        return len(self.s)
    
    def empty(self):
        return self.size() <= 0
    
    def equals(self, t):
        flag = True
        for i in self.s:
            if i in t.to_seq() == False:
                flag = False
        return flag
        