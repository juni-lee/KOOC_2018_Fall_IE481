"""
self and super
    self : reference variable pointing the instance itself
    super : reference variable pointing the base class instance
        super is used to call the base class methods.
"""

class Father():
    strHometown = "Jeju"
    def __init__(self,paramHome):
        self.strHometown = paramHome
        print("Father is created")
    def doFatherThing(self):
        print("Father's action")
    def doRunning(self):
        print("Slow")

class Mother():
    strHometown = "Seoul"
    def __init__(self):
        print("Mother is created")
    def doMotherThing(self):
        print("Mother's action")

class Child(Mother,Father):
    strName = "Moon"
    def __init__(self,paramName,paramHome):
        paramHome = paramHome
        super(Child, self).__init__(paramHome)
        self.strName = paramName
        print("Child is created")
    def doRunning(self):
        print("Fast")


me = Child("Sun","Universe")
print(me.strName)
