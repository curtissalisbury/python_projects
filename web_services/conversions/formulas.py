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
