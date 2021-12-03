class GymClass:
    
    def __init__(self, description, duration, available_slots, type, id = None):
        
        self.description = description
        self.duration = duration
        self.available_slots = available_slots
        self.type = type
        self.id = id