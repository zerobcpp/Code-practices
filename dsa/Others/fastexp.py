def fastexp(base, exponent):
    res = 1
    while exponent > 0:
        # If the exponent is odd, multiply the result by the base
        if exponent % 2:
            res = (res * base)

        # Square the base and halve the exponent
        base = (base * base)
        exponent //= 2

    return res