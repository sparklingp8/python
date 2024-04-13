# full stack code with functions implementation using array
import array as arr

MAXSIZE: int = 3


def log(msg: str) -> None:
    print("-" * 30)
    print(f"{msg:^30}")


def isStackFull(stckTp: int) -> bool:
    if stckTp == MAXSIZE-1:
        return True
    else:
        return False


def isStackEmpty(stckTp: int) -> bool:
    if stckTp == -1:
        return True
    else:
        return False


def currentSize(stck: arr.array) -> int:
    return len(stck)


def pop(stck: arr.array, stckTp: int) -> int:
    if isStackEmpty(stckTp):
        log("stack is empty, Nothing to show")
        return stckTp
    else:
        log(f"{stck[stckTp]} has been popped from stack")
        stck.pop()
        return stckTp - 1


def push(stck: arr.array, stckTp: int) -> int:
    if isStackFull(stckTp):
        log("stack is full, Sorry")
        return stckTp
    else:
        val = None
        while val is None:
            try:
                val = int(input("Enter value: "))
                stck.append(val)
                log(f"{val} added to stack")
                return stckTp + 1
            except ValueError:
                log("only integers  are allowed")


def peek(stck: arr.array, stckTp: int) -> None:
    if isStackEmpty(stckTp):
        return log("Stack is Empty, nothing to show")
    else:
        log(f"Top Elements is: {stck[stckTp]}")


def seeFullStack(stck: arr.array, stckTp: int) -> None:
    if isStackEmpty(stckTp):
        return log("Stack is Empty, nothing to show")
    print("Stack Elements are: ")
    i = stckTp
    while i >= 0:
        print(stck[i])
        i -= 1


def main(choice: int, stck: arr.array, stck_tp: int) -> int:
    if choice == 1:
        stck_tp = push(stck, stck_tp)
    if choice == 2:
        stck_tp = pop(stck, stck_tp)
    if choice == 3:
        peek(stck, stck_tp)
    if choice == 4:
        log(f"stack is full") if isStackFull(stck_tp) else log("stack is not full")
    if choice == 5:
        log(f"stack is empty") if isStackEmpty(stck_tp) else log("stack is not Empty")
    if choice == 6:
        log(f"stack size is: {stck_tp+1}/{MAXSIZE}")
    elif choice == 7:
        seeFullStack(stck, stck_tp)
    elif choice == 8:
        log("Thank you")
    return stck_tp


def menu() -> None:
    stack = arr.array('i')
    stack_top: int = -1
    choice = 0
    while choice != 8:
        log("Choose from below: "
            "\n1. push element to stack\n2. pop element from stack"
            "\n3. peek at stack\n4. is stack full\n5. is stack empty"
            "\n6. stack size\n7. see full stack\n8. Quit"
            )
        try:
            choice = int(input("Enter option: "))
            if choice not in range(1, 9):
                raise ValueError
            else:
                stack_top = main(choice, stack, stack_top)
        except ValueError:
            log("only digits 1-8 are allowed")


if __name__ == "__main__":
    menu()
