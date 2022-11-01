from hashlib import new
import re


class Bars:
    def __init__(self, string: str):
        self.array = []
        for c in string:
            self.array.append(c)

    def len(self):
        return len(self.array)

    def str(self):
        return ''.join(self.array)

    def pos(self, index: int):
        return self.array[index]

    def pos_mut(self, index: int, c: str):
        self.array[index] = c

    def next(self):
        l = len(self.array)
        new_array = []
        for _ in range(0, l):
            new_array.append(' ')
        # TODO: implement rule of 'I'
        for i in range(0, l):
            if self.array[i - 1] == 'i' and self.array[i] == 'T' and self.array[(i + 1) % l] == 'i':
                new_array[i] = 'i'
            elif self.array[i - 1] == 'i' and self.array[i] == ' ' and self.array[(i + 1) % l] == 'i':
                new_array[i] = ' '
            elif self.array[i - 1] == 'i' and self.array[i] == 'T':
                new_array[i] = ' '
            elif self.array[i] == 'T' and self.array[(i + 1) % l] == 'i':
                new_array[i] = ' '
            elif self.array[i - 1] == 'i' and self.array[i] == ' ':
                new_array[i] = 'i'
            elif self.array[i] == ' ' and self.array[(i + 1) % l] == 'i':
                new_array[i] = 'i'
            elif self.array[i] == ' ':
                new_array[i] = ' '
            elif self.array[i] == 'i':
                new_array[i] = 'T'
            else:  # self.array[i] == 'T'
                new_array[i] = 'i'
        self.array = new_array

    def print(self):
        print(''.join(self.array))


bs = Bars("I    IT ii  i I   I i   i   I  T")
bs.print()
