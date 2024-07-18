from day19_1 import set_up_elves


def main(num_elves):
    current_elf = set_up_elves(num_elves)
    while current_elf.left is not current_elf:
        print(f"{current_elf.index=}")
        # TODO: It has to be this call that is the slow part that needs to speed up
        # Probably need to develop more of a hash table tracker or something
        # Oooh, or some kind of b-tree or something
        # One obvious first improvement is that we go around the loop 1 time to calculate how many steps
        # then another half time around to find the elf to remove...
        # So the first step would be to stop going around that first time and instead just keep track of the number of elves
        stealee = current_elf.find_stealee()
        current_elf.presents += stealee.presents
        stealee.presents = 0
        stealee.remove()
        current_elf = current_elf.left

    return current_elf.index


if __name__ == '__main__':
    print(main(3_005_290))
