import threading

class TernaryCPU:
    def __init__(self):
        self.registers = [6] * 4
        self.pc = 0
        self.memory = []
        self.running = False
        self.thread = None

    def load_program(self, instructions):
        self.memory = instructions

    def start(self):
        """Starts execution in a separate thread."""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.execute, daemon=True)
            self.thread.start()

    def stop(self):
        """Stops execution safely."""
        self.running = False
        if self.thread:
            self.thread.join()

    def execute(self):
        """Executes instructions in ternary logic."""
        while self.running and self.pc < len(self.memory):
            op, reg, value = self.memory[self.pc]
            if op == "SET":
                self.registers[reg] = value
            elif op == "ADD":
                self.registers[reg] = self.add(self.registers[reg], value)
            elif op == "JUMP":
                if self.registers[reg] == 9:
                    self.pc = value
                    continue
            self.pc += 1

    def add(self, a, b):
        """Performs balanced ternary addition."""
        dec_a = -1 if a == 3 else 0 if a == 6 else 1
        dec_b = -1 if b == 3 else 0 if b == 6 else 1
        dec_sum = dec_a + dec_b
        return 3 if dec_sum < 0 else 6 if dec_sum == 0 else 9

    def __str__(self):
        return f"Registers: {self.registers}"
