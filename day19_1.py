class Elf:
    def __init__(self, index, right=None):
        self.index = index
        self.presents = 1
        self.right = right
        if self.right:
            self.right.left = self
        self.left = None

    def __repr__(self):
        s = f'Elf #{self.index}; presents: {self.presents}'
        s += f'; left: {self.left.index}' if self.left else '; left: None'
        s += f'; right: {self.right.index}' if self.right else '; right: None'
        return s

    def steal_presents(self):
        """only used in part 1"""
        self.presents += self.left.presents
        self.left = self.left.left
        self.left.right = self

    def remove(self):
        self.left.right = self.right
        self.right.left = self.left

    def find_stealee(self):
        num_elves_in_circle = 1
        current = self.left
        while current is not self:
            num_elves_in_circle += 1
            current = current.left

        num_times_to_step = num_elves_in_circle // 2
        stealee = self
        for _ in range(num_times_to_step):
            stealee = stealee.left

        return stealee


def main(num_elves):
    current_elf = set_up_elves(num_elves)
    while current_elf.left is not current_elf:
        current_elf.steal_presents()
        current_elf = current_elf.left

    return current_elf.index


def set_up_elves(num_elves):
    first_elf = Elf(1)
    prev_elf = first_elf
    for i in range(2, num_elves):
        elf = Elf(i, prev_elf)
        prev_elf = elf
    last_elf = Elf(num_elves, prev_elf)
    last_elf.left = first_elf
    first_elf.right = last_elf
    current_elf = first_elf
    return current_elf


if __name__ == '__main__':
    print(main(3_005_290))
