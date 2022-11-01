from hashlib import new
import re

class SimpleBars:
    def __init__(self, num: int):
        self.array = []
        for _ in range(0, num):
            self.array.append(' ')

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
            else: # self.array[i] == 'T'
                new_array[i] = 'i'
        self.array = new_array

    def print(self):
        print(''.join(self.array))

test = SimpleBars(24)
test.pos_mut(8, 'T')
for _ in range(30):
    test.next()
    test.print()

bs = SimpleBars(78)

commands = "1(///(1iTiTiTi|||[(1 ])1( [L|[L|[L|[(] |1//)/)1i||1)///)1i||||1(///)1i\
(/////)1iTiTi[L!])|])[L!])])l|])1/( [(1/ ]L!l|[(1 ])1( //(1 ]L[L!|"
pos = 0; acc = 1; accx = 1; output = ""

for c in commands:
    if   c == "1": acc = 1
    elif c == "/": acc = acc * 2
    elif c == ")": pos += acc; pos %= bs.len()
    elif c == "(": pos -= acc; pos %= bs.len()
    elif c == "i" or c == "T" or c == " ":
        for i in range(acc): bs.pos_mut(pos, c); pos += 1; pos %= bs.len()
    elif c == "]":
        s = bs.str()[pos:]+bs.str()[:pos+1];         m = re.search("^ *[iT]* ", s)
        acc = (m and m.end() - 1) or 0
    elif c == "[":
        t = bs.str(); s = t[pos-1]+t[pos:]+t[:pos]; m = re.search(" [iT]* *$", s)
        acc = (m and len(s) - m.start() - 1) or 0
    elif c == "l": acc, accx = accx, acc
    elif c == "L": acc, accx = accx - acc, accx + acc
    elif c == "|": bs.print(); bs.next()
    elif c == "!": output += chr((ord('0') + acc) % 128)

print("answer: " + output)