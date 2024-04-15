# deque (double ended queue)  with double ended linked list

class Node:
    def __init__(self, dat: int):
        self.prev: [None, Node] = None
        self.next: [None, Node] = None
        self.data: int = dat


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


def log(msg: str) -> None:
    print("-" * 30)
    print(f"{msg:^30}")


def intInput(prmpt: str, errmsg: str) -> int:
    val = None
    while val is  None:
        try:
            val = int(input(prmpt))
        except ValueError:
            log(errmsg)
    return val


def pushBeginning(db_list: DoublyLinkedList):
    dat = intInput("Enter data: ", "Only int data is allowed")
    new_node = Node(dat)
    if db_list.head is None:
        db_list.head = new_node
        db_list.tail = new_node
    else:
        new_node.next = db_list.head
        db_list.head.prev = new_node
        db_list.head = new_node
    log(f"{dat} added to beginning of list")
    return db_list.head


def popAtBeginning(db_list: DoublyLinkedList):
    if db_list.head is None:
        log("list is Empty")
    else:
        if db_list.head.next is None:
            db_list.tail = None
            log(f"removed last element {db_list.head.data} from list")
            del db_list.head
            return None
        else:
            db_list.head.next.prev = None
            log(f"removed  {db_list.head.data} element from beginning list")

            db_list.head = db_list.head.next

        return db_list.head


def seeList(db_head: Node):
    if db_head is None:
        log("list is Empty")
    else:
        log("link elements are")
        print("DLNodes: ", db_head.data, end="")
        temp = db_head.next
        while temp:
            print(" <->", temp.data, end="")
            temp = temp.next
        print(" <-> None")


def seeListReverse(db_tail) -> None:
    if db_tail is None:
        log("list is Empty")
    else:
        log("link elements in reverse are")
        print("DLNodes [rev]: ", db_tail.data, end="")
        temp = db_tail.prev
        while temp:
            print(" <->", temp.data, end="")
            temp = temp.prev
        print(" <-> None")

def menu(db_list: DoublyLinkedList, choice: int):

    if choice == 1:
        db_list.head = pushBeginning(db_list)
    elif choice == 2:
        db_list.head = popAtBeginning(db_list)
    elif choice == 3:
        seeList(db_list.head)
    elif choice == 4:
        seeListReverse(db_list.tail)
    elif choice == 11:
        log("Thank You")
    else:
        log("Please choose only digits from 1-10")


def main() -> None:
    choice = 0
    db_list = DoublyLinkedList()
    while choice != 11:
        log("choose from below:"
            "\n1. Push at beginning"
            "\n2. Pop from beginning"
            "\n3. Display all"
            "\n4. Display all in reverse")
        choice = intInput("your choice: ", "Please choose only digits from 1-10")
        menu(db_list, choice)


if __name__ == "__main__":
    main()
