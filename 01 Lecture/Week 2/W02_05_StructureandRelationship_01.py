"""
Generalization between classes
    is-a relationship
    Inheritance relationship
    Customer -> Person
        From subclass
        To superclass
        Direction of generalization
    Hollow triangle shape
Base class
    Person
Leaf class
    Park::Customer
"""

"""
Association between classes
    has-a relationship
    Member variables
        A customer has a number of holding accounts
        An account has an account holder customer
    Simple line
    If a simple arrow is added
        A customer has a reference to bank accounts
        A bank account has a reference to a customer
        Navigability
    Line ends are tagged by roles
        Account holder
        Holding accounts
        With prefix showing the visibility
            + : public, - : private, # : protected     
"""

class Customer():
    ID = "No one"
    lstAccounts = []
    def addBankAccount(self,account):
        self.lstAccounts.append(account)

class BankAccount():
    strAccountHolder = "No one"
    def changeAccountHolder(self,holder):
        self.strAccountHolder = holder