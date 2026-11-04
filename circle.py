import math


def area(r):
    """
    Вычисляет площадь круга по заданному радиусу.

    Args:
        r (float): радиус круга.

    Returns:
        float: площадь круга.

    Example:
        >>> area(4)
        50.26548245743669
    """
    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет длину окружности по заданному радиусу.

    Args:
        r (float): радиус круга.

    Returns:
        float: длина окружности.

    Example:
        >>> perimeter(4)
        25.132741228718345
    """
    return 2 * math.pi * r