import unittest
from LRUCache import LRUCache

class LRUCacheTest(unittest.TestCase):
    def setUp(self) -> None:
        self.lRUCache = LRUCache(2)

    def test_cache1(self):
        self.lRUCache.put(1, 1)
        self.lRUCache.put(2, 2)
        self.assertEqual(1, self.lRUCache.get(1))
        self.lRUCache.put(3, 3)
        self.assertEqual(-1, self.lRUCache.get(2))
        self.lRUCache.put(3, 3)
        self.lRUCache.put(4, 4)
        self.assertEqual(-1, self.lRUCache.get(1))
        self.assertEqual(3, self.lRUCache.get(3))
        self.assertEqual(4, self.lRUCache.get(4))


    def test_cache2(self):
        # [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
        self.lRUCache.put(2, 1)
        self.lRUCache.put(2, 2)
        self.assertEqual(2, self.lRUCache.get(2))
        self.lRUCache.put(1, 1)
        self.lRUCache.put(4, 1)
        self.assertEqual(-1, self.lRUCache.get(2))