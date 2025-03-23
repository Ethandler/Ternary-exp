class TernaryLogic:
    """
    Implements ternary logic gates (AND, OR, NOT) using 3,6,9 instead of -1,0,1.
    """

    @staticmethod
    def ternary_and(a, b):
        """
        Ternary AND operation.
        Returns the minimum of the two ternary values.
        """
        return min(a, b)

    @staticmethod
    def ternary_or(a, b):
        """
        Ternary OR operation.
        Returns the maximum of the two ternary values.
        """
        return max(a, b)

    @staticmethod
    def ternary_not(a):
        """
        Ternary NOT operation.
        Flips 3 (negative) to 9 (positive), 9 to 3, and keeps 6 (neutral) as is.
        """
        return 9 if a == 3 else 3 if a == 9 else 6  # 6 stays the same

# Example Usage
print("Ternary AND (9,3):", TernaryLogic.ternary_and(9, 3))  # Expected: 3
print("Ternary OR (9,3):", TernaryLogic.ternary_or(9, 3))    # Expected: 9
print("Ternary NOT (9):", TernaryLogic.ternary_not(9))       # Expected: 3
print("Ternary NOT (6):", TernaryLogic.ternary_not(6))       # Expected: 6
print("Ternary NOT (3):", TernaryLogic.ternary_not(3))       # Expected: 9

