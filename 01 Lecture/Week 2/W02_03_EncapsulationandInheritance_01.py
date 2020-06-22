"""
Encapsulation
    Object = Data + Behavior
        Data : field, member variable, attribute
        Behavior : method, member function, operation
    Delegating the implementation responsibility
        Bring me a sausage, and I don't care how you made it
    Utilizing the visibility
        private: seen only within the class
        protected: seen only within the class and its descendants
        public: seen everywhere
    Python does not support the visibility options
"""

"""
Inheritance
    Inheritance
        Giving my attributes to my descendants
            My attributes include
                Member variables
                Methods
            My descendants may have new attributes of their own
            My descendants may mask the received attributes
            But, if not specified, sons follow their father
    Superclass
        My ancestors, specifically my father
        Generalized from the conceptual view
    Subclass
        My descendants, specifically my son
        Specialized from the conceptual view
    How about having a mother?
        Yes. It is possible in Python        
"""

class Father():
    strHometown = "Jeju"
    def __init__(self):
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
    def __init__(self):
        super(Child, self).__init__()
        # super(Child, self).doFatherThing()
        super(Child, self).doMotherThing()
        print("Child is created")
    def doRunning(self):
        print("Fast")


me = Child()
me.doFatherThing()
me.doMotherThing()
me.doRunning()
print(me.strHometown)
print(me.strName)