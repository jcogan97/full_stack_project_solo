class Member:
    def __init__(self, first_name, last_name, membership = "None", wallet = 10, id = None):
        
        self.first_name = first_name
        self.last_name = last_name
        self.membership = membership
        self.wallet = wallet
        self.id = id
        
    def pay_membership(self, fee):
        self.wallet -= fee