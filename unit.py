def unit(x, y):
    mag = (x**2 + y**2) ** 0.5
    if mag == 0:
        raise ValueError("Cannot calculate the unit vector of a zero vector.")
    ux = x / mag
    uy = y / mag
    uxy = [ux, uy]
    return uxy
