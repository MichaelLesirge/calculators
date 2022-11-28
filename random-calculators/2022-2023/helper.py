def sint(x):
    x = float(x)
    if str(x)[-2:] == ".0":
        return int(x)
    return x