from unittest import TestCase, main
from ispair import isPair


class Tests(TestCase):
    def testIsPair(self):
        self.assertEqual(isPair(2), True)

    def testIsOdd(self):
        self.assertEqual(isPair(3), False)

    def testString(self):
        self.assertEqual(isPair('test'), False)

    def testFloat(self):
        self.assertEqual(isPair(3.0), False)


if __name__ == '__main__':
    main()
