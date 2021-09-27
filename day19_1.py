def find_next_elf_with_presents(presents, elf):
    next_elf = (elf + 1) % len(presents)
    while not presents[next_elf]:
        next_elf = (next_elf + 1) % len(presents)

    return next_elf


def main(num_elves):
    presents = [1] * num_elves

    elf = 0
    while len([present for present in presents if present]) > 1:
        if presents[elf]:
            next_elf_with_presents = find_next_elf_with_presents(presents, elf)
            presents[elf] += presents[next_elf_with_presents]
            presents[next_elf_with_presents] = 0
        elf = (elf + 1) % len(presents)
    for i, p in enumerate(presents):
        if p:
            return i+1


if __name__ == '__main__':
    print(main(3005290))
