import hashlib
import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
        self.next = None

    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __str__(self):
        # print values
        result = "Data: " + self.data + "\n"
        result += "Timestamp: " + self.timestamp + "\n"
        result += "SHA256 Hash: " + str(self.hash) + "\n"
        result += "Prev_Hash: " + str(self.previous_hash) + "\n"
        return result


class BlockChain:
    def __init__(self):
        self.head = None

    def append(self, data):
        # check if head is none
        if self.head is None:
            self.head = Block(self.get_date_time(), data, 0)
            return

        block = self.head
        # go to the end of the LinkedList and create a new block
        while block.next:
            block = block.next

        prev_hash = block.hash
        block.next = Block(self.get_date_time(), data, prev_hash)

    def search(self, data):
        # check if head is none
        if self.head is None:
            return None

        # traverse the LinkedList and check if value is equal
        block = self.head
        while block:
            if block.data == data:
                return block
            block = block.next

    def get_date_time(self):
        return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")

    def __repr__(self):
        # check if head is none
        if self.head is None:
            return 'Blockchain is empty.\n'

        # traverse the entire LinkedList and print
        output = ''
        block = self.head
        while block:
            output += str(block) + "\n"
            block = block.next
        return output


if __name__ == '__main__':
    def test_1():  # check if the block chain works
        print('Test 1 is running')
        blockchain = BlockChain()
        blockchain.append("Hello")
        blockchain.append("My")
        blockchain.append("name")
        blockchain.append("is")
        blockchain.append("Geovani")
        print(repr(blockchain))
        # you should see the block chain and the prev has shoud be the same as the last block's hash


    def test_2():  # search a value in the block chain
        print('Test 1 is running')
        blockchain = BlockChain()
        blockchain.append("Hello")
        blockchain.append("My")
        blockchain.append("name")
        blockchain.append("is")
        blockchain.append("Geovani")
        found = blockchain.search("Geovani")
        print(str(found)) # returns the block with data 'Geovani'


    def test_3():  # search a value in the block chain
        print('Test 1 is running')
        blockchain = BlockChain()
        blockchain.append("Hello")
        blockchain.append("My")
        blockchain.append("name")
        blockchain.append("is")
        blockchain.append("Geovani")
        found = blockchain.search("Missael")
        print(str(found))  # returns None because that data does not exist in the block chain
# test_1()
# test_2()
test_3()
