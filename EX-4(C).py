class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None

    # Function to display the Doubly Linked list
    def display(self):
        if self.head is None:
            print("Empty Doubly Linked List")
        else:
            temp = self.head
            while temp:
                print(temp.data, " --->", end=" ")
                temp = temp.next
            print("None")

    def insert_beginning(self, data):
        n = Node(data)
        temp = self.head
        temp.prev = n
        n.next = temp
        self.head = n

    def insert_end(self, data):
        n = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = n
        n.prev = temp

    def insert_position(self, pos, data):
        n = Node(data)
        temp = self.head
        for i in range(1, pos - 1):
            temp = temp.next
        n.prev = temp
        n.next = temp.next
        temp.next.prev = n
        temp.next = n

    def delete_beginning(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.head.prev = None

    def delete_end(self):
        temp = self.head.next
        before = self.head
        while temp.next is not None:
            temp = temp.next
            before = before.next
        before.next = None
        temp.prev = None

    def delete_position(self, pos):
        temp = self.head.next
        before = self.head
        for i in range(1, pos - 1):
            temp = temp.next
            before = before.next
        before.next = temp.next
        temp.next.prev = before
        temp.next = None
        temp.prev = None


# Driver code
obj = DLL()
n1 = Node(10)
obj.head = n1
n2 = Node(20)
n2.prev = n1
n1.next = n2
n3 = Node(30)
n3.prev = n2
n2.next = n3
n4 = Node(40)
n4.prev = n3
n3.next = n4

print("Created doubly linked list...")
obj.display()

obj.insert_beginning(5)
print("After inserting 5 at the beginning of doubly linked list...")
obj.display()

obj.insert_end(50)
print("After inserting 50 at the end of doubly linked list...")
obj.display()

obj.insert_position(4, 25)
print("After inserting 25 as 4th item of doubly linked list...")
obj.display()

obj.delete_beginning()
print("Deletion at the beginning...")
obj.display()

obj.delete_end()
print("Deletion at the end of doubly linked list...")
obj.display()

obj.delete_position(3)
print("Deleting the 3rd item from doubly linked list...")
obj.display()
