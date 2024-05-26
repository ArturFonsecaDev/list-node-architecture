from node import Node

class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self._size = 0

    def __len__(self) -> int:
        """This returns the size of the linked list"""
        return self._size
    
    def __getitem__(self, index):
        """This allow the print(list[index]) syntax available"""

        if index < 0 or index >= self._size:
            raise IndexError('Index out of range!')

        pointer = self.head
        for i in range(index):
            if pointer.next is not None:
                pointer = pointer.next
        if pointer:
            return pointer
    
    def __setitem__(self, index, new_value):
        """This allow to set a new value to an already indexed value on a list"""

        if index < 0 or index > self._size:
            raise IndexError('Index out of range!')

        pointer = self.head
        for i in range(index):
            if pointer.next is not None:
                pointer = pointer.next
        if pointer:
            pointer.data = new_value
    
    def __str__(self) -> str:
        """This allows you to print the whole list with a [element[0], element[1], ... element[n]] pattern"""
        formato = '[{}]'
        lista_str = ''
        pointer = self.head
        for i in range(self._size):
            if pointer:
                lista_str += str(pointer)
                lista_str += ' -> '
                pointer = pointer.next
        lista_str = lista_str.rstrip(' -> ')
        return formato.format(lista_str)
    
    def append(self, new_element):
        """This appends a new element to the linked list"""
        # inserção do primeiro elemento
        if self.head is None:
            self.head = Node(new_element)
            self._size += 1
            return
        # inserção a partir do segundo elemento
        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next
        if pointer:
            pointer.next = Node(new_element)
        self._size += 1

if __name__ == '__main__':
    lista = LinkedList()
    lista.append(1)
    lista.append(22)
    lista[0] = 15
    print(lista)


