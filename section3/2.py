# Que.02
# Create a Python class named "DictOperations" with methods to manipulate dictionaries, including:
# (a) Adding a key-value pair to the dictionary.
# (b) Removing a key-value pair from the dictionary.
# (c) Updating the value associated with a specific key.
# (d) Checking if a key exists in the dictionary.
# (e) Retrieving all keys or values from the dictionary


class DictOperations:
    def __init__(self):
        self.dictionary = {}

    def add_pair(self, key, value):
        self.dictionary[key] = value
        print(f"Key-value pair ({key}: {value}) added successfully.")

    def remove_pair(self, key):
        if key in self.dictionary:
            del self.dictionary[key]
            print(f"Key '{key}' removed successfully.")
        else:
            print(f"Key '{key}' not found in the dictionary.")

    def update_value(self, key, new_value):
        if key in self.dictionary:
            self.dictionary[key] = new_value
            print(f"Value associated with key '{key}' updated to '{new_value}'.")
        else:
            print(f"Key '{key}' not found in the dictionary.")

    def check_key(self, key):
        if key in self.dictionary:
            print(f"Key '{key}' exists in the dictionary.")
        else:
            print(f"Key '{key}' does not exist in the dictionary.")

    def get_keys(self):
        keys = list(self.dictionary.keys())
        print("Keys in the dictionary:", keys)

    def get_values(self):
        values = list(self.dictionary.values())
        print("Values in the dictionary:", values)


dict_ops = DictOperations()

while True:
    print("\nChoose an operation:")
    print("1. Add a key-value pair")
    print("2. Remove a key-value pair")
    print("3. Update the value associated with a key")
    print("4. Check if a key exists")
    print("5. Retrieve all keys from the dictionary")
    print("6. Retrieve all values from the dictionary")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        dict_ops.add_pair(key, value)
    elif choice == '2':
        key = input("Enter the key to remove: ")
        dict_ops.remove_pair(key)
    elif choice == '3':
        key = input("Enter the key to update: ")
        new_value = input("Enter the new value: ")
        dict_ops.update_value(key, new_value)
    elif choice == '4':
        key = input("Enter the key to check: ")
        dict_ops.check_key(key)
    elif choice == '5':
        dict_ops.get_keys()
    elif choice == '6':
        dict_ops.get_values()
    elif choice == '7':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid choice.")
