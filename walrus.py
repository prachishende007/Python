if (n:= len([1, 2, 3, 4, 5])) > 3:
    print("List is too long")

# type variable
from typing import List, Tuple, Dict, Union
n : int = 5
name: str = "Harry"

def sum(a: int, b: int)-> int:
    return a+b

num: List[int] = [1, 2, 3, 4, 5]

person: Tuple[str, int] = {"Alice", 17}

