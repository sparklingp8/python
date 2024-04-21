class Stack:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.top = -1
        self.dataArray = []

    def currentSize(self):
        if self.top == -1:
            return 0
        else:
            return self.top + 1

    def push(self, data) -> None:
        self.dataArray.append(data)
        print("data pushed")
        self.top += 1

    def pop(self):
        if self.top >= 0:
            popped = self.dataArray[self.top]
            self.top -= 1
            print(popped, " has been popped")
            return popped
        else:
            print("List is empty, nothing to pop")
            return None

    def elements(self) -> list:
        l: list = []
        for i in range(self.top, -1, -1):
            l.append(self.dataArray[i])
        return l

    def peek(self):
        if self.top == -1:
            print("list is empty nothing to show")
            return None
        else:
            print("top element is :", self.dataArray[self.top])
            return self.dataArray[self.top]


def main():
    my_stack = Stack(5)
    choice = -1

    while choice != 5:
        try:
            print("1. push\n2. pop\n3. size\n4. peek\n5. quit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                if my_stack.top < my_stack.maxsize - 1:
                    data = input("Enter your dat: ")
                    my_stack.push(data)
                else:
                    print("sorry, stack is full")
            elif choice == 2:
                my_stack.pop()
            elif choice == 3:
                print("current size of stack is ", my_stack.currentSize())
                print(my_stack.elements())
            elif choice == 4:
                my_stack.peek()
            elif choice == 5:
                print("-------------------\nThank you")
            else:
                print("choose correct value")
        except ValueError:
            print("Choose between 1-5")


if __name__ == "__main__":
    main()
