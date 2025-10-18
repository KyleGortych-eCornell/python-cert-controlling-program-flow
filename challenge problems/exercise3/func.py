"""
func
Descript:


File name:  func.py
Maintainer: Kyle Gortych
created:    03-29-2022
"""
def bjack(hand):
    """
    Returns the score of the blackjack hand.

    When scoring the hand, number cards are always worth their value and face cards
    (Jack, Queen, King) are always worth 10.  However, Aces are either worth 1 or 11,
    which ever is more advantageous.

    When determining how to value a hand, the score should be as high as possible without
    going over 21.  If the hand is worth more than 21 points, then all Aces should be
    worth 1 point.

    Examples:
        bjack(('KS','AD')) returns 21
        bjack(('KS','9C','AD')) returns 20
        bjack(('AS','AC','KH')) returns 12
        bjack(('AS','AC','KH','TD')) returns 22
        bjack(()) returns 0

    Parameter hand: the blackjack hand to score
    Precondition: hand is a (possibly empty) tuple of 2-character strings representing
    cards. The first character of each string is '2'-'9', 'T', 'J', 'Q', 'K', or 'A'.
    The second character of each string is 'H', 'D', 'C', or 'S'.
    """
    assert type(hand) == tuple
    # Hint: Keep track of whether you have seen any aces in the hand that are worth 11
    # If so, subtract 10 from the accumulator if you go over.
    var = ','.join(hand)
    nums = []
    idx = 0

    for i in var:
        try:
            if ord(i) in range(50,58):
                nums.append(int(i))
                idx += 1
        except:
            pass

        if i == 'T' or i == 'J' or i == 'Q' or i == 'K':
            nums.append(10)
            idx += 1

        elif i == 'A':
            if sum(nums) < 15 and var.count('A') == 1:
                nums.append(11)
                idx += 1
            else:
                nums.append(1)
                idx += 1

        elif len(hand) == 0:
            nums.append(0)
            idx += 1
        else:
            idx += 1

    return sum(nums)
    #pass
