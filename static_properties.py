class myParent(object):
    parentNumberStatic = 10

    def inheritedFromParent(self):
        return myParent.parentNumberStatic

class myChild(myParent):
    def __init__(self, childNum):
        super(self.__class__, self).__init__() #only works for new style classes (parents need to inherit from object)
        self.childNumber = childNum

    def childOnly(self):
        return myParent.parentNumberStatic

c = myChild(10)
print c.parentNumberStatic
print myParent.parentNumberStatic
print c.inheritedFromParent()
print c.childOnly()

