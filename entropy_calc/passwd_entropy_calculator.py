# encoding:utf-8
# calculate enctropy of password supplied

# ver. 1.0

# abcabcabcabcabcabcabcabcabcabcabcabc
# 0123456789

import math

ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

class EntropyCalculator():

    def calc(self, pswd):
        res = []
        if pswd:
            res.append(4) # first symbol -  4 bits
            res.append(len(pswd[1:8])*2) # next 7 symbols (2 bits per symbol)
            res.append(len(pswd[8:20])*1.5) # from 9th to 20th symbols (1.5 bits per symbol)
            res.append(len(pswd[20:])) # from 21st symbols (1 bit per symbol)
            if any([ch in ascii_uppercase and ch in punctuation for ch in pswd]):
                res.append(6) # 6 bit for any non-alphabet symbol or uppercase letter
            return sum(res)
        return 0

    def calc2(self, pswd, possible_number_of_symbols=94):
        # possible_number_of_symbols = 94 # lower and upper case, punctuation and numbers
        if pswd:
            return len(pswd) * math.log2(possible_number_of_symbols)
        return 0

    def calc3(self, pswd, entropy_per_symbol=5.9542):
        if pswd:
            return len(pswd) * entropy_per_symbol
        return 0

    def a(self, p):
        upper = [ch in ascii_uppercase for ch in p]
        punct = [ch in punctuation for ch in p]
        print('Upper: {}'.format(upper))
        print('Punctuation: {}'.format(punct))
        if any(upper) and any(punct):
            return True
        return False

    def b(self, p):
        return p, bool(p in ascii_uppercase), bool(p in punctuation)

    def c(self, p):
        for x in p:
            yield x, bool(x in ascii_uppercase), bool(x in punctuation)


if __name__ == '__main__':
    print('=' * 75)
    a = EntropyCalculator()
    pswd1 = 'adsfjlafLJA'
    pswd2 = 'b4441d6e33f83589a080444a23aa457286034131b0a0e0f0494ced745c8ee84e'
    print(pswd1)
    print(pswd2)
    # print('a calling...')
    # print(a.a(pswd1))
    # print('b calling...')
    # print([a.b(x) for x in pswd1])
    # print('c calling...')
    # print(list(a.c(pswd1)))
    # [print(x) for x in list(a.c(pswd1))]
    print('First method...')
    print(a.calc(pswd1))
    print(a.calc(pswd2))
    print('Second method...')
    print(a.calc2(pswd1))
    print(a.calc2(pswd1, 36))
    print('Third method...')
    print(a.calc3(pswd1))
    print(a.calc3(pswd2, 5.1699))
