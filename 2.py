import sys


def op(program, counter):
    cmd = program[counter]
    x1 = program[program[counter + 1]]
    x2 = program[program[counter + 2]]
    if cmd == 1:
        return x1 + x2
    if cmd == 2:
        return x1 * x2

    raise ValueError


def run(program, p1, p2):
    program = program.copy()
    program[1] = p1
    program[2] = p2
    counter = 0
    while counter <= len(program):
        cmd = program[counter]
        if cmd in [1, 2]:
            program[program[counter + 3]] = op(program, counter)
            counter += 4
        elif cmd == 99:
            return program[0]
            break
        else:
            raise ValueError


input = [int(x) for x in sys.argv[1:]]
print(run(input, 12, 2))

p1 = 0
p2 = 0
target = 19690720
while run(input, p1, p2) < target:
    p1 += 1

p1 -= 1
p2 = target - run(input, p1, p2)
print(100 * p1 + p2)
