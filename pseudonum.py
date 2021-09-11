#! /usr/bin/env python3
'''
This module contains data structures that are used to map sounds to integers.
Pseudonumerology uses these maps to help improve human memory for digits.

These mnemonic mappings were obtained from Wikipedia (`https://en.wikipedia.org/wiki/Mnemonic_major_system`)
on 2021-Sep-11.
'''


NUMERAL_CONSONANTS = [
    ['s', 'z'],             # 0
    ['t', 'd', 't h'],       # 1
    ['n'],                  # 2
    ['m'],                  # 3
    ['r'],                  # 4
    ['l'],                  # 5
    ['c h', 's h', 'j', 'z h'],# 6
    ['k', 'q', 'hard g'],      # 7
    ['f', 'v'],             # 8
    ['p', 'b']              # 9
    ]

ONE_DIGIT_PEGS = [
    ['hose', 'sew', 'easy'],    # 0
    ['hat', 'hate', 'hot'],     # 1
    ['hen', 'know', 'new'],     # 2
    ['home', 'aim', 'yummy'],   # 3
    ['arrow', 'row', 'hairy'],  # 4
    ['whale', 'heal', 'oily'],  # 5
    ['shoe', 'chew', 'itchy'],  # 6
    ['cow', 'hook', 'gay'],     # 7
    ['hoof', 'view', 'heavy'],  # 8
    ['pie', 'buy', 'happy']     # 9
    ]

