# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, item_list):
        self.name = name
        self.description = description
        self.item_list = item_list
    
    def __str__(self):
        return f'Room: {self.name} \n Description: {self.description} \n'

    def remove_item(self, item):
        self.item_list.remove(item)

    def add_item(self, item):
        self.item_list.append(item)