! /usr/bin/env python3
'''
This module is an audio trainer for learning pseudonumerology
'''

import pyttsx3

import pseudonum

PLEASANT_ENGLISH_FEMALE_VOICE_INDEX = 17

if __name__ == '__main__':
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[PLEASANT_ENGLISH_FEMALE_VOICE_INDEX].id)
    engine.setProperty('rate', 150)
    for i in range(len(pseudonum.NUMERAL_CONSONANTS)):
        sentence = f"The digit {i} maps to "
        num_sounds = len(pseudonum.NUMERAL_CONSONANTS[i])
        if num_sounds > 1:
            sounds_printed = 0
            sentence += f"{num_sounds} different letter combinations: "
            for j in range(num_sounds):
                sentence += f"'{pseudonum.NUMERAL_CONSONANTS[i][j]}'"
                if j < (num_sounds - 1):
                    sentence += ", "
                    if j == (num_sounds - 2):
                        sentence += "and "
                else:
                    sentence += "."     
        else:
            sentence += f"letter combination: '{pseudonum.NUMERAL_CONSONANTS[i][0]}'."
        engine.say(sentence)
        engine.runAndWait()
