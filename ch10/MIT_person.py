from Person import Person

# Figure 10-4 from page 192
class MIT_person(Person):
    
    _next_id_num = 0 #identification number
    
    def __init__(self, name):
        super().__init__(name)
        self._id_num = MIT_person._next_id_num
        MIT_person._next_id_num += 1
        
    def get_id_num(self):
        return self._id_num
    
    def __lt__(self, other):
        return self._id_num < other._id_num


if __name__ == "__main__":
    # # Code from page 192
    p1 = MIT_person('Barbara Beaver')
    print(str(p1) + '\'s id number is ' + str(p1.get_id_num()))
    
    print()
    
    # # Code from page 193
    p1 = MIT_person('Mark Guttag')
    p2 = MIT_person('Billy Bob Beaver')
    p3 = MIT_person('Billy Bob Beaver')
    p4 = Person('Billy Bob Beaver')
    
    print('p1 < p2 =', p1 < p2) # Uses MIT_person __lt__
    print('p3 < p2 =', p3 < p2) # Uses MIT_person __lt__
    
    # First argument of expression is used to determine 
    # __lt__ method to invoke:
    # p4.__lt__(p1) --> Uses Person __lt__ --> Order by name
    print('p4 < p1 =', p4 < p1) 
    
    # p1.__lt__(p4) --> AttributeError p4 has no attribute '_id_num'
    # print('p1 < p4 =', p1 < p4)