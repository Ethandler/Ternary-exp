class BalancedTernary:
    """
    A class to handle computations in a Balanced Ternary system using 3,6,9 instead of -1,0,1.
    """

    def __init__(self, value):
        """
        Initializes a number in balanced ternary (3,6,9 representation)
        from either a decimal integer or an existing balanced ternary list.
        """
        if isinstance(value, int):
            self.ternary = self.decimal_to_balanced_ternary(value)
        elif isinstance(value, list):
            self.ternary = value
        else:
            raise ValueError("Input must be an integer or a list of 3,6,9 values.")

    def decimal_to_balanced_ternary(self, num):
        """
        Converts a decimal number to balanced ternary using 3,6,9 instead of -1,0,1.
        """
        if num == 0:
            return [6]  # 0 in balanced ternary
        
        ternary = []
        while num != 0:
            remainder = num % 3
            num //= 3
            
            if remainder == 2:  # Convert 2 to -1 (represented as 3)
                remainder = -1
                num += 1  # Carry the balance
            
            # Convert -1,0,1 to 3,6,9
            ternary.append(9 if remainder == 1 else 6 if remainder == 0 else 3)

        return ternary[::-1]  # Reverse for correct order

    def balanced_ternary_to_decimal(self):
        """
        Converts the stored balanced ternary (3,6,9) back to decimal.
        """
        decimal_value = 0
        power = 1  # Start at 3^0
        
        for digit in reversed(self.ternary):
            trit = 1 if digit == 9 else 0 if digit == 6 else -1
            decimal_value += trit * power
            power *= 3

        return decimal_value

    def add(self, other):
        """
        Adds two balanced ternary numbers.
        """
        dec_sum = self.balanced_ternary_to_decimal() + other.balanced_ternary_to_decimal()
        return BalancedTernary(dec_sum)

    def multiply(self, other):
        """
        Multiplies two balanced ternary numbers.
        """
        dec_product = self.balanced_ternary_to_decimal() * other.balanced_ternary_to_decimal()
        return BalancedTernary(dec_product)

    def __str__(self):
        """
        Returns a human-readable string of the ternary representation.
        """
        return ''.join(str(x) for x in self.ternary)

# Example Usage
num1 = BalancedTernary(7)
num2 = BalancedTernary(-4)

print("Balanced Ternary Representation of 7:", num1)  # Should output a list of 3,6,9
print("Balanced Ternary Representation of -4:", num2)

# Convert back to decimal
print("Converted Back to Decimal (7):", num1.balanced_ternary_to_decimal())
print("Converted Back to Decimal (-4):", num2.balanced_ternary_to_decimal())

# Addition
sum_result = num1.add(num2)
print("Sum in Balanced Ternary:", sum_result)

# Multiplication
product_result = num1.multiply(num2)
print("Product in Balanced Ternary:", product_result)

