# in the_bank.py
class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, "value"):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount
        
        
class Bank(object):
    """ The Bank"""
    def __init__(self):
        self.accounts = []
    
    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account: Account() new account to append
            @return True if success, False if an error occured
        """
        try:
            if not isinstance(new_account, Account):
                raise Exception("ERROR: Account must be of type Account.")
            if (len([a for a in self.accounts if a.name == new_account.name])):
                raise Exception("ERROR: Account with name {name} already exists.".format(name=new_account.name))
            self.accounts.append(new_account)
            return True
        except Exception as err:
            print(err)
            return False
        

valid_account_Alice = Account("Alice", value=100.) 
valid_account_Bob = Account("Bob", value=100.)
bank = Bank()

bank.add(valid_account_Alice)
bank.add(valid_account_Bob)

# METHODS INTERESANTES:

# methods = set([m if not m.startswith("_") else "" for m in dir(bank)])
# methods.discard("")
# print(methods)
# print([a.name for a in bank.accounts].index("Alice"))
# print([a.name for a in bank.accounts].index("Bob"))

