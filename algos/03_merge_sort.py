def split_it(data_list):
    if len(data_list) > 1:
        mid = len(data_list) // 2
        left_split = data_list[: mid]
        right_split = data_list[mid:]
        split_it(left_split)
        split_it(right_split)
        merge_sorted(left_split, right_split, data_list)


def merge_sorted(left_split, right_split, data_list):
    la = len(left_split)
    lb = len(right_split)
    i = j = k = 0

    while i < la and j < lb:
        if left_split[i] < right_split[j]:
            data_list[k] = left_split[i]
            i += 1
        else:
            data_list[k] = right_split[j]
            j += 1
        k += 1
    if i < la:
        data_list[k:] = left_split[i:]
    if j < lb:
        data_list[k:] = right_split[j:]

def main():
    li = [22, -1, 0, 3999999, 12, 4545, 2578, 5, 6, 4]
    split_it(li)
    print(li)


main()
