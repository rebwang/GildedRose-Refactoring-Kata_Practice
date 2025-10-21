# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
    
    def test_normal_item(self):
        items = [Item("Normal", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_normal_item(gilded_rose.items[0])
        self.assertEqual(19, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()
