#!/usr/bin/python3
""" Define a class node """


class Node:
    """ class node which defines a node of a singly linked list
    Attributes:
    data: its a private instance attribute
    """
    def __init__(self, data, next_node=None):
        """Creates new instances of node.

        Args:
            __data : data field of node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ it's used to retrieve data as a
        private instance attribute
        Return: data field of a node
        """
        return self._data

    @data.setter
    def data(self, value):
        """Propery setter for data.

        Args:
            value (int): data field of a node.

        Raises:
            TypeError: data must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Retrives the next_node instance.

        Returns: The next_node instance.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """Property setter for Node.

        Args:
            value (None): next node of a Node.

        Raises:
            TypeError: next_node must be a Node object .
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """
    Class that defines properties of SinglyLinkedList.

    Attributes:
        head: head of the SinglyLinkedList.
    """
    def __init__(self):
        """Creates new instances of SinglyLinkedList .

        Args:
            __head : head of the SinglyLinkedList .
        """

        self.head = None

    def sorted_insert(self, value):
        """Inserts a new node at a given position.

        Args:
            value: value.
        """
        new_node = Node(value)

        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Represents the class objects as a string.

        Returns: The class object represented as a string.
        """
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
