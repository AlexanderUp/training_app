# encoding:utf-8
# tests for memowords kivy framework application

# python3 -m unittest -v test_class_dictionary.py

print("*" * 75)

import unittest
import os

import class_dictionary


OUTPUT_FILE = 'test_dictionary.shelve_file'

class DictionaryTest(unittest.TestCase):

    def setUp(self):
        self.d = class_dictionary.Dictionary(OUTPUT_FILE)
        print('Current working directory is: {}'.format(os.getcwd()))
        print([x for x in self.d._dictionary.items()])

    def testAdd(self):
        word = 'stout'
        translation = 'крепкий'
        self.d.add_word(word, translation)
        self.assertIsNotNone(self.d._dictionary[word])
        self.assertIsInstance(self.d._dictionary[word], list)
        self.assertIsInstance(self.d._dictionary[word][0], str)
        self.assertEqual(len(self.d._dictionary[word]), 1)
        self.assertIn(word, self.d._dictionary.keys())
        self.assertIn([translation], self.d._dictionary.values())
        self.assertIn((word, [translation]), self.d._dictionary.items())
        self.assertEqual(self.d._dictionary[word][0], translation)

    def testAddSecondTranslation(self):
        word = 'buxom'
        transOne = 'пышногрудая'
        transTwo = 'сисястая'
        self.d.add_word(word, transOne)
        self.d.add_word(word, transTwo)
        self.assertIsNotNone(self.d._dictionary[word])
        self.assertIsInstance(self.d._dictionary[word], list)
        self.assertIsInstance(self.d._dictionary[word][0], str)
        self.assertIsInstance(self.d._dictionary[word][1], str)
        self.assertEqual(len(self.d._dictionary[word]), 2)
        self.assertIn(word, self.d._dictionary.keys())
        self.assertIn([transOne, transTwo], self.d._dictionary.values())
        self.assertIn((word, [transOne, transTwo]), self.d._dictionary.items())
        self.assertEqual(self.d._dictionary[word][0], transOne)
        self.assertEqual(self.d._dictionary[word][1], transTwo)

    def testWordDeletion(self):
        pass

    def tearDown(self):
        try:
            os.remove(OUTPUT_FILE + '.db')
        except OSError as err:
            print('Unable to remove file')
            print('Error occured: {}'.format(err))
        else:
            print('Test file successfully deleted!')
        self.d.close()

if __name__ == '__main__':
    unittest.main()
