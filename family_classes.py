

class Family:
        def __init__(self, parents=[]):
            self.parents = parents
            self.kids = []

        #def _init_(self, parent1="Dave", parent2=None):
        #above code means if no parameter given for parent1, Dave will be set as parent 1


class Kid:
    def __init__(self, name=None, age = -1):