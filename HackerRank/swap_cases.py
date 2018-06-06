def swap(s):
    if str.islower(s):
        return str.upper(s)
    elif str.isupper(s):
        return str.lower(s)
    else:
        return s


def swap_case(s):
    return ''.join(list(map(swap, s)))


s = input()
result = swap_case(s)
print(result)
