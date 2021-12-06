class GymClass:
    
    def __init__(self, description, duration, available_slots, type, entry_fee = 5, id = None):
        
        self.description = description
        self.duration = duration
        self.available_slots = available_slots
        self.type = type
        self.entry_fee = entry_fee
        self.id = id