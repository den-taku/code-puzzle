import unittest

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
        return self

    def print(self):
        print(''.join(self.array))

    def decode_morse(self) -> str:
        ans = ""
        index = 0
        while index + 3 < len(self.array):
            word = self.array[index: index + 4]
            ans += self.decode_word(word)
            index += 4
            print(word)
        return ans

    def decode_word(self, word: list[str]) -> str:
        # I -> long
        # i -> short
        if word == ['i', 'I', ' ', ' ']:
            return 'A'
        elif word == ['I', 'i', 'i', 'i']:
            return 'B'
        elif word == ['I', 'i', 'I', 'i']:
            return 'C'
        elif word == ['I', 'i', 'i', ' ']:
            return 'D'
        elif word == ['i', ' ', ' ', ' ']:
            return 'E'
        elif word == ['i', 'i', 'I', 'i']:
            return 'F'
        elif word == ['I', 'I', 'i', ' ']:
            return 'G'
        elif word == ['i', 'i', 'i', 'i']:
            return 'H'
        elif word == ['i', 'i', ' ', ' ']:
            return 'I'
        elif word == ['i', 'I', 'I', 'I']:
            return 'J'
        elif word == ['I', 'i', 'I', ' ']:
            return 'K'
        elif word == ['i', 'I', 'i', 'i']:
            return 'L'
        elif word == ['I', 'I', ' ', ' ']:
            return 'M'
        elif word == ['I', 'i', ' ', ' ']:
            return 'N'
        elif word == ['I', 'I', 'I', ' ']:
            return 'O'
        elif word == ['i', 'I', 'I', 'i']:
            return 'P'
        elif word == ['I', 'I', 'i', 'I']:
            return 'Q'
        elif word == ['i', 'I', 'i', ' ']:
            return 'R'
        elif word == ['i', 'i', 'i', ' ']:
            return 'S'
        elif word == ['I', ' ', ' ', ' ']:
            return 'T'
        elif word == ['i', 'i', 'I', ' ']:
            return 'U'
        elif word == ['i', 'i', 'i', 'I']:
            return 'V'
        elif word == ['i', 'I', 'I', ' ']:
            return 'W'
        elif word == ['I', 'i', 'i', 'I']:
            return 'X'
        elif word == ['I', 'i', 'I', 'I']:
            return 'Y'
        elif word == ['I', 'I', 'i', 'i']:
            return 'Z'
        else:
            return '?'

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
            elif list[1] == 'i':
                if list[2] == ' ' or list[2] == 'T':
                    return 'T'
                else:
                    return 'I'
            elif list[1] == 'T':
                if list[2] == ' ' or list[2] == 'T':
                    return 'i'
                else:
                    return ' '
            else:
                if list[2] == ' ' or list[2] == 'T':
                    return 'I'
                else:
                    return "T"
        elif list[0] == 'i':
            if list[1] == ' ':
                if list[2] == ' ' or list[2] == 'T':
                    return 'i'
                else:
                    return ' '
            elif list[1] == 'i':
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
                if list[2] == ' ' or list[2] == 'T':
                    return 'T'
                else:
                    return 'I'
        elif list[0] == 'T':
            if list[1] == ' ':
                if list[2] == ' ' or list[2] == 'T':
                    return ' '
                else:
                    return 'i'
            elif list[1] == 'i':
                if list[2] == ' ' or list[2] == 'T':
                    return 'T'
                else:
                    return 'I'
            elif list[1] == 'T':
                if list[2] == ' ' or list[2] == 'T':
                    return 'i'
                else:
                    return ' '
            else:
                if list[2] == ' ' or list[2] == 'T':
                    return 'I'
                else:
                    return 'T'
        else:
            if list[1] == ' ':
                if list[2] == ' ' or list[2] == 'T':
                    return 'i'
                else:
                    return ' '
            elif list[1] == 'i':
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
                if list[2] == ' ' or list[2] == 'T':
                    return 'T'
                else:
                    return 'I'


class testBars(unittest.TestCase):
    def setUp(self):
        pass

    def test_simple_rule(self):
        self.assertEqual(Bars("     ").next().str(), "     ")
        self.assertEqual(Bars("  i  ").next().str(), " iTi ")
        self.assertEqual(Bars(" i i ").next().str(), "iT Ti")
        self.assertEqual(Bars("  T  ").next().str(), "  i  ")
        self.assertEqual(Bars(" TiT ").next().str(), "  T  ")
        self.assertEqual(Bars(" iTi ").next().str(), "iTiTi")
        self.assertEqual(Bars(" TTT ").next().str(), " iii ")

    def test_rule(self):
        self.assertEqual(Bars(" I  ").next().str(), "iIi ")
        self.assertEqual(Bars(" ii ").next().str(), "iIIi")
        self.assertEqual(Bars(" Ii ").next().str(), "iTIi")
        self.assertEqual(Bars(" TI ").next().str(), "  Ii")
        self.assertEqual(Bars(" II ").next().str(), "iTTi")

    def test_loop(self):
        bs = Bars("Ti  ")
        self.assertEqual(bs.next().str(), " Ti ")
        self.assertEqual(bs.next().str(), "  Ti")
        self.assertEqual(bs.next().str(), "i  T")
        self.assertEqual(bs.next().str(), "Ti  ")
        bs = Bars("  iT")
        self.assertEqual(bs.next().str(), " iT ")
        self.assertEqual(bs.next().str(), "iT  ")
        self.assertEqual(bs.next().str(), "T  i")
        self.assertEqual(bs.next().str(), "  iT")

    def test_next(self):
        bs = Bars("I    IT ii  i I   I i   i   I  T")
        bs.next()
        self.assertEqual(bs.str(), "Ii  iI iIIiiT Ii iI Ti iTi iIi  ")
        bs.next()
        self.assertEqual(bs.str(), "TIiiIT IIITI iTI ITi T TiT IIIii")

    def tearDown(self):
        pass


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(testBars))
    unittest.TextTestRunner(verbosity=2).run(suite)

    bs = Bars("I    IT ii  i I   I i   i   I  T")
    for i in range(26):
        bs.print()
        bs.next()
    bs.print()

    print("answer: " + bs.decode_morse())
