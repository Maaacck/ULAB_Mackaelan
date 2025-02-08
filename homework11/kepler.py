# File: kepler.py
def moduleKepler(planet):
    # Calculate orbital period given semi-major axis.
    period = (planet**3)**(1/2)
    return period