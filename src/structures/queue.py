# -*- coding: utf-8 -*-

class Queue:
    '''
    Basic FIFO queue: enqueue, dequeue, isempty.
    Implemented with list + head index.
    '''

    def __init__(self):
        self._data = []
        self._head = 0

    def enqueue(self, e):
        self._data.append(e)

    def dequeue(self):
        if self.isempty():
            raise IndexError("dequeue from empty queue")
        e = self._data[self._head]
        self._head += 1

        if self._head > 32 and self._head * 2 > len(self._data):
            self._data = self._data[self._head:]
            self._head = 0
        return e

    def isempty(self):
        return self._head >= len(self._data)
