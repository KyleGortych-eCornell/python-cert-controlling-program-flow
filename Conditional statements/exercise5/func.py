"""
func
Descript:


File name:  func.py
Maintainer: Kyle Gortych
created:    03-16-2022
"""
import introcs


def valid_format(s):
    """
    Returns True if s is a valid numerical string; it returns False otherwise.

    A valid numerical string is one with only digits and commas, and commas only
    appear at every three digits.  In addition, a valid string only starts with
    a 0 if it has exactly one character.

    Pay close attention to the precondition, as it will help you (e.g. only numbers
    < 1,000,000 are possible with that string length).

    Examples:
        valid_format('12') returns True
        valid_format('apple') returns False
        valid_format('1,000') returns True
        valid_format('1000') returns False
        valid_format('10,00') returns False
        valid_format('0') returns True
        valid_format('012') returns False

    Parameter s: the string to check
    Precondition: s is nonempty string with no more than 7 characters
    """
    assert len(s) != 0, 'empty str'
    assert len(s) <= 9, 'str exceeds len 9'

    result = True

    # note: elif behaves like an xor gate | evaluates Ǝ! conditional if True else False
    if ((len(s) == 1) and ('0' in s[0])):
        return result

    elif ((len(s) <= 3) and (introcs.isnumeric(s) == True) and
            (',' not in s) and ('0' not in s[0])):
        return result

    elif (len(s) == 4):
        result = False

    elif ((len(s) == 5) and (introcs.isnumeric(s[0]) == True) and
            (introcs.isnumeric(s[2:]) == True) and (',' in s[1]) and
            ('0' not in s[0])):
        return result

    elif ((len(s) == 6) and (introcs.isnumeric(s[:2]) == True) and
            (introcs.isnumeric(s[3:]) == True) and (',' in s[2]) and
            ('0' not in s[0])):
        return result

    elif ((len(s) == 7) and (introcs.isnumeric(s[:3]) == True) and
            (introcs.isnumeric(s[4:]) == True) and (',' in s[3]) and
            ('0' not in s[0])):
        return result

    elif ((len(s) == 9) and (introcs.isnumeric(s[0]) == True) and
            (introcs.isnumeric(s[2:5]) == True) and
            (introcs.isnumeric(s[6:]) == True) and (',' in s[1]) and
            (',' in s[5]) and ('0' not in s[0])):
        return result

    else: result = False

    return result
    #pass
