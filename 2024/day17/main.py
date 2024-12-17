import re

p = re.compile(r'(\d+)')

with open("input.txt", "r") as f:
    input = [int(n) for n in re.findall(p, f.read())]

A, B, C = 4, 5, 6
REGISTERS = [0, 1, 2, 3] + input[:3]
PROGRAM = input[3:]

def run_program(registers, program):
    ip = 0
    output = []

    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]
        ip += 2

        if opcode == 0:  # adv: A = A // (2 ** operand)
            registers[A] = registers[A] // (2 ** registers[operand])
        elif opcode == 1:  # bxl: B = B ^ operand
            registers[B] = registers[B] ^ operand
        elif opcode == 2:  # bst: B = combo % 8
            registers[B] = registers[operand] % 8
        elif opcode == 3:  # jnz: if A != 0, jump to operand
            if registers[A] != 0:
                ip = operand
                continue
        elif opcode == 4:  # bxc: B = B ^ C (ignores operand)
            registers[B] = registers[B] ^ registers[C]
        elif opcode == 5:  # out: output combo % 8
            output.append(registers[operand] % 8)
        elif opcode == 6:  # bdv: B = A // (2 ** operand)
            registers[B] = registers[A] // (2 ** registers[operand])
        elif opcode == 7:  # cdv: C = A // (2 ** operand)
            registers[C] = registers[A] // (2 ** registers[operand])

    return output

def run_program_reverse(registers, program, idx = 1):
    if idx > len(program):
        return registers[A]

    vs = []
    n_registers = registers[:]
    for word in range(8):
        n_registers[A] = (registers[A] << 3) | word
        if run_program(n_registers[:], program) == program[-idx:]:
            result = run_program_reverse(n_registers, program, idx + 1)
            if result is not None:
                vs.append(result)

    return min(vs) if vs else None

print("Part 1:", ",".join(map(str, run_program(REGISTERS[:], PROGRAM))))
print("Part 2:", run_program_reverse([0, 1, 2, 3, 0] + REGISTERS[5:], PROGRAM))