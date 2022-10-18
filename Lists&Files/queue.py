class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    # Method to add an item to the queue
    def EnQueue(self, item):
        temp = Node(item)
        if self.rear == None:
            self.front = self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp

    # Method to remove an item from queue
    def DeQueue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
        if(self.front == None):
            self.rear = None

    def Output(self):
        temp = self.front
        while temp != None:
            print(temp.data)
            temp = temp.next
        print()

q = Queue()
q.EnQueue("Eli")
q.EnQueue("Jason")
q.EnQueue("Milly")
q.EnQueue("Bob")
q.Output()
q.DeQueue()
q.EnQueue("Adam")
q.Output()
