# AIM: To reverse string, integer, list, and tuple using Python class and functions

class Reverser:
    def reverse_string(self, text: str) -> str:
        """Reverse a given string."""
        return text[::-1]

    def reverse_integer(self, num: int) -> int:
        """Reverse a given integer."""
        reversed_str = str(num)[::-1]
        return int(reversed_str) if num >= 0 else -int(reversed_str[:-1])

    def reverse_list(self, lst: list) -> list:
        """Reverse a list."""
        return lst[::-1]

    def reverse_tuple(self, tpl: tuple) -> tuple:
        """Reverse a tuple."""
        return tpl[::-1]


# --------------------------
# Example usage
# --------------------------
if __name__ == "__main__":
    r = Reverser()

    # Reverse string
    text = "HELLO"
    print("Original String:", text)
    print("Reversed String:", r.reverse_string(text))

    # Reverse integer
    number = 12345
    print("\nOriginal Integer:", number)
    print("Reversed Integer:", r.reverse_integer(number))

    # Reverse list
    lst = [10, 20, 30, 40, 50]
    print("\nOriginal List:", lst)
    print("Reversed List:", r.reverse_list(lst))

    # Reverse tuple
    tpl = (1, 2, 3, 4, 5)
    print("\nOriginal Tuple:", tpl)
    print("Reversed Tuple:", r.reverse_tuple(tpl))