class Member:
    # def __init__(self, first_name, last_name, membership = "Free", wallet = 10, id = None):
    def __init__(self, first_name, last_name, membership_id, wallet = 10, id = None):
        
        self.first_name = first_name
        self.last_name = last_name
        self.membership = membership_id
        self.wallet = wallet
        self.id = id
        
        # self.membership_types = ["Free", "Silver", "Gold"]
        
    def pay_membership(self, fee):
        if self.sufficient_funds(fee):
            self.wallet -= fee
        
    def refund(self, fee):
        self.wallet += fee
        
    def sufficient_funds(self, fee):
        return self.wallet >= fee
        
    def membership_logic(self):
        pass