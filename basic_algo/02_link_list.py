# link list implementation
def log(msg: str) -> None:
    print("-" * 30)
    print(f"{msg:^30}")


def intInput(opt: str = "", msg: str = "") -> int:
    val = None
    while val is None:
        try:
            val = int(input(opt))
        except ValueError:
            log("Only digits allowed" + msg)
    return val


class Node:
    def __init__(self, data):
        self.data: int = data
        self.next: [Node, None] = None


class LinkedList:
    def __init__(self):
        self.head = None


def pushAtEnd(head: [Node, None]) -> Node:
    dat = intInput("Enter your data: ")
    new_data = Node(dat)
    if head is None:
        head = new_data
    else:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_data
    log(f"data {dat} added to linked list")
    return head


def popFromEnd(head: [Node, None]) -> Node:
    temp = head
    temp1 = temp
    if temp is None:
        log("link list is empty")
    elif temp.next is None:
        log(f"last element {temp.data} removed from linked list ")
        head = None
    else:
        while temp.next is not None:
            temp1 = temp
            temp = temp.next
        log(f"{temp.data} removed from linked list ")
        temp1.next = None
        del temp
    return head


def seeList(head: [Node, None]) -> None:
    temp = head
    if temp is None:
        log("link list is empty")
    else:
        log("link list is:")
        while temp.next is not None:
            print(f" -> {temp.data}", end="")
            temp = temp.next
        print(f" -> {temp.data}")


def addAtBeginning(head: [Node, None]) -> Node:
    dat = intInput("Enter your data: ")
    new_data = Node(dat)
    if head is None:
        head = new_data
    else:
        new_data.next = head
        head = new_data
    log(f"data {dat} added to beginning of linked list")
    return head


def popFromBeginning(head: [Node, None]) -> Node:
    temp = head
    if temp is None:
        log("link list is empty")
    elif temp.next is None:
        log(f"last element {temp.data} removed from linked list ")
        head = None
    else:
        head = head.next
        log(f"data {temp.data} removed from beginning of linked list")
        del temp
    return head


def addAtNthPlace(head: [None, Node], place: int) -> Node:
    list_size = listSize(head)
    if place < 0 or place > list_size+1:
        log(f"Enter range in current list size [0 - {list_size+1}]")
    elif place == 0 or place == 1:
        head = addAtBeginning(head)
    elif place == list_size + 1:
        head = pushAtEnd(head)
    else:
        dat = intInput("Enter your data: ")
        new_data = Node(dat)
        plc = 1
        temp = head
        temp1 = temp
        while plc != place:
            temp1 = temp
            temp = temp.next
            plc += 1
        temp1.next = new_data
        new_data.next = temp
        log(f"data {temp.data} added at {place}th place of linked list")
    return head


def removeFromNthPlace(head: [None, Node], place: int) -> Node:
    list_size = listSize(head)
    if place < 0 or place > list_size + 1:
        log(f"Enter range in current list size [0 - {list_size }]")
    elif place == 0 or place == 1:
        head = popFromBeginning(head)
    elif place == list_size + 1:
        head = popFromEnd(head)
    else:
        temp = head
        temp1 = temp
        plc = 1
        while plc != place:
            temp1 = temp
            temp = temp.next
            plc += 1
        temp1.next = temp.next
        log(f"data {temp.data} added at {place}th place of linked list")
        del temp

    return head


def listSize(head: [Node, None]) -> int:
    if head is None:
        return 0
    elif head.next is None:
        return 1
    else:
        temp = head
        count = 1
        while temp.next is not None:
            count += 1
            temp = temp.next
    return count


def menu(link_list: LinkedList, choice: int):
    list_head = link_list.head
    if choice == 1:
        link_list.head = pushAtEnd(list_head)
    elif choice == 2:
        link_list.head = popFromEnd(list_head)
    elif choice == 3:
        seeList(list_head)
    elif choice == 4:
        link_list.head = addAtBeginning(list_head)
    elif choice == 5:
        link_list.head = popFromBeginning(list_head)
    elif choice == 6:
        place = intInput("Enter the place: ")
        link_list.head = addAtNthPlace(list_head, place)
    elif choice == 7:
        place = intInput("Enter the place: ")
        link_list.head = removeFromNthPlace(list_head, place)
    elif choice == 8:
        log(f"current list length is {listSize(list_head)}")
    elif choice == 9:
        log("Thank you")
    else:
        log("\nChoose digits from 1-9 only\n")


def main():
    link_list = LinkedList()
    choice = None
    options = ("\nChoose your option: "
               "\n\t1. Add last element to link list."
               "\n\t2. Remove last element from link list."
               "\n\t3. See full link list"
               "\n\t4. Add element to beginning of link list."
               "\n\t5. Remove element from beginning of link list."
               "\n\t6. Add element to nth place."
               "\n\t7. Remove element from nth place."
               "\n\t8. Size of list"
               "\n\t9. Quit.")
    while choice != 9:
        log(options)
        choice = intInput("Enter your choice: ", "\nChoose digits from 1-9 only\n" + options)
        menu(link_list, choice)


if __name__ == "__main__":
    main()
