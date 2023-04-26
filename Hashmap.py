class HashMap:
    def __init__(self):
        self._buckets = [[] for _ in range(10)]
        self._size = 0
        
    def _hash(self, key):
        return hash(key) % len(self._buckets)
    
    def __len__(self):
        return self._size
    
    def __contains__(self, key):
        idx = self._hash(key)
        return any(key == k for k, _ in self._buckets[idx])
    
    def __getitem__(self, key):
        idx = self._hash(key)
        for k, v in self._buckets[idx]:
            if k == key:
                return v
        raise KeyError(key)
    
    def __setitem__(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self._buckets[idx]):
            if k == key:
                self._buckets[idx][i] = (key, value)
                break
        else:
            self._buckets[idx].append((key, value))
            self._size += 1
    
    def __delitem__(self, key):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self._buckets[idx]):
            if k == key:
                del self._buckets[idx][i]
                self._size -= 1
                return
        raise KeyError(key)
    
    def items(self):
        return [(k, v) for bucket in self._buckets for k, v in bucket]

def add_extension(extension_dict):
    extension = input("Enter a file extension: ")
    program = input("Enter the associated program: ")
    extension_dict[extension] = program
    print(f"Added {extension}: {program} to the dictionary")

def remove_extension(extension_dict):
    extension = input("Enter a file extension to remove: ")
    if extension in extension_dict:
        del extension_dict[extension]
        print(f"Removed {extension} from the dictionary")
    else:
        print(f"{extension} not found in the dictionary")

def view_extensions(extension_dict):
    for extension, program in extension_dict.items():
        print(f"{extension}: {program}")

def find_program(extension_dict):
    extension = input("Enter a file extension to look up: ")
    if extension in extension_dict:
        program = extension_dict[extension]
        print(f"The associated program is {program}")
    else:
        print(f"{extension} not found in the dictionary")

def main():
    extension_dict = HashMap()
    extension_dict["AIFF"] = "VLC Media Player"
    extension_dict["PY"] = "Mu"
    extension_dict["SQL"] = "DB Browser Lite"

    while True:
        print("1. Add a key-value pair to the dictionary")
        print("2. Remove a key-value pair from the dictionary")
        print("3. View the entire contents of the dictionary")
        print("4. Find a value by entering a key")
        print("5. Exit the program")

        choice = input("Enter your choice: ")
        
        if choice == '1':
if __name__ == "__main__":
    main()