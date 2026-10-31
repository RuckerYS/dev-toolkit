"""Array and collection utility functions."""

from typing import List, Any, TypeVar

T = TypeVar('T')

def chunk(lst: List[T], size: int) -> List[List[T]]:
    """Split list into chunks of given size."""
    if size <= 0:
        raise ValueError("Chunk size must be positive")
    return [lst[i:i + size] for i in range(0, len(lst), size)]

def unique(lst: List[Any]) -> List[Any]:
    """Return unique elements preserving order."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
