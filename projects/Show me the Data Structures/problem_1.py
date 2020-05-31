class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRU_Cache(object):

    def __init__(self, capacity):
        if capacity < 1:
            print('LRUCache should have capacity > 0')
            return
        # Initialize class variables
        self.capacity = capacity
        self.size = 0
        self.map = dict()
        self.head = None  # this node represents the least recently used
        self.tail = None  # this node represents the most recently used

    def get_capacity(self):
        return self.capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key is None:
            return -1
        elif key not in self.map:
            return -1
        else:
            node = self.map[key]
            self.move_to_front(node)
            return node.value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        """
        First. we validate the input key
        Second. we verify if key is already in the map
                If key in map:
                    We update the node value and move it to the front
                If not in map:
                    We create a new node and set it in the map
        Third: we validate if we passed the cache capacity
        """
        if key is None or value is None:
            return -1

        elif key not in self.map:
            node = Node(key, value)
            self.map[key] = node
            self.add(node)

        else:
            node = self.map[key]
            node.value = value
            self.move_to_front(node)

        if self.capacity < 0:
            self.remove_lru()

    def move_to_front(self, node):
        self.remove(node)
        self.add(node)

    def add(self, node):
        # add data to the next attribute of the tail (i.e. the end of the queue)
        # if head and tail have no values
        if self.head is None or self.tail is None:
            self.head = node
            self.tail = node
        # if the linked list has values already
        else:
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node

        self.capacity = self.capacity - 1

    def remove(self, node):
        # if the node we want to delete is the head
        if self.head.key == node.key:
            next_node = self.head.next
            self.head = next_node
        # if the node we want to delete is the tail
        elif self.tail.key == node.key:
            prev_node = self.tail.prev
            self.tail = prev_node
        # if none of the above happens
        else:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node

        self.capacity += 1

    def remove_lru(self):
        node = self.tail
        self.remove(node)
        del self.map[node.key]


if __name__ == '__main__':
    def test_case_1():  # invalid length cache test case
        our_cache = LRU_Cache(-1)
        # should show an invalid capacity value


    def test_case_2():  # normal length cache test case
        our_cache = LRU_Cache(5)
        our_cache.set(1, 11)
        our_cache.set(2, 22)
        our_cache.set(3, 33)
        our_cache.set(4, 44)
        our_cache.set(5, 55)
        our_cache.set(6, 66)
        our_cache.set(7, 77)

        print(our_cache.get(1))  # returns -1
        print(our_cache.get(2))  # returns -1
        print(our_cache.get(3))  # returns 33
        print(our_cache.get(7))  # returns 77
        print(our_cache.get(6))  # returns 66
        print(our_cache.get(4))  # returns 44
        our_cache.set(8, 88)
        print(our_cache.get(5))  # returns -1


    def test_case_3():  # short cache test case
        our_cache = LRU_Cache(1)
        our_cache.set(1, 11)
        our_cache.set(2, 22)
        print(our_cache.get(1))  # returns -1
        our_cache.set(-3, 100)
        print(our_cache.get(2))  # returns -1
        print(our_cache.get(-3))  # returns 100

test_case_1()
test_case_2()
test_case_3()
