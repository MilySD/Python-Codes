class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def print_stack(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

def main():
    stack = LinkedListStack()

    while True:
        print("\nSelect an option:")
        print("1. Add an element to the top of the stack")
        print("2. Remove the top element from the stack")
        print("3. Is the stack empty")
        print("4. View the entire contents of the stack")
        print("5. Exit the program")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter the element to be added: ")
            stack.push(data)
            print(f"Added {data} to the stack.")

        elif choice == '2':
            data = stack.pop()
            if data is None:
                print("Stack is empty.")
            else:
                print(f"Removed {data} from the stack.")

        elif choice == '3':
            if stack.is_empty():
                print("Stack is empty.")
            else:
                print("Stack is not empty.")

        elif choice == '4':
            print("Contents of the stack:")
            stack.print_stack()

        elif choice == '5':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()