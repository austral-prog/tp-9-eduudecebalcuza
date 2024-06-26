
def create_inventory(items):
    inventory = dict()
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def add_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def decrement_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] -= 1
        else:
            inventory[item] = 1
        if inventory[item] <= 0:
            inventory[item] = 0
    return inventory


def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventory


def list_inventory(inventory):
    my_list = []
    for item in inventory.items():
        key, value = item
        if value > 0:
            my_list.append((item))
    return my_list
