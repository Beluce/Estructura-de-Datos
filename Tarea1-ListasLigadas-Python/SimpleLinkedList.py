from Node import Node

class SimpleLinkedList:
    def __init__(self, values=None):
        self.header = Node()
        if values is not None:
            temp = self.header
            for i in range(len(values)):
                temp.value = values[i]
                if i < len(values) - 1:
                    temp.reference = Node()
                    temp = temp.reference

    def add(self, index, value):
        temp = self.header
        for i in range(index):
            if i == index - 1 or temp.reference is None:
                if temp.reference is None:
                    temp.reference = Node(value)
                else:
                    temp.reference = Node(value, reference=temp.reference)
            else:
                temp = temp.reference

    def print_data(self):
        self.__print_data_helper(self.header)

    def __print_data_helper(self, node):
        if node is not None:
            print(node.value, end=' ')
            self.__print_data_helper(node.reference)
        else:
            print()