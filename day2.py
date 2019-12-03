# day 2
from typing import List

def run_code(intcode):
    pos = 0
    while pos < len(intcode):
        [opc, pos1, pos2, out] = intcode[pos:pos+4]
        if opc == 99:
            return intcode[0]
        elif opc == 1:
            intcode[out] = intcode[pos1] + intcode[pos2]
        elif opc == 2:
            intcode[out] = intcode[pos1] * intcode[pos2]
        else:
            print(f'unknown op {opc} at pos {pos}')
        pos += 4

def find_noun_verb():
    for noun in range(100):
        for verb in range(100):
            ic = intcode[:]
            ic[1] = noun
            ic[2] = verb

            result = run_code(ic)

            if result == 19690720:
                print(f'noun:{noun}, verb:{verb}, value:{100 * noun + verb}')


if __name__ == "__main__":

    with open('day2_input.txt') as f:
        intcode = [int(i) for i in f.read().split(',')]

    # do alts
    intcode[1] = 12
    intcode[2] = 2

    # part 1
    # run_code(intcode)

    # part 2
    find_noun_verb()
