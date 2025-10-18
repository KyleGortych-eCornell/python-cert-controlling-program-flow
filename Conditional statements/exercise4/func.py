"""
func
Descript:


File name:  func.py
Maintainer: Kyle Gortych
created:    03-14-2022
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
