
# Class inheritance

class TestParentClass():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setSize(self, x, y):
        self.size_x = x
        self.size_y = y


class TestChildClass(TestParentClass):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #def setSize(self, x, y):
        #self.size_x = x
        #self.size_y = y

obj = TestChildClass(1, 2)
obj.setSize(3,4)

print(f"{obj.size_x} , {obj.size_y}")




