"""
funcs
Descript:


File name:  funcs.py
Maintainer: Kyle Gortych
created:    03-16-2022
"""
import introcs


def first_vowel(s):
    """
    Returns the position of the first vowel in s; it returns -1 if there are no vowels.

    We define the vowels to be the letters 'a','e','i','o', and 'u'.  The letter
    'y' counts as a vowel only if it is not the first letter in the string.

    Examples:
        first_vowel('hat') returns 1
        first_vowel('grrm') returns -1
        first_vowel('sky') returns 2
        first_vowel('year') returns 1

    Parameter s: the string to search
    Precondition: s is a nonempty string with only lowercase letters
    """
    assert introcs.isalpha(s), 'not alpha'
    assert introcs.islower(s), 'not lowercase'

    result = len(s)

    if 'a' in s:
        result = introcs.index_str(s, 'a')

    if 'e' in s:
        if result > introcs.index_str(s, 'e'):
            result = introcs.index_str(s, 'e')

    if 'i' in s:
        if result > introcs.index_str(s, 'i'):
            result = introcs.index_str(s, 'i')

    if 'o' in s:
        if result > introcs.index_str(s, 'o'):
            result = introcs.index_str(s, 'o')

    if 'u' in s:
        if result > introcs.index_str(s, 'u'):
            result = introcs.index_str(s, 'u')

    if 'y' in s:
        if ((introcs.count_str(s, 'y') == 1 and
                introcs.index_str(s, 'y') != 0) or
                introcs.count_str(s, 'y') > 1):
                if result > introcs.index_str(s, 'y', 1):
                    result = introcs.index_str(s, 'y', 1)

    return result if (('a' in s or 'e' in s or 'i' in s or
            'o' in s or 'u' in s or 'y' in s) and result != len(s)) else -1
    # pass


def pigify(s):
    """
    Returns a copy of s converted to Pig Latin

    Pig Latin is childish encoding of English that adheres to the following rules:

    1.  The vowels are 'a', 'e', 'i', 'o', 'u', as well as any 'y'
        that is not the first letter of a word. All other letters are consonants.

        For example, 'yearly' has three vowels  ('e', 'a', and the last 'y')
        and three consonants (the first 'y', 'r', and 'l').

    2.  If the English word begins with a vowel, append 'hay' to the end of the word
        to get the Pig Latin equivalent. For example, 'ask 'askhay' and 'use' becomes
        'usehay'.

    3.  If the English word starts with 'q', then it must be followed by'u'; move
        'qu' to the end of the word, and append 'ay'.  Hence 'quiet' becomes
        'ietquay' and 'quay' becomes 'ayquay'.

    4.  If the English word begins with a consonant, move all the consonants up to
        the first vowel (if any) to the end and add 'ay'.  For example, 'tomato'
        becomes 'omatotay', 'school' becomes 'oolschay'. 'you' becomes 'ouyay' and
        'ssssh' becomes 'sssshay'.

    Parameter s: the string to change to Pig Latin
    Precondition: s is a nonempty string with only lowercase letters. If s starts with
    'q', then it starts with 'qu'.
    """
    assert type(s) == str
    assert introcs.isalpha(s) == True

    s2 = introcs.strip(s, s[:first_vowel(s)])

    if (first_vowel(s) == 0):
        result = s + 'hay'

    elif (('q' in s[0]) and ('u' not in s[2])):
        result = introcs.strip(s, s[:2]) + 'quay'

    elif (('q' in s[0]) and ('u' in s[2])):
        result = 'u' + introcs.strip(s, 'qu') + 'quay'

    elif ((first_vowel(s) > 0) and ('q' not in s[0])):
        result =  s2 + s[:first_vowel(s)] + 'ay'

    elif ('y' in s[0] and 'y' in s[1:]):
        result = 

    else: result = s + 'ay'

    return result
    #pass
