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
        for i in range(0, l):
            new_array[i] = self.decide_char(i, l)
        self.array = new_array

    def print(self):
        print(''.join(self.array))

    def decide_char(self, index: int, length: int) -> str:
        if index == length - 1:
            list = [self.array[index - 1], self.array[index], self.array[0]]
        elif index == 0:
            list = [self.array[length - 1], self.array[0], self.array[1]]
        else:
            list = self.array[index-1:index+2]

        if list[0] == ' ':
            if list[1] == ' ':
                if list[2] == ' ' or list[2] == 'T':
                    return ' '
                else:
                    return 'i'
            elif list[1] == 'i' or list[1] == 'I':
                if list[2] == ' ' or list[2] == 'T':
                    return 'T'
                else:
                    return 'I'
            elif list[1] == 'T':
                if list[2] == ' ' or list[2] == 'T':
                    return 'i'
                else:
                    return ' '
        elif list[0] == 'i':
            if list[1] == ' ':
                if list[2] == ' ' or list[2] == 'T':
                    return 'i'
                else:
                    return ' '
            elif list[1] == 'i' or list[1] == 'I':
                if list[2] == ' ' or list[2] == 'T':
                    return 'I'
                else:
                    return 'T'
            elif list[1] == 'T':
                if list[2] == ' ' or list[2] == 'T':
                    return ' '
                else:
                    return 'i'
        else:
            return ' '


if __name__ == "__main__":
    bs = Bars("I    IT ii  i I   I i   i   I  T")
    for i in range(26):
        bs.print()
        bs.next()
    bs.print()
