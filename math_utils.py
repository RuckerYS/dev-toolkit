"""Math and numeric helper functions."""


def clamp(value: float, min_val: float, max_val: float) -> float:
    """Clamp value between min_val and max_val."""
    return max(min_val, min(value, max_val))


def lerp(start: float, end: float, t: float) -> float:
    """Linear interpolation between start and end."""
    return start + t * (end - start)


def is_even(n: int) -> bool:
    """Check if number is even."""
    return n % 2 == 0
