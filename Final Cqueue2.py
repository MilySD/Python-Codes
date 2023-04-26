import numpy as np

class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = np.empty(k, dtype=np.object)
        self.head = self.tail = -1  # Initilize with -1 not with 0 because 0 is the starting index of array

    def enQueue(self, data):
        if ((self.tail + 1) % self.k == self.head):
            print("Queue is full")

        elif (self.head == -1):  # If its first element
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:  # If its nth element
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    def deQueue(self):
        if (self.head == -1):
            print("Queue is empty")

        elif (self.head == self.tail):  # If it has only one value
            temp = self.queue[self.head]
            self.head = -1  # Reset head
            self.tail = -1  # Reset tail
            return temp
        else:  # If it has nth values
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def display(self):
        if (self.head == -1):
            print("No element in the Queue")
        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            print()
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


def main():
    hasInitilized = False
    obj = ''
    answer = 1
    while answer != 5:
        print("""Menu
        1) Initialise queue.
        2) Add to queue.
        3) Delete from queue.
        4) Display queue.
        5) Exit
        """)

        answer = int(input("Make a selection> "))  # This is the top level program with menu.)
        if answer == 1:
            hasInitilized = True
            obj = CircularQueue(int(input("Enter size of queue: ")))
        if answer == 2:
            if not hasInitilized:
                print("Please Initilize the queue first \n")
            else:
                obj.enQueue(input("Enter Value: "))
        if answer == 3:
            if not hasInitilized:
                print("Please Initilize the queue first \n")
            else:
                temp = obj.deQueue()
                print("Value deQueued : " + str(temp) + " ")
        if answer == 4:
            if not hasInitilized:
                print("Please Initilize the queue first")
            else:
                obj.display()
        if answer == 5:
            print("Bye")


if __name__ == "__main__":
    main()