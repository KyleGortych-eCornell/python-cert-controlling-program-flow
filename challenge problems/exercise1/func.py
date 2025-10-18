"""
func
Descript:


File name:  func.py
Maintainer: Kyle Gortych
created:    03-28-2022
"""
import introcs


def findall(text,sub):
    """
    Returns the tuple of all positions of substring sub in text.

    If sub does not appears anywhere in text, this function returns the empty tuple ().

    Examples:
        findall('how now brown cow','ow') returns (1, 5, 10, 15)
        findall('how now brown cow','cat') returns ()
        findall('jeeepeeer','ee') returns (1,2,5,6)

    Parameter text: The text to search
    Precondition: text is a string

    Parameter sub: The substring to search for
    Precondition: sub is a nonempty string
    """
    assert type(text) == str
    assert type(sub) == str and len(sub) > 0

    idx = 0
    count = 1
    var = []
    sublen = len(sub)

    while count < len(text):
        var2 = introcs.find_str(text[idx:idx + sublen], sub)
        if var2 != -1:
            var.append(idx)
        idx += 1
        count += 1

    return tuple(var)
    #pass
