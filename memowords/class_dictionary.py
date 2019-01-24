# encoding:utf-8
# class dictionary for memowords kivy framework application

# ==============================================================================
# *******************     from shelve documentation      ***********************
# ==============================================================================
# Normally, d[key] returns a COPY of the entry.  This needs care when
#    mutable entries are mutated: for example, if d[key] is a list,
#            d[key].append(anitem)
#    does NOT modify the entry d[key] itself, as stored in the persistent
#    mapping -- it only modifies the copy, which is then immediately
#    discarded, so that the append has NO effect whatsoever.  To append an
#    item to d[key] in a way that will affect the persistent mapping, use:
#            data = d[key]
#            data.append(anitem)
#            d[key] = data

# To avoid the problem with mutable entries, you may pass the keyword
# argument writeback=True in the call to shelve.open.  When you use:
#         d = shelve.open(filename, writeback=True)
# then d keeps a cache of all entries you access, and writes them all back
# to the persistent mapping when you call d.close().  This ensures that
# such usage as d[key].append(anitem) works as intended.
# However, using keyword argument writeback=True may consume vast amount
# of memory for the cache, and it may make d.close() very slow, if you
# access many of d's entries after opening it in this way: d has no way to
# check which of the entries you access are mutable and/or which ones you
# actually mutate, so it must cache, and write back at close, all of the
# entries that you access.  You can call d.sync() to write back all the
# entries in the cache, and empty the cache (d.sync() also synchronizes
# the persistent dictionary on disk, if feasible)
# ==============================================================================

import shelve
import sys
import random

# directory = '/Users/alexanderuperenko/Desktop/Python - my projects/kivy-training/memowords'

OUTFILE = 'dictionary.shelve_file'

class Dictionary():
    ''' Pairs word/translation are stored in '._dictionary' attribute. '''

    def __init__(self, output_file=OUTFILE):
        try:
            self._dictionary = shelve.open(output_file, 'w')
        except Exception as err:
            print('Error occured: {}'.format(err))
            self._dictionary = shelve.open(output_file, 'c')
            print('File successfully created')
        else:
            print('File successfully read')
            print('Keys: {}'.format(list(key for key in self._dictionary.keys())))
        return None

    def show_dictionary(self):
        # dictionary to be used, 'get method' required
        return {key:item for key, item in self._dictionary.items()}

    def add_word(self, word, translation):
        if word and translation:
            try:
                str(word)
            except TypeError as err:
                print('"{}" is not a string'.format(word))
                print('Error: {}'.format(err))
            else:
                if word in self._dictionary and translation not in self._dictionary[word]:
                    temp = self._dictionary[word]
                    temp.append(translation)
                    self._dictionary[word] = temp
                    print('Appended translation {} to {}'.format(translation, word))
                else:
                    self._dictionary[word] = [translation]
                    print('Created entry: {} - {}'.format(word, translation))
        else:
            print('Empty word or translation')
        return None

    def remove_word(self, word):
        try:
            del self._dictionary[word]
        except Exception as err:
            print('Can\'t remove "{}" from dictionary'.format(word))
            print('Error: {}'.format(err))
        else:
            print('{} successfully deleted.'.format(word))
        return None

    # edit word or its translation
    def edit_word(self, word, translation):
        # should word with selection in recycleview
        # print('Prepare to edit...')
        pass

    def search_word(self, target):
        target = target.lower()
        return {key:self._dictionary[key] for key in self._dictionary.keys() if key.startswith(target)}

    def get_random_word(self):
        ''' Returns tuple (random_word, self._dictionary[random_word]) '''
        # print('Type of self._dictionary: {}'.format(type(self._dictionary)))
        keys = [key for key in self._dictionary.keys()]
        # print('keys: {}'.format(keys))
        random_word = random.choice(keys)
        # print('Random word: {}'.format(random_word))
        return (random_word, self._dictionary[random_word])

    def close(self):
        self._dictionary.close()

    def _validate(self, word):
        # type(word) -> string
        # consist of letters only
        # string.ascii_letters
        pass


if __name__ == '__main__':
    d = Dictionary('test-test')
    print('Random_word tuple is {}'.format(d.get_random_word()))
