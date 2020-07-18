"""
Functions for calculating conversions
"""


def kilometers_to_miles(kilometers: float):
    """
    Convert kilometers to miles
    :param kilometers: number of kilometers to convert
    :return: converted miles
    """
    if kilometers <= 0:
        return ValueError

    miles = kilometers * 0.62137
    return round(miles, 2)


def miles_to_kilometers(miles: float):
    """
    Convert miles to kilometers
    :param miles: number of miles to convert
    :return: converted kilometers
    """
    if miles <= 0:
        return ValueError

    kilometers = miles * 1.609344
    return round(kilometers, 2)


def grams_to_ounces(grams: float):
    """
    Convert grams into ounces
    :param grams: number of grams to convert
    :return: converted ounces
    """
    if grams <= 0:
        return ValueError

    ounces = grams * 0.035274
    return round(ounces, 2)


def ounces_to_grams(ounces: float):
    """
    Convert ounces into grams
    :param ounces: number of ounces to convert
    :return: converted grams
    """
    if ounces <= 0:
        return ValueError

    grams = ounces * 28.35
    return round(grams, 2)
