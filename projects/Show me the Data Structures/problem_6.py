class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    union = set()
    # getting data from list 1
    head = llist_1.head
    if head is not None:
        while head.next:
            union.add(head.value)
            head = head.next
        union.add(head.value)
    # getting data from list 2
    head = llist_2.head
    if head is not None:
        while head.next:
            union.add(head.value)
            head = head.next
        union.add(head.value)
    # converting set to LinkedList
    result = LinkedList()
    for element in union:
        result.append(element)

    return result


def intersection(llist_1, llist_2):
    data_1 = set()
    # getting data from list 1
    head = llist_1.head
    if head is not None:
        while head.next:
            data_1.add(head.value)
            head = head.next
        data_1.add(head.value)

    data_2 = set()
    # getting data from list 2
    head = llist_2.head
    if head is not None:
        while head.next:
            data_2.add(head.value)
            head = head.next
        data_2.add(head.value)

    data = data_1.intersection(data_2)
    # converting set to LinkedList
    result = LinkedList()
    for element in data:
        result.append(element)

    return result


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))  # returns the union of LinkedList 1 and 2
print(intersection(linked_list_1, linked_list_2))  # returns the intersection of LinkedList 1 and 2

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))  # returns the union of LinkedList 1 and 2
print(intersection(linked_list_3, linked_list_4))  # returns nothing because there is no intersection between LinkedList 1 and 2

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [66]
for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)


print(union(linked_list_5, linked_list_6))  # returns the union of LinkedList 1 and 2
print(intersection(linked_list_5, linked_list_6))  # returns nothing because there is no intersection between LinkedList 1 and 2
