# 10.1 Abstract Data Types and Classes

import datetime

# Figure 10-3 Class Person
class Person(object):
    
    def __init__(self, name):
        """Assumes name a string. Create a person"""
        self._name = name
        try:
            last_blank = name.rindex(' ')
            self._last_name = name[last_blank+1:]
        except:
            self._last_name = name
        self.birthday = None
        
    def get_name(self):
        """Returns self's full name"""
        return self._name
    
    def get_last_name(self):
        """Returns self's last name"""
        return self._last_name
    
    def set_birthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
           Sets self's birthday to birthdate"""
        self._birthday = birthdate
        
    def get_age(self):
        """Returns self's current age in days"""
        if self._birthday == None:
            raise ValueError
        return (datetime.date.today() - self._birthday).days
    
    def __lt__(self, other):
        """Assume other a Person
           Returns True if self precedes other in alphabetical
           order, and False otherwise. Comparison is based on last
           names, but if these are the same full names are
           compared."""
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name
    
    def __str__(self):
        """Returns self's name"""
        return self._name

if __name__ == "__main__":
    # Code from page 188
    me = Person('Michael Guttag')
    him = Person('Barack Hussein Obama')
    her = Person('Madonna')
    print(him.get_last_name())
    him.set_birthday(datetime.date(1961, 8, 4))
    her.set_birthday(datetime.date(1958, 8, 16))
    print(him.get_name(), 'is', him.get_age(), 'days old')
    
    print()
    
    # Code from page 190
    p_list = [me, him, her]
    for p in p_list:
        print(p)
    
    print()
    
    p_list.sort()
    for p in p_list:
        print(p)
