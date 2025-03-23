# ternary_alu.py
class TernaryALU:
    """ Handles ternary arithmetic and logic (3,6,9 instead of -1,0,1). """

    def add(self, a, b):
        return min(9, max(3, a + b))  # Clamped to ternary range

    def subtract(self, a, b):
        return min(9, max(3, a - b))

    def multiply(self, a, b):
        return self.to_ternary(self.to_decimal(a) * self.to_decimal(b))

    def jump_if_positive(self, value, jump_address):
        return jump_address if value == 9 else None

    def to_decimal(self, ternary_value):
        return -1 if ternary_value == 3 else 0 if ternary_value == 6 else 1

    def to_ternary(self, decimal_value):
        return 3 if decimal_value < 0 else 6 if decimal_value == 0 else 9
