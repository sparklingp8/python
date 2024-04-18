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
    while val is None:
        try:
            val = int(input(prmpt))
        except ValueError:
            log(errmsg)
    return val


def pushAtBeginning(db_list: DoublyLinkedList):
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


def pushATEnd(db_list: DoublyLinkedList):
    dat = intInput("Enter you data: ", "Only int data allowed")
    new_node = Node(dat)
    if db_list.head is None:
        db_list.head = new_node
        db_list.tail = new_node
    else:
        db_list.tail.next = new_node
        new_node.prev = db_list.tail
        db_list.tail = new_node
    log(f"{dat} has been added to the list")
    return db_list.head


def popAtEnd(db_list: DoublyLinkedList):
    if db_list.head is None:
        log("list is empty")
    elif db_list.head.next is None:
        log(f"Removed last element {db_list.head.data} from the list")
        db_list.head = None
        db_list.tail = None
    else:
        db_list.tail.prev.next = None
        log(f"Removed {db_list.tail.data} from the end of the list")
        db_list.tail = db_list.tail.prev
    return db_list.head


def lenOfList(db_list: DoublyLinkedList) -> int:
    if db_list.head is None:
        return 0
    elif db_list.head.next is None:
        return 1
    else:
        temp = db_list.head.next
        cnt = 1
        while temp is not None:
            cnt += 1
            temp = temp.next
        return cnt


def pushAtNthPlace(db_list: DoublyLinkedList):
    plc = -1
    len_of_list = lenOfList(db_list)
    while plc < 0 or plc > len_of_list + 1:
        plc = intInput("Enter position: ", f"Enter Place between 0 - {len_of_list + 1}")
        if plc > len_of_list + 1:
            log(f"Enter Place between 0 - {len_of_list + 1}")
    if plc == 0 or plc == 1:
        db_list.head = pushAtBeginning(db_list)
    elif plc == len_of_list + 1:
        db_list.head = pushATEnd(db_list)
    else:
        temp = db_list.head
        t_plc = 2
        while t_plc < plc:
            temp = temp.next
            t_plc += 1
        dat = intInput("Enter you data: ", "Only int data allowed")
        new_node = Node(dat)

        new_node.prev = temp
        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node
        log(f"{dat} added at {plc}th place")
    return db_list.head


def popAtNthPlace(db_list):
    plc = -1
    len_of_list = lenOfList(db_list)
    while plc < 0 or plc > len_of_list + 1:
        plc = intInput("Enter position: ", f"Enter Place between 0 - {len_of_list + 1}")
        if plc > len_of_list + 1:
            log(f"Enter Place between 0 - {len_of_list + 1}")
    if plc == 0 or plc == 1:
        db_list.head = popAtBeginning(db_list)
    elif plc == len_of_list + 1 or plc == len_of_list:
        db_list.head = popAtEnd(db_list)
    else:
        temp = db_list.head
        t_plc = 2
        while t_plc <= plc:
            temp = temp.next
            t_plc += 1

        log(f"{temp.data} removed from {plc}th place")
        temp.next.prev = temp.prev
        temp.prev.next = temp.next

    return db_list.head

def menu(db_list: DoublyLinkedList, choice: int):
    if choice == 1:
        db_list.head = pushAtBeginning(db_list)
    elif choice == 2:
        db_list.head = popAtBeginning(db_list)
    elif choice == 3:
        seeList(db_list.head)
    elif choice == 4:
        seeListReverse(db_list.tail)
    elif choice == 5:
        db_list.head = pushATEnd(db_list)
    elif choice == 6:
        db_list.head = popAtEnd(db_list)
    elif choice == 7:
        db_list.head = pushAtNthPlace(db_list)
    elif choice == 8:
        db_list.head = popAtNthPlace(db_list)
    elif choice == 9:
        log(f"Length of list is: {lenOfList(db_list)}")
    elif choice == 10:
        log("Thank You")
    else:
        log("Please choose only digits from 1-10")


def main() -> None:
    choice = 0
    db_list = DoublyLinkedList()
    while choice != 10:
        log("choose from below:"
            "\n1. Push at beginning"
            "\n2. Pop from beginning"
            "\n3. Display all"
            "\n4. Display all in reverse"
            "\n5. Push at end"
            "\n6. Pop at end"
            "\n7. Push at Nth place"
            "\n8. Pop at Nth place"
            "\n9. See length of the list"
            "\n10. Quit"
            )
        choice = intInput("your choice: ", "Please choose only digits from 1-10")
        menu(db_list, choice)


if __name__ == "__main__":
    main()
