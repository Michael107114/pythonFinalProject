import unittest

from CoinCollector import CoinCollector


class CoinCollectorTest(unittest.TestCase):

    def testEmpty(self):
        cl = CoinCollector()
        self.assertEqual(0, cl.parseChange(''))

    def testSimple(self):
        cl = CoinCollector()
        self.assertEqual(10, cl.parseChange('D'))
        self.assertEqual(1, cl.parseChange('P'))
        self.assertEqual(2, cl.parseChange('pp'))
        self.assertEqual(5, cl.parseChange('n'))

    def testComplex(self):
        cl = CoinCollector()
        self.assertEqual(100, cl.parseChange('D d___DDD *H*'))