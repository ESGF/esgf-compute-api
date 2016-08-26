"""
Utilities Module.
"""

def int_or_float(number):
    """ Tries to convert string to int or float. """
    try:
        return int(number)
    except ValueError:
        return float(number)
