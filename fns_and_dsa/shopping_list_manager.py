shopping_list = []
def add_item(item):
    shopping_list.append(item)
    print(f'"{item}" has been added to the shopping list.')

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove
        print(f"{item} has been removed from the shopping list")
    else:
        print("Item not found")

def display_list():
    print("Shopping List: ")
    for item in shopping_list:
        print(f"{item}")
