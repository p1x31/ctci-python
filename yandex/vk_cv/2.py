class Parent(object):
    var = [1,2,3]

class Child(Parent):
    def __init__(self):
        try:
            self.var.append(1)
        except:
            this.var = []
a = Child()
b = Child()
print(a.var)