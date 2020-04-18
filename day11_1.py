import itertools
from copy import copy

PrG = 'PrG'
PrM = 'PrM'
CoG = 'CoG'
CuG = 'CuG'
RG = 'RG'
PlG = 'PlG'
CoM = 'CoM'
CuM = 'CuM'
RM = 'RM'
PlM = 'PlM'

FLOORS = [
    [PrG, PrM],
    [CoG, CuG, RG, PlG],
    [CoM, CuM, RM, PlM],
    [],
]


class Puzzle(object):
    def __init__(self, floors, steps=0, floor_num=0, seen_states=None):
        self.floors = floors
        self.steps = steps
        self.current_floor_num = floor_num
        self.seen_states = seen_states if seen_states else {}

    @property
    def current_floor(self):
        return self.floors[self.current_floor_num]

    @property
    def lower_floor(self):
        if self.current_floor_num == 0:
            return None
        return self.floors[self.current_floor_num - 1]

    @property
    def higher_floor(self):
        if self.current_floor_num == len(self.floors) - 1:
            return None
        return self.floors[self.current_floor_num + 1]

    @property
    def available_items(self):
        return self.floors[self.current_floor_num]

    @staticmethod
    def is_valid_floor(floor):
        chips = [item for item in floor if item[-1] == 'M']
        unmatched_chips = [c for c in chips if c[:-1] + 'G' not in floor]

        if unmatched_chips and any([item[-1] == 'G' for item in floor]):
            return False

        return True

    @property
    def terminating_condition(self):
        all_items = [item for floor in self.floors for item in floor]
        desired_top_floor = ','.join(sorted(all_items))
        newlines = '\n' * len(self.floors)
        return f'{len(self.floors)-1}{newlines}{desired_top_floor}'

    def is_valid_floor_num(self, fnum):
        return self.is_valid_floor(self.floors[fnum])

    def is_complete(self):
        return repr(self) == self.terminating_condition

    def is_valid(self):
        return all(self.is_valid_floor(f) for f in self.floors)

    def generate_next_states(self):
        item_combos = list(itertools.combinations(self.available_items, 2)) + [
            (ai,) for ai in self.available_items
        ]

        answer = []

        for combo in item_combos:
            if self.higher_floor is not None:
                newp = self.produce_move(combo, 'UP')
                if newp.is_valid():
                    answer.append(newp)

            if self.lower_floor is not None:
                newp = self.produce_move(combo, 'DOWN')
                if newp.is_valid():
                    answer.append(newp)

        return answer

    def produce_move(self, combo, direction):
        new_floors = copy(self.floors)
        new_current_floor = copy(self.current_floor)
        for c in combo:
            new_current_floor.remove(c)
        new_floors[self.current_floor_num] = new_current_floor

        if direction == 'UP':
            new_higher_floor = copy(self.higher_floor)
            new_higher_floor.extend(list(combo))
            new_floors[self.current_floor_num + 1] = new_higher_floor
            newp = Puzzle(new_floors, self.steps + 1, self.current_floor_num + 1, self.seen_states)
        elif direction == 'DOWN':
            new_lower_floor = copy(self.lower_floor)
            new_lower_floor.extend(list(combo))
            new_floors[self.current_floor_num - 1] = new_lower_floor
            newp = Puzzle(new_floors, self.steps + 1, self.current_floor_num - 1, self.seen_states)
        else:
            raise Exception('wut')

        return newp

    def solve(self):
        """Used for DFS solving"""
        if any(not self.is_valid_floor(floor) for floor in self.floors):
            return

        if repr(self) in self.seen_states:  # already been here...
            if self.steps >= self.seen_states[repr(self)]:  # ...and in same or fewer steps
                return

        self.seen_states[repr(self)] = self.steps

        if self.is_complete():
            return

        item_combos = list(itertools.combinations(self.available_items, 2)) + [
            (ai,) for ai in self.available_items
        ]

        for combo in item_combos:
            if self.higher_floor is not None:  # I can move up
                new_floors = copy(self.floors)
                new_current_floor = copy(self.current_floor)
                new_higher_floor = copy(self.higher_floor)
                new_higher_floor.extend(list(combo))

                for c in combo:
                    new_current_floor.remove(c)

                new_floors[self.current_floor_num] = new_current_floor
                new_floors[self.current_floor_num + 1] = new_higher_floor

                newp = Puzzle(new_floors, self.steps + 1, self.current_floor_num + 1, self.seen_states)
                newp.solve()

            if self.lower_floor is not None:  # I can move down
                new_floors = copy(self.floors)
                new_current_floor = copy(self.current_floor)
                new_lower_floor = copy(self.lower_floor)
                new_lower_floor.extend(list(combo))

                for c in combo:
                    new_current_floor.remove(c)

                new_floors[self.current_floor_num] = new_current_floor
                new_floors[self.current_floor_num - 1] = new_lower_floor

                newp = Puzzle(new_floors, self.steps + 1, self.current_floor_num - 1, self.seen_states)
                newp.solve()

    def __repr__(self):
        lines = [str(self.current_floor_num)]
        lines += [','.join(sorted(floor)) for floor in self.floors]
        return '\n'.join(lines)


def shortest_path_solver(floors):
    puzzles = [Puzzle(floors)]
    steps = 0
    seen_states = {}
    while not any(p.is_complete() for p in puzzles):
        for p in puzzles:
            if repr(p) not in seen_states:
                seen_states[repr(p)] = steps
        steps += 1

        new_puzzles = []
        for p in puzzles:
            next_states = p.generate_next_states()
            new_puzzles += [ns for ns in next_states if repr(ns) not in seen_states]

        d = {repr(np): np for np in new_puzzles}
        puzzles = list(d.values())

    return steps


if __name__ == '__main__':
    # DFS
    # p = Puzzle(FLOORS)
    # p.solve()
    # print(p.seen_states[p.terminating_condition])

    # BFS
    print(shortest_path_solver(FLOORS))
