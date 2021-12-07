class Member:
    
    def __init__(self, first_name, last_name, membership, wallet = 10, classes_remaining = 0, id = None):
        
        self.first_name = first_name
        self.last_name = last_name
        self.membership = membership
        self.classes_remaining = classes_remaining
        self.wallet = wallet
        self.id = id
        
        # self.membership_ids = ["Free", "Silver", "Gold"]
        
    def decrease_remaining_classes(self):
        if self.classes_remaining > 0:
            self.classes_remaining -= 1
    
    def payment(self, fee):
        self.wallet -= fee
        
    def refund(self, fee):
        self.wallet += fee
        
    def sufficient_funds(self, fee):
        return self.wallet >= fee
    
    def remaining_classes(self):
        if self.classes_remaining != 0:
            return False
        else:
            return True
        
    def set_membership(self, membership):
        self.classes_remaining += membership.free_classes
        self.membership = membership