from quest_node import quest_node

class quest_tree:
    def __init__(self):
        self.head = None

    def append(self, name):
        new_node = quest_node(name)

        # If the list is empty, make the new node the head
        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            # Find the last node in the list
            while current.next:
                current = current.next

            # Append the new node to the end
            current.next = new_node

    def set_subquest(self, parent_name, child_name):
        new_child = quest_node(child_name)

        current = self.head
        while current and current.name != parent_name:
            current = current.next

        if current:
            current.set_subquest(new_child)
        else:
            print("Parent not found in the list.")

    def traverse(self):
        current = self.head

        while current:
            print(current.name)

            for subquest in current.subquests:
                print("--", subquest.name)

            current = current.next