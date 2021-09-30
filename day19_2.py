from day19_1 import set_up_elves


def main(num_elves):
    current_elf = set_up_elves(num_elves)
    while current_elf.left is not current_elf:
        stealee = current_elf.find_stealee()
        current_elf.presents += stealee.presents
        stealee.presents = 0
        stealee.remove()
        current_elf = current_elf.left

    return current_elf.index


if __name__ == '__main__':
    print(main(3_005_290))
