#!/usr/bin/env python3
import sys


class Node:
    def __init__(self, frequency, character=None):
        self.frequency = frequency
        self.character = character
        self.left = None
        self.right = None
        self.bin = ''


class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.length = 0

    def size(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def put(self, node):
        # adding an element to the queue
        self.queue.append(node)
        self.length += 1

    def pop_least_frequent(self):
        # deleting  least frequent node
        least_frequent_node = self.queue[0]

        index = 0

        for i in range(self.length):
            if self.queue[i].frequency < least_frequent_node.frequency:
                least_frequent_node = self.queue[i]
                index = i

        del self.queue[index]
        self.length -= 1
        return least_frequent_node


def huffman_encoding(data):
    if data is None or data == '':
        print('Cannot encode empty data.')
        return '', None
    # First, determine the frequency of each character in the message.
    frequencies = get_char_frequencies(data)

    # Second: Build the Huffman Tree.
    tree = build_tree(frequencies)

    # Third: Map the codes from the Huffman Tree.
    # only if the frequencies length is distinct than 1
    binary_codes = dict()
    if len(frequencies) == 1:
        binary_codes[tree.character] = '0'
    else:
        binary_codes = create_binary_codes(tree, '', dict())

    # Fourth, encoding the letters having the binary codes
    encoded_value = ''
    for char in data:
        encoded_value += binary_codes[char]

    return encoded_value, tree


def get_char_frequencies(data):
    frequencies = dict()
    for character in data:
        frequencies[character] = frequencies.get(character, 0) + 1
    return frequencies


def build_tree(frequencies):
    # check if there are no frequencies
    if len(frequencies) == 0:
        return
    if len(frequencies) == 1:
        queue = []
        for character in frequencies:
            queue.append(Node(frequencies[character], character))

        return queue[0]

    # build priority queue
    queue = PriorityQueue()
    for character in frequencies:
        queue.put(Node(frequencies[character], character))

    while queue.size() > 1:
        # getting first and second least frequent nodes
        first = queue.pop_least_frequent()
        second = queue.pop_least_frequent()

        # creating a parent node based on the first and second nodes
        parent = Node(first.frequency + second.frequency)
        parent.left = first
        parent.right = second

        # adding the parent node to the priority queue
        queue.put(parent)
    # returning the built tree
    return queue.pop_least_frequent()


def create_binary_codes(node, code, binary_codes):
    # traversing the tree

    # if node.left is None and node.right is None:
    #     binary_codes[node.character] = '0'
    #     return binary_codes

    if node.left is not None:
        create_binary_codes(node.left, code + '0', binary_codes)
    else:
        binary_codes[node.character] = code

    if node.right is not None:
        create_binary_codes(node.right, code + '1', binary_codes)
    else:
        binary_codes[node.character] = code

    return binary_codes


def huffman_decoding(data, tree):
    if data is None or data == '' or tree is None:
        print('Cannot decode empty data.')
        return None
    decoded_value = ''
    # saving the parent node reference
    node = tree
    for bit in data:
        # Walk to the left child.
        if int(bit) == 1:
            if node.right is not None:
                node = node.right
        else:
            if node.left is not None:
                node = node.left

        if node.left is None and node.right is None:
            decoded_value += node.character
            # restarting reference to the start of the tree
            node = tree
    return decoded_value


def trimString(data):
    return data.strip()


if __name__ == '__main__':
    def run_test_1():
        a_great_sentence = "    The bird is the word   "
        a_great_sentence = trimString(a_great_sentence)
        print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print("The content of the data is: {}\n".format(a_great_sentence))

        encoded_data, tree = huffman_encoding(a_great_sentence)

        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print("The content of the encoded data is: {}\n".format(decoded_data))


    def run_test_2():
        a_great_sentence = ""
        encoded_data, tree = huffman_encoding(a_great_sentence)  # returns message 'Cannot encode empty data.'
        decoded_data = huffman_decoding(encoded_data, tree)  # returns message: 'Cannot decode empty data.'


    def run_test_3():
        values = {
            "AAAAAAAAAA",
            "AAAAABBBBB",
            "anitalavalatina",
            "101010",
        }
        for value in values:
            print("The size of the data is: {}\n".format(sys.getsizeof(value)))
            print("The content of the data is: {}\n".format(value))

            encoded_data, tree = huffman_encoding(value)

            print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
            print("The content of the encoded data is: {}\n".format(encoded_data))

            decoded_data = huffman_decoding(encoded_data, tree)

            print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
            print("The content of the encoded data is: {}\n".format(decoded_data))

run_test_1()
run_test_2()
run_test_3()
