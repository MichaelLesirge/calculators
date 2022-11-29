def sint(x):
    x = float(x)
    if str(x)[-2:] == ".0" or x % 1 <= 0.00000000000001:
        return int(x)
    return x
