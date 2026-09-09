# Add two polynomials using linked list
class Node:
    def __init__(self, data, power):
        self.data = data
        self.power = power
        self.next = None

    # Update node value
    def updateRecord(self, data, power):
        self.data = data
        self.power = power


class AddPolynomial:
    def __init__(self):
        self.head = None

    # Display given polynomial nodes
    def display(self):
        if self.head == None:
            print("Empty Polynomial ")
            print(" ", end="")

        temp = self.head

        while temp != None:
            if temp != self.head:
                print("+", temp.data, end="")
            else:
                print(temp.data, end="")

            if temp.power != 0:
                print("x^", temp.power, end=" ", sep="")

            temp = temp.next

        print(end="\n")

        def addNode(self, data, power):
        if self.head == None:
            self.head = Node(data, power)
        else:
            node = None
            temp = self.head
            location = None

            while temp != None and temp.power >= power:
                location = temp
                temp = temp.next

            if location != None and location.power == power:
                location.data = location.data + data
                return

            node = Node(data, power)

            if location == None:
                node.next = self.head
                self.head = node
            else:
                node.next = location.next
                location.next = node

    
    def addTwoPolynomials(self, second):
        first = self.head
        second = second.head
        result = None
        tail = None

        while first != None and second != None:
            if first.power > second.power:
                node = Node(first.data, first.power)
                first = first.next

            elif first.power < second.power:
                node = Node(second.data, second.power)
                second = second.next

            else:
                node = Node(first.data + second.data, first.power)
                first = first.next
                second = second.next

            if tail == None:
                tail = node
                result = node
            else:
                tail.next = node
                tail = node

        while first != None:
            node = Node(first.data, first.power)
            first = first.next

            if tail == None:
                tail = node
                result = node
            else:
                tail.next = node
                tail = node

        while second != None:
            node = Node(second.data, second.power)
            second = second.next

            if tail == None:
                tail = node
                result = node
            else:
                tail.next = node
                tail = node

        return result


def main():
    poly1 = AddPolynomial()
    poly2 = AddPolynomial()
    result = AddPolynomial()

    
    poly1.addNode(9, 3)
    poly1.addNode(4, 2)
    poly1.addNode(3, 0)
    poly1.addNode(7, 1)
    poly1.addNode(3, 4)

    
    poly2.addNode(7, 3)
    poly2.addNode(4, 0)
    poly2.addNode(6, 1)
    poly2.addNode(1, 2)

    
    print("\n Polynomial A")
    poly1.display()

    print(" Polynomial B")
    poly2.display()

    result.head = poly1.addTwoPolynomials(poly2)

    
    print(" Result")
    result.display()


if __name__ == "__main__":
    main()
