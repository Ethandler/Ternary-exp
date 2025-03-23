# ternary_cpu.py
from ternary_alu import TernaryALU
from ternary_logic import TernaryLogic  # Ensure this exists (for NOT operation)
from balanced_ternary import BalancedTernary  # Ensure this exists (for number representation)

class TernaryCPU:
    """ 
    A hybrid ternary CPU with registers, ALU operations, and logical execution. 
    """

    def __init__(self):
        """ Initialize CPU with registers and ALU """
        self.registers = [6] * 4  # Default to neutral (0)
        self.pc = 0  # Program Counter
        self.memory = []
        self.alu = TernaryALU()

    def load_program(self, instructions):
        """ Load a list of instructions into memory. """
        self.memory = instructions

    def execute(self):
     """ Executes stored instructions in ternary with conditional logic. """
     while self.pc < len(self.memory):
        op, reg, value = self.memory[self.pc]

        if op == "SET":
            self.registers[reg] = value
        elif op == "ADD":
            self.registers[reg] = self.alu.add(self.registers[reg], value)
        elif op == "SUB":
            self.registers[reg] = self.alu.subtract(self.registers[reg], value)
        elif op == "MUL":
            self.registers[reg] = self.alu.multiply(self.registers[reg], value)
        elif op == "NOT":
            self.registers[reg] = TernaryLogic.ternary_not(self.registers[reg])
        elif op == "JUMP":
            new_pc = self.alu.jump_if_positive(self.registers[reg], value)
            if new_pc is not None:
                self.pc = new_pc
                continue
        elif op == "IF-GOTO":
            """New conditional jump: If register value is 9, jump to instruction"""
            if self.registers[reg] == 9:
                self.pc = value
                continue  # Skip incrementing PC

        self.pc += 1

    def __str__(self):
        """ Print CPU register states """
        return f"Registers: {self.registers}"


# Example Program (SET, ADD, NOT, JUMP)
if __name__ == "__main__":
    cpu = TernaryCPU()
    program = [
        ("SET", 0, 9),   # Set Register 0 to 9 (1)
        ("SET", 1, 3),   # Set Register 1 to 3 (-1)
        ("ADD", 0, 3),   # Add -1 to Register 0
        ("NOT", 0, None), # NOT operation on Register 0
        ("JUMP", 0, 2)   # Jump if Register 0 is positive
    ]

    cpu.load_program(program)
    cpu.execute()
    print(cpu)  # Expected to show updated registers
