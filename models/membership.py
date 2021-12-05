class Membership:
    def __init__(self, type, cost, free_classes, id = None):
        self.type = type
        self.cost = cost
        self.free_classes = free_classes
        self.id = id