class myParent(object):
    parentNumberStatic = 10

    def __init__(self):
        self.parentNumber = 5

    def inheritedFromParent(self):
        return 7

class myChild(myParent):
    def __init__(self, childNum):
        super(myChild, self).__init__() #only works for new style classes (parents need to inherit from object)
        #myParent.__init__(self)
        self.childNumber = childNum

    def multiplyNumbers(self):
        #print myParent.parentNumber * self.childNumber #myParent has not attr parentNumber
        #print myParent.parentNumberStatic * self.childNumber #dont even need inheritance to access a static member of the parent
        print self.parentNumber * self.childNumber #not possible w/o calling parent's __init__

c = myChild(10)
c.multiplyNumbers()
print c.parentNumberStatic
print myParent.parentNumberStatic
print c.inheritedFromParent()
