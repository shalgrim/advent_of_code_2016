import itertools
from copy import copy

PrG = 'PG'
PrM = 'PM'
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

    def solve(self):
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


if __name__ == '__main__':
    p = Puzzle(FLOORS)
    p.solve()
    print(p.seen_states[p.terminating_condition])