class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def show(self):
        if self.isEmpty():
            print("Empty stack")
        else: # from top
            print("Stack contents: ", end='')
            for i in range(self.size()):
                print(self.items[i], end=' ')
            print()

s = Stack()
s.push('hello')
s.push('true')
print(s.pop())
s.show()
