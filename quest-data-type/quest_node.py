class quest_node:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.subquests = []

    def set_next_quest(self, next):
        self.next = next

    def set_subquest(self, subquest):
        self.subquests.append(subquest)
    