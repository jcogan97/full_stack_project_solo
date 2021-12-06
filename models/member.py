from models import membership


class Member:
    
    def __init__(self, first_name, last_name, membership, wallet = 10, id = None):
        
        self.first_name = first_name
        self.last_name = last_name
        self.membership = membership
        self.classes_remaining = membership.free_classes
        self.wallet = wallet
        self.id = id
        
        # self.membership_ids = ["Free", "Silver", "Gold"]
        
    def decrease_remaining_classes(self):
        if self.classes_remaining is not 0:
            self.classes_remaining -= 1
    
    def payment(self, fee):
        if self.sufficient_funds(fee):
            self.wallet -= fee
        else:
            return False
        
    def refund(self, fee):
        self.wallet += fee
        
    def sufficient_funds(self, fee):
        return self.wallet >= fee
        
    def membership_logic(self):
        pass