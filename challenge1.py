
MIN_VALUE = 97
MAX_VALUE = 122


def solution1(x):
    """
    Deciphers string and prints the output.
    :param x: Encrypted string.
    :return: None.
    """
    output = ""
    for ch in x:
        ch_decimal = ord(ch)
        if MIN_VALUE <= ch_decimal <= MAX_VALUE:
            output = output + chr(MAX_VALUE - (ch_decimal - MIN_VALUE))
        else:
            output = output + ch
    print(output)


if __name__ == '__main__':
    test1 = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
    solution1(test1)
